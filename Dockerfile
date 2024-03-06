FROM python:3.11.0-slim-bullseye

ENV PIP_DISABLE_PIP_VERSION CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /apps

COPY ./requirements.txt .

RUN pip install -r requirements.txt

EXPOSE 9000

COPY . .
CMD ["python", "run.py"]