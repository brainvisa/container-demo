FROM ubuntu:18.04

RUN apt-get update \
 && apt-get upgrade -y \
 && apt-get install -y python3 python3-setuptools git \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

RUN git clone https://github.com/brainvisa/container-demo.git \
  && cd container-demo \
  && python3 setup.py install \
  && cd .. \
  && rm -Rf container-demo
