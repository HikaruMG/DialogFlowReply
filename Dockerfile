FROM python:3.8-slim

WORKDIR /app

RUN apt-get update
RUN apt-get install 'ffmpeg'\
    'libsm6'\ 
    'libxext6'  -y
COPY . .

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

CMD gunicorn app:app --bind 0.0.0.0:${PORT:-5000}
