FROM python:3.11.7

COPY ./requirements.txt /root/
WORKDIR /root
RUN pip install -r requirements.txt