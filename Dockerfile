# Use an official Python runtime as a parent image
FROM python:3.6

MAINTAINER YitJian Wong "yitjian.wyj@gmail.com"

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app

# Update the package index
RUN apt-get update

RUN apt-get install -y python-pip python-dev build-essential

RUN pip install -r requirements.txt

EXPOSE 5000

ENV FLASK_ENV development 

CMD ["python", "proxyserver.py"]