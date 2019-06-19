FROM python:3
ADD . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 8080
CMD python ./manage.py runserver 0.0.0.0:8080
