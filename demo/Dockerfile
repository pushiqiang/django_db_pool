# django APP
# do not operate database in APP's docker
# for there would be several apps, sharing one database
#
FROM python:3.6

RUN curl -s http://ip-api.com | grep "China" > /dev/null && \
    curl -s http://mirrors.163.com/.help/sources.list.jessie > /etc/apt/sources.list || true

RUN apt-get update;\
    apt-get install -y vim gettext;\
    true

COPY example /opt/src
WORKDIR /opt/src

RUN curl -s http://ip-api.com | grep "China" > /dev/null && \
    pip install -r requirements.txt -i https://pypi.doubanio.com/simple --trusted-host pypi.doubanio.com || \
    pip install -r requirements.txt
