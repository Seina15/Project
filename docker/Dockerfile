FROM python:3.10-slim
RUN apt-get update && apt-get install -y --no-install-recommends \
    git curl ffmpeg libglib2.0-0 libsm6 libxext6 libxrender1 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir ultralytics==8.3.0 opencv-python numpy

COPY . /app
RUN mkdir -p /app/out
ENV PYTHONUNBUFFERED=1
CMD ["/bin/bash"]
