FROM alpine:latest

WORKDIR /usr/src/app

RUN apk update

RUN apk add --no-cache python3 \
	 py3-pip \
	 curl \
	 git \
	 openssh

RUN pip install docker \
	 halo

RUN mkdir /root/.ssh/ && touch /root/.ssh/config

ADD github /root/.ssh/github
ADD github.pub /root/.ssh/github.pub
ADD config /root/.ssh/config

ADD dockerize.py /usr/src/app/dockerize.py

RUN chmod 600 /root/.ssh/github
RUN chmod 600 /root/.ssh/config

RUN ssh-keyscan github.com >> /root/.ssh/known_hosts

ENTRYPOINT ["python3", "dockerize.py"]
