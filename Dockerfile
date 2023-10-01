FROM python:3.10

ENV PYTHONUNBUFFERED 1

WORKDIR /portfolio_api
COPY ./requirements.txt /portfolio_api/

RUN pip install -r requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY ./ /portfolio_api

CMD python manage.py migrate \
    && python manage.py collectstatic --noinput \
    && uvicorn portfolio.asgi:fastapp --host 0.0.0.0 --port 80 --reload