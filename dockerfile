FROM python:3.8.0

RUN apt-get update \
    && apt-get --assume-yes --no-install-recommends install \
        build-essential \
        curl \
        git \
        jq \
        libgomp1 \
        vim

WORKDIR /app

# upgrade pip version
RUN pip install --no-cache-dir --upgrade pip

RUN pip install rasa==3.6.20
RUN pip install flask

COPY ./actions /app/actions
COPY ./data /app/data
COPY ./models /app/models
COPY ./static /app/static
COPY ./templates /app/templates
COPY ./tests /app/tests
COPY ./utils /app/utils
COPY ./ai_model /app/ai_model
COPY ./app.py /app/app.py
COPY ./config.yml /app/config.yml
COPY ./credentials.yml /app/credentials.yml
COPY ./docker-compose.yml /app/docker-compose.yml
COPY ./dockerfile /app/dockerfile
COPY ./domain.yml /app/domain.yml
COPY ./endpoints.yml /app/endpoints.yml
COPY ./socketio.py /usr/local/lib/python3.8/site-packages/rasa/core/channels/socketio.py