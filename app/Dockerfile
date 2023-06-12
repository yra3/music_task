# syntax=docker/dockerfile:1
FROM python:3.10
ENV PYTHONUNBUFFERED 1
WORKDIR /app
RUN apt-get update && apt-get install -y software-properties-common
RUN apt-get -y upgrade
RUN apt-get install -y ffmpeg
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
