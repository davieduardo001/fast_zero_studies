FROM python:3.12-slim

COPY . /app
WORKDIR /app

RUN pip install --no-cache-dir pipx
RUN pipx install poetry --force

ENV PATH=/root/.local/bin:$PATH

RUN poetry install --no-interaction

ENV PYTHONPATH=/app

EXPOSE 8000

CMD ["poetry", "run", "task", "run"]
