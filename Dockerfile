FROM python:3-slim

USER root
WORKDIR /usr/src/app

RUN pip install --no-cache fitch==0.2.1 \
    && pip install --no-cache html-testRunner \
    && apt-get update \
    && apt-get install -y adb \
    && apt-get install -y libglib2.0 \
    && apt-get install -y libsm6 libxrender1 libxext-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

CMD ["python", "entry.py"]