FROM python:3.7-alpine

COPY bot/config.py /bot/
COPY bot/bot.py /bot/
COPY bot/gettweets.py /bot/
COPY bot/models_mongodb.py /bot/
COPY requirements.txt /tmp
RUN pip3 install -r /tmp/requirements.txt

WORKDIR /bot
CMD ["python3", "bot.py"]