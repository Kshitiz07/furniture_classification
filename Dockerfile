## getting python image
FROM python:3.10.10-buster
# Install additional packages
# RUN apk add --no-cache build-base
## setting working directory
WORKDIR /usr/src/app

## copying requirements.txt to working directory
## copying all files to working directory
COPY . .

## Upgrade pip
RUN pip install --upgrade pip

RUN pip install --upgrade pip setuptools wheel

## installing requirements
RUN pip install -r requirements.txt


