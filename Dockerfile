FROM python:3.12.2 as base

COPY requirements.txt /tmp/requirements.txt

RUN pip install --upgrade pip && \
    pip install -r /tmp/requirements.txt

RUN mkdir /code
COPY code /code

WORKDIR /code
# ENTRYPOINT ["sh", "-c", "while :; do sleep 1; done"]
ENTRYPOINT [ "python", "-m", "llm_agent.app" ]
