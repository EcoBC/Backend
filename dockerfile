FROM ubuntu

RUN apt-get update
RUN apt-get install -y python python3-pip
COPY requirements.txt requirements.txt
RUN pip install -U setuptools
RUN pip install -r requirements.txt
ENV DEBUG=True

COPY / /

ENTRYPOINT python3 manage.py runserver 0.0.0.0:80