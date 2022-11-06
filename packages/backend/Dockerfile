# --- builder ---
FROM python:3.9-slim AS builder

WORKDIR /app

RUN pip install poetry

COPY pyproject.toml poetry.lock ./
RUN poetry export --without-hashes -o requirements.txt
RUN poetry export --without-hashes --dev -o requirements-dev.txt


# --- local ---
FROM python:3.9-slim  AS local

WORKDIR /app

RUN pip install uvicorn

COPY --from=builder /app/requirements-dev.txt requirements-dev.txt
RUN pip install -r requirements-dev.txt --no-cache-dir

COPY ./backend .
RUN chmod 744 /app/initialize.sh

CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8080"]

# --- prod ---
FROM python:3.9-slim  AS prod

WORKDIR /app

RUN pip install uvicorn

COPY --from=builder /app/requirements-dev.txt requirements-dev.txt
RUN pip install -r requirements-dev.txt --no-cache-dir

COPY ./backend .

CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8080"]

