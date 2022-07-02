FROM python:3.10-slim

WORKDIR /app

ADD requirements.txt ./

RUN apt-get update && apt-get -y install ffmpeg && apt-get -y clean

RUN pip install -r requirements.txt && pip install gunicorn

ADD *.py ./
ADD static ./static
ADD templates ./templates

EXPOSE 80

CMD gunicorn --bind 0.0.0.0:80 --timeout=1800 --workers=4 --threads=4 --max-requests=30 --max-requests-jitter=20 --name=gunicorn  main:app