from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from users.models import User
from devices.api.serializers import DeviceSerializer
from devices.models import Device
from datetime import datetime
import threading
import cv2 as cv
import time
import os
# import ffmpeg
# import schedule


class DevicesViewSet(ModelViewSet):
    serializer_class = DeviceSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = (TokenAuthentication,)

    def get_queryset(self):
        username = self.request.user  # fazer a busca pelo token ?
        queryset = User.objects.filter(username__exact=username)
        company = queryset[0].id_company
        return Device.objects.filter(id_company=company)

    def destroy(self, request):
        return Response(status=status.HTTP_403_FORBIDDEN)

    @action(detail=True, methods=['post'])
    def shed_record(self, request, pk=None):
        t = threading.Thread(target=self.start_record, args=(request.data['access_address'], pk,), daemon=True)
        t.start()
        return Response({'device': request.data['access_address']})

    def start_record(self, endereco, id):
        print('Gravando de ' + endereco)
        cap = cv.VideoCapture(endereco)
        if not cap.isOpened():
            print("Cannot open camera")
            exit()
        # fourcc = cv.VideoWriter_fourcc(*'XVID')
        fourcc = cv.VideoWriter_fourcc(*'mp4v')
        time_now = datetime.now().strftime('%d%m%Y_%H%M%S')
        # filename = 'cam_' + id + '_at_' + time_now + '.avi'
        filename = 'cam_' + id + '_at_' + time_now + '.mp4'
        print('Gravando em: ' + filename)
        out = cv.VideoWriter(filename, fourcc, 12.0, (1280, 720))
        # timeout = time.time() + 60 * 10
        timeout = time.time() + 60  # 1 minuto
        while True:
            if time.time() > timeout:
                print('Finished record 10m. Exiting ...')
                break
            # Capture frame-by-frame
            ret, frame = cap.read()
            # if frame is read correctly ret is True
            if not ret:
                print("Can't receive frame (stream end?). Exiting ...")
                break
            # Our operations on the frame come here
            # gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
            # Display the resulting frame
            # cv.imshow('frame', gray)
            out.write(frame)
            # When everything done, release the capture
        print('Releasing out ...')
        out.release()
        print('Compressing ...')
        print('ffmpeg -i ./' + filename + ' -c:a copy -c:v h264 -b:v 150k ' + 'compressed_' + filename)
        os.system('ffmpeg -i ./' + filename + ' -c:a copy -c:v h264 -b:v 150k ' + 'compressed_' + filename + ' &')
        # subprocess.run(os.system('ffmpeg -i ./' + filename + ' -c:a copy -c:v h264 -b 25k ' + 'compressed_' + filename))
        # ffmpeg.input(filename).output('compressed' + filename, bitrate='25k').run()
        print('Releasing capture ...')
        cap.release()
    # cv.destroyAllWindows()
