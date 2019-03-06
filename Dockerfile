FROM python:3.7.0-slim-stretch

RUN apt-get update && \
  apt-get install -y \
  unixodbc \
  unixodbc-dev \
  default-libmysqlclient-dev \
  python-dev \
  wget

WORKDIR /usr/local/earnup

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

ENV DATABASE_URI= \
  CONFIG_ENV= \
  AWS_REGION=us-west-2 \
  REDIS_HOST= \
  REDIS_PORT=6379 \
  JOB_NAME= \
  WEB_PORT=5000

EXPOSE $WEB_PORT

ENTRYPOINT ["sh", "-c", "/usr/local/earnup/entrypoint.sh", "${JOB_NAME}"]
