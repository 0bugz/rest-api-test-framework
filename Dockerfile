FROM ubuntu

MAINTAINER ujnamss "ujnamss@gmail.com"

RUN  apt-get update -y && \
     apt-get upgrade -y && \
     apt-get dist-upgrade -y && \
     apt-get -y autoremove && \
     apt-get clean

RUN apt-get install -y git wget zip unzip python3-pip python3-dev

# update pip
RUN python3 -m pip install pip --upgrade

ADD install/requirements.txt /app/requirements.txt

RUN python3 -m pip install -Ur /app/requirements.txt

ENV HOME_DIR /homedir

WORKDIR $HOME_DIR/rest-api-test-framework/src

CMD python3 main.py
