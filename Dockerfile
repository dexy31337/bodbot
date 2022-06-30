FROM python:3
ADD abrabot.py /
RUN pip install mailru-im-bot
CMD [ "python", "./abrabot.py" ]
