FROM python:3.9

WORKDIR /app

ADD requirements.txt .

RUN pip install -r requirements.txt

ADD . .

EXPOSE 80

ENTRYPOINT ["bash", "docker_entrypoint.sh"]
