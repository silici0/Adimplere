FROM python:3.9.12-slim

RUN pip install fastapi uvicorn poetry wheel virtualenv

EXPOSE 8888

WORKDIR /usr/src/adimplete

ENV PORT 8888
ENV HOST "0.0.0.0"
COPY ./src/ /adimplete/src
COPY ./pyproject.toml /adimplete

WORKDIR /adimplete
RUN poetry config virtualenvs.create false \
  && poetry install

CMD uvicorn src.main:app --host 0.0.0.0 --port 8888
