FROM python:3.9.7-slim

RUN mkdir easyocr_main
WORKDIR /easyocr_main
ADD . /easyocr_main

RUN apt-get update -y
RUN apt-get install build-essential -y


RUN pip install -r requirements.txt

#CMD ["python3", "app.py"]
CMD [ "gunicorn", "app:app", "-b", "0.0.0.0:8989", "-k" ,"gevent", "--timeout", "5000", "--graceful-timeout", "4890" ]
