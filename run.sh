#!/bin/bash

sudo docker build -t biodata .
sudo docker run -it -p 8082:8000 biodata