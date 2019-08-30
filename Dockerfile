FROM lework/python:3.7.3-alpine3.10

LABEL maintainer="lework <lework@yeah.net>"

	
copy . ${WORKSPACE}

RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r ${WORKSPACE}/requirements.txt \
    && cd ${WORKSPACE}; python manage.py collectstatic --noinput \
