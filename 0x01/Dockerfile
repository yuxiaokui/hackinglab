FROM alpine:3.9
MAINTAINER xi4okv <xi4okui@gmail.com>
RUN echo "https://mirror.tuna.tsinghua.edu.cn/alpine/v3.9/main" > /etc/apk/repositories

RUN apk add --update \
    python \
    py-pip
  && pip install Flask \
  && rm -rf /var/cache/apk/*


FROM       demo/alpine-python:1.0
MAINTAINER demo <juest a demo>

WORKDIR /data
COPY main.py /data

EXPOSE 5000

CMD ["/env/bin/python", "/data/main.py"]
