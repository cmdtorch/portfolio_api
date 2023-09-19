FROM python:3.10

WORKDIR /portfolio_api
COPY ./requirements.txt /portfolio_api/

RUN pip install -r requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY ./ /portfolio_api

RUN python manage.py collectstatic