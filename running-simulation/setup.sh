#!/bin/bash

sudo apt-get update
sudo apt-get -y install python3-pip
sudo apt-get install python3-venv
sudo apt-get install bc

python3 -m venv merlin

wget  http://download.redis.io/releases/redis-5.0.7.tar.gz
tar xvf redis-5.0.7.tar.gz
cd redis-5.0.7
make

cd ..
source merlin/bin/activate
pip3 install merlinwf
merlin config

cp app.yaml ~/.merlin/app.yaml
