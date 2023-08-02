FROM python:3.10

WORKDIR /portfolio_app
COPY ./requirements.txt /portfolio_app/

RUN pip install -r requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY ./ /portfolio_app