FROM python:3

WORKDIR /www/app

EXPOSE 8000

RUN apt-get update && pip3 install flask gunicorn requests && rm -rf /var/lib/apt/lists/*

COPY . .

CMD ["gunicorn", "-w", "4", "--bind", "0.0.0.0:5732", "application:app" ]