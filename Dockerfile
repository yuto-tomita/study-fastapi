FROM python:3.9

RUN pip install --upgrade pip

WORKDIR /app

RUN pip install poetry

COPY ./app ./

RUN poetry config virtualenvs.in-project true
RUN if [ -f pyproject.toml ]; then poetry install; fi

ENTRYPOINT ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080", "--reload"]
