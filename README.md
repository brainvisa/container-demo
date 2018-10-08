# container-demo
Very simple python software used to illustrate Singularity or Docker usage.


## Download project sources
```sh
git clone https://github.com/brainvisa/container-demo.git /tmp/container-demo
```


## Install project without container

First download project sources

```sh
sudo apt-get install python virtualenv git
virtualenv /tmp/venv
cd /tmp/container-demo
/tmp/venv/bin/python setup.py install

# Command usage:
/tmp/venv/bin/cdemo_threshold /tmp/somewhere/image.nii.gz 150 /tmp/elsewhere/result_image.nii.gz
```

## Use command from DockerHub
docker run --rm -v /tmp/somewhere:/tmp/somewhere -v /tmp/elsewhere:/tmp/elsewhere brainvisa/container-demo cdemo_threshold /tmp/somewhere/image.nii.gz 150 /tmp/elsewhere/result_image.nii.gz

## Create a Docker image

First download project sources

```sh
sudo apt install docker.io
sudo addgroup $USER docker
docker build -t brainvisa/container-demo /tmp/container-demo/docker
```
