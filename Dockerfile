FROM python:3-slim

USER root
WORKDIR /root

# install dependencies
RUN apt-get update \
    && apt-get install -y git wget zip android-tools-adb \
    && apt-get install -y libglib2.0 libsm6 libxrender1 libxext-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY . .

# init adb (adb always fails at the first time)
RUN adb start-server || echo "init adb" \
    && pip install .

# start testing
WORKDIR /usr/src/app
CMD ["bash"]
