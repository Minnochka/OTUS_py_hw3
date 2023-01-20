#docker run -it -p 8000:8000 hw3
FROM python:3.10-buster
ENV PYTHONUNBUFFERED=1

WORKDIR /var

RUN pip install --upgrade pip && \
    pip install poetry

RUN poetry config virtualenvs.create false --local

COPY poetry.lock pyproject.toml ./

RUN poetry install --only main

COPY . .

CMD uvicorn main:app --host 0.0.0.0 --port 8000
EXPOSE 8000