FROM python:3.10-bullseye

RUN pip install --upgrade pip
RUN pip install blink1 flask flask-cors

COPY ./src/ /opt/src

WORKDIR /opt/src

ENTRYPOINT ["python3","app.py"]
CMD [""]
