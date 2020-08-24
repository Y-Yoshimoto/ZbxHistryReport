FROM nginx/unit:1.14.0-python3.7
# https://github.com/nginx/unit/tree/master/pkg/docker
LABEL  maintainer "y.yoshimoto"

# Install pip
RUN apt-get -y update\
    && apt-get install -y python3-pip\
    && apt-get clean
RUN pip3 install requests python-dateutil

# アプリケーションを配置
RUN mkdir -p /www/snippet
# COPY contents/*.py /www/snippet/

## コンフィグファイル設置
COPY appconfig.json /docker-entrypoint.d/

