#syntax=harbor.leops.local/library/docker/dockerfile:1

# ---- 运行环境 ----
FROM harbor.leops.local/common/runtime/python:3.11 AS running

ARG APP_ENV=test \
    APP=undefine \
    GIT_BRANCH= \
    GIT_COMMIT_ID=

ENV APP_ENV=$APP_ENV \
    APP=$APP \
    GIT_BRANCH=$GIT_BRANCH \
    GIT_COMMIT_ID=$GIT_COMMIT_ID \
    PATH=$PATH:/home/nonroot/.local/bin/

WORKDIR /app

#USER root
# 下载依赖
COPY requirements.txt .
RUN --mount=type=cache,id=pip,target=/home/nonroot/.cache,uid=999,gid=999 \
    pip install -r requirements.txt

#USER nonroot
# 拷贝代码
COPY --chown=nonroot:nonroot . .

CMD ["bash", "-c", "python manage.py flush --no-input && python manage.py migrate && gunicorn demo.wsgi:application --bind 0.0.0.0:${SERVER_PORT:-8080}"]