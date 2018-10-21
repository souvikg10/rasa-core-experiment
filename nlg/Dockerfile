FROM rasa_core_latest

SHELL ["/bin/bash", "-c"]

WORKDIR /app

ADD . .

EXPOSE 5006

CMD python nlg_server.py --port 5006 --domain data/servicing-bot-en/domain.yml