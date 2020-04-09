FROM alpine:3.9
MAINTAINER xi4okv <xi4okui@gmail.com>
RUN echo "https://mirror.tuna.tsinghua.edu.cn/alpine/v3.9/main" > /etc/apk/repositories

RUN apk add --update \
    python \
    py-pip \
  && pip install Flask \
  && pip install requests \
  && rm -rf /var/cache/apk/*

WORKDIR /data
COPY main.py /data

EXPOSE 5000

CMD ["python", "/data/main.py"]
