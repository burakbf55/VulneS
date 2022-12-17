FROM python:3.9-alpine3.13

WORKDIR /code
COPY requirements.txt /code/

# Install dependencies
RUN apk add --update --no-cache \
    ca-certificates \
    libpcap \
    libgcc libstdc++ \
    libressl3.1-libcrypto libressl3.1-libssl \
    && update-ca-certificates \
    && rm -rf /var/cache/apk/*


# Compile and install Nmap from sources
RUN apk add --update --no-cache --virtual .build-deps \
    libpcap-dev libressl-dev lua-dev linux-headers \
    autoconf g++ libtool make \
    curl \
    && curl -fL -o /tmp/nmap.tar.bz2 \
    https://nmap.org/dist/nmap-7.70.tar.bz2 \
    && tar -xjf /tmp/nmap.tar.bz2 -C /tmp \
    && cd /tmp/nmap* \
    && ./configure \
    --prefix=/usr \
    --sysconfdir=/etc \
    --mandir=/usr/share/man \
    --infodir=/usr/share/info \
    --without-zenmap \
    --without-nmap-update \
    --with-openssl=/usr/lib \
    --with-liblua=/usr/include \
    && make \
    && make install \
    && apk del .build-deps \
    && rm -rf /var/cache/apk/* \
    /tmp/nmap*


ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN pip install -r requirements.txt
COPY . /code/
