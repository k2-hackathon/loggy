# --- local ---
FROM nginx:1.21.5 AS local

RUN apt-get update && \
    apt-get install -y apt-utils curl \
    locales && \
    echo "ja_JP.UTF-8 UTF-8" > /etc/locale.gen && \
    locale-gen ja_JP.UTF-8
ENV LC_ALL ja_JP.UTF-8
ADD ./nginx.conf /etc/nginx/conf.d

EXPOSE 80
