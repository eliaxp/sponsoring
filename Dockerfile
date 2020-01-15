# pull image
FROM python:3.7.4-alpine

# set directory
WORKDIR /web
COPY . /web/

# set environment
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# install psycopg2
RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add postgresql \
    && apk add postgresql-dev \
    && pip install psycopg2 \
    && apk add jpeg-dev zlib-dev libjpeg \
    && pip install Pillow==6.1.0 \
    && apk del build-deps

# install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ENTRYPOINT [ "/web/entrypoint.sh" ]