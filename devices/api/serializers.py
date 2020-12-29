from rest_framework.serializers import ModelSerializer

from devices.models import Device


class DeviceSerializer(ModelSerializer):
    class Meta:
        model = Device
        fields = '__all__'
