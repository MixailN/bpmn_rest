FROM python:3.10

WORKDIR /app/bpmn_rest/

RUN pip install poetry tblib holdup
RUN poetry config virtualenvs.create false

COPY . .

RUN poetry install

ENTRYPOINT ["./entrypoint.sh"]

