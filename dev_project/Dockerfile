FROM python:3.8
ENV PYTHONUNBUFFERED 1

RUN mkdir -p /app/static
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt

