# Dockerfile, Image, Container
FROM python:3.6.9

WORKDIR /code

COPY . .

#ADD TLEVisualizer.py .

RUN pip install sgp4 matplotlib numpy

CMD [ "python", "./TLEVisualizer.py" ]