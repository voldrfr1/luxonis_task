FROM python:3

RUN pip install psycopg2
RUN pip install scrapy

COPY . /
CMD ["scrapy", "crawl", "sreality"]