FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE 1 \
    PYTHONFAULTHANDLER 1 \
    PYTHONBUFFERED 1

RUN pip install --upgrade pip uv
RUN python -m pip install pytest-runner setuptools-scm==6.*

WORKDIR app
COPY pyproject.toml ./pyproject.toml
RUN uv pip compile pyproject.toml > requirements.txt
RUN uv pip sync requirements.txt --system

