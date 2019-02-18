FROM python:3-slim

USER root
WORKDIR /usr/src/app

RUN pip install --no-cache fitch \
    && apt-get update \
    && apt-get install -y adb \
    && apt-get install -y libglib2.0 \
    && rm -rf /var/lib/apt/lists/*

CMD ["python", "-m", "unittest"]
