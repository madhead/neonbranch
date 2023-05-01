FROM --platform=arm64 python:3.9

RUN apt update && apt install -y zip
RUN curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
