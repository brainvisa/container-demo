FROM ubuntu:18.04

RUN apt-get update \
 && apt-get upgrade -y \
 && apt-get install -y python python-setuptools git \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

RUN git clone https://github.com/brainvisa/container-demo.git \
  && cd container-demo \
  && python setup.py install \
  && cd .. \
  && rm -Rf container-demo
