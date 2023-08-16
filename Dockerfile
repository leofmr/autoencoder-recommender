FROM python:3.11.4-bullseye

RUN pip install --upgrade pip \
    && apt-get update \
    && apt-get install curl \ 
    && curl -sSL https://install.python-poetry.org | POETRY_VERSION=1.5.1 python3 -

ENV PATH="/root/.local/bin:${PATH}"

COPY pyproject.toml poetry.lock ./

RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi --no-root