# My Portfolio App

This is the API for my portfolio site. It is developed using the <a href="https://github.com/cmdtorch/django_fastapi/">FastApi-Django</a> frameworks. The application supports information about:

- Personal
- Testimonials
- Technologies
- Experience/Education
- Projects
- Contacts

---

**Front-End Source Code**: https://github.com/ilgarabdullazade/nuxt3-my-portfolio

---

## Installation

#### Clone repository
```bash
$ git clone https://github.com/cmdtorch/portfolio_api
```
or download <a href="https://github.com/cmdtorch/portfolio_api/releases/latest" class="external-link" target="_blank">archive</a>
#### Install packages
```bash
$ pip install -r requirements.txt
```

## Until run

Migrations
```bash
python manage.py migrate
```

## Run

```bash
$ uvicorn portfolio.asgi:fastapp --port 8000 --reload
...
Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
...
```

## Docker

Clone project as described above.

### .env file
Clone file `.env-example` with name `.env` and set your data in it
```bash
$ cp .env-example .env
```

### Build image and run container
Run inside project directory for create image:

```bash
$ docker build -t portfolio-api .
```

then run container with your `.env` file:

```bash
$ docker run -dp 127.0.0.1:8000:80 --name portfolio-api --env-file .env portfolio-api
```

This binds port 80 of the container to TCP port 8000 on 127.0.0.1 of the host machine.

### Create django admin user

The docker exec command runs a new command in a running container.

```bash
$ docker exec -it portfolio-api sh
```

and run command for create admin:
```bash
$ python manage.py createsuperuser
```
`Ctrl+D` for return to main.