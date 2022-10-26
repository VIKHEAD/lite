FROM python:3

ENV PYTHONUNBUFFERED 1

RUN mkdir -p /usr/src/app/
WORKDIR /usr/src/app/

COPY requirements.txt /usr/src/app/
RUN pip3 install --upgrade pip
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . /usr/src/app/

CMD gunicorn --bind 0.0.0.0:8668 -w 3 run:app
