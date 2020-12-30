# emilcam-api
Projeto desenvolvido em Python com o framework Django Rest Framework, consistindo numa api que faz o gerenciamento de câmeras de videomonitoramento.

### Introdução

Estas instruções lhe permitirão obter uma cópia do projeto e executá-lo na sua máquina local para desenvolvimento e testes. Veja as notas de compilação para saber como compilar o projeto.

## Pré-requisitos

* python3.8
* python3.8-venv

## Instalação

Após o download deste projeto, dentro de sua pasta principal deve ser executado o comando `python3 -m venv myvenv`, para criar o ambiente de desenvolvimento.

Em seguida o ambiente de desenvolvimento deve ser acessado através do comando `. myvenv/bin/activate`

Para sair do ambiente de desenvolvimento execute o comando `deactivate`

<<<<<<< HEAD
As dependências do projeto devem ser instaladas através dos seguintes comandos, nessa ordem:
=======
As dependências do projeto devem ser instaladas através dos seguintes comandos nessa ordem:
>>>>>>> 3a45ac254c1e57eb0c22d2457b612a7f440777b7
* `pip install django`
* `pip install djangorestframework`
* `pip install django-cors-headers`
* `pip install opencv-python`

Após a instalação das dependências, basta executar os seguintes passos de configuração do projeto:

Executar os scripts de banco de dados predefinidos no banco padrão (sqlite)

`python manage.py migrate`

Deve ser criado um superusuário (password = 12345)

`python manage.py createsuperuser --email admin@example.com --username admin`

## Servidor de desenvolvimento

Execute `python manage.py runserver 0.0.0.0:8000`, no terminal de comando, para iniciar o servidor de desenvolvimento. Acesse o endereço web `http://localhost:8000/`.

Para parar a execução do servidor de desenvolvimento, pressione `Ctrl + C`, no terminal de comando.

## Ajuda

Para obter mais informações sobre o framework DjangoRestFramework, acesse [DjangoRestFrameWork Docs](https://www.django-rest-framework.org/).

## Licença

Este projeto está licenciado sob os termos da [GNU General Public License v3.0](http://licencas.softwarelivre.org/gpl-3.0.pt-br.html).

## Autor

* **Moacir Costa** - *Desenvolvedor inicial*

## Agradecimentos

* A Jesus Cristo, que me deu fé, coragem, inteligência e determinação para chegar até aqui
* Ao meu irmão, Claudio Costa, que me ensinou a desenvolver sistemas web nos seus momentos de folga
