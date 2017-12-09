FROM debian:jessie

RUN apt-get update -y && apt-get install -y python-pip

RUN pip install pyyaml Pygments

COPY yamlfilter/ /yamlfilter/

WORKDIR /yamlfilter

RUN python setup.py develop