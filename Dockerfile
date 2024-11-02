FROM ubuntu:22.04


WORKDIR /opt/

EXPOSE 5000



RUN apt-get update

RUN apt-get install -yq ffmpeg

RUN apt-get install -yq python3 python3-dev python3-pip


RUN pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu


COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt


RUN apt-get install -yq build-essential cmake && \

   apt-get install -yq libopenblas-dev liblapack-dev && \

   pip install dlib


COPY ./backend backend

COPY ./output_template output_template

COPY ./static static

COPY ./templates templates

COPY app.py ./

RUN mkdir video

RUN mkdir output



CMD ["python3", "-m", "flask", "--app", "app", "run", "--host=0.0.0.0"]