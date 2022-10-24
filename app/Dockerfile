FROM python:3

ADD main.py /

RUN pip install psycopg2
RUN pip install flask
COPY . /
CMD [ "python", "./main.py" ]