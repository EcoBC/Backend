FROM ubuntu


RUN apt-get update
RUN apt-get install -y python python3-pip
COPY requirements.txt requirements.txt
ENV TZ=Asia/Dubai
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN pip install setuptools
# OPENCV linux dependency
RUN apt-get install ffmpeg libsm6 libxext6  -y
RUN apt-get update
RUN pip install -r requirements.txt

ENV DEBUG=True

COPY / /

ENTRYPOINT python3 manage.py runserver 0.0.0.0:80