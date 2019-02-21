FROM python:3-slim

USER root
WORKDIR /root

# install dependencies
RUN pip install --no-cache html-testRunner \
    && apt-get update \
    && apt-get install -y adb git \
    && apt-get install -y libglib2.0 libsm6 libxrender1 libxext-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# install from source
RUN git clone https://github.com/williamfzc/fitch.git \
    && cd fitch \
    && pip install --no-cache .

# init adb (adb always fails at the first time)
RUN adb devices || echo "init adb"

# start testing
WORKDIR /usr/src/app
CMD ["python", "entry.py"]
