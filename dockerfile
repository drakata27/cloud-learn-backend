FROM python:3.10-bullseye

ENV PYTHONBUFFERED=1

WORKDIR /django

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

CMD gunicorn cloudlearnbackend.wsgi:application --bind 0.0.0.0:8000

EXPOSE 8000












