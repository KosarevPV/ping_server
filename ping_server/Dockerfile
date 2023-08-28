from python:3.11.5 

WORKDIR /home/kosarev/ping_server/ping_server

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


RUN apt-get update
RUN apt-get install -y postgresql postgresql-contrib libpq-dev python3-dev iputils-ping

RUN pip3 install --upgrade pip

COPY ./requirements.txt .

RUN mkdir -p /home/app
ENV HOME=/home/app
ENV APP_HOME=/home/app/web
RUN mkdir $APP_HOME
RUN mkdir $APP_HOME/staticfiles

RUN pip3 install -r requirements.txt
RUN pip3 install gunicorn

COPY . .


COPY wait-for-postgres.sh .
RUN chmod +x wait-for-postgres.sh
