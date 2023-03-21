FROM alpine:3.14

WORKDIR /usr/src/app

EXPOSE 5000

RUN apk add --no-cache wget unzip

RUN wget "https://github.com/grimalschi/calque/archive/refs/heads/master.zip"

RUN unzip ./master.zip

WORKDIR /usr/src/app/calque-master/

RUN apk add --update python3 && ln -sf python3 /usr/bin/python

RUN python3 -m ensurepip

RUN pip3 install --upgrade pip setuptools

CMD ["python3", "-m", "http.server", "5000"]
