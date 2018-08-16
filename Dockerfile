FROM ubuntu:bionic

RUN echo ttf-mscorefonts-installer msttcorefonts/accepted-mscorefonts-eula select true | debconf-set-selections

RUN apt-get update -qq && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
        python3 python3-pip python3-setuptools \
        curl libfontconfig xvfb libpq-dev ttf-mscorefonts-installer fonts-takao-pgothic && \
    curl -fLsSo /tmp/wkhtmltox.deb https://downloads.wkhtmltopdf.org/0.12/0.12.5/wkhtmltox_0.12.5-1.bionic_amd64.deb && \
    echo "db48fa1a043309c4bfe8c8e0e38dc06c183f821599dd88d4e3cea47c5a5d4cd3 /tmp/wkhtmltox.deb" | sha256sum -c && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends /tmp/wkhtmltox.deb && \
    pip3 install -U pip

COPY binaries/cpdf/cpdf /usr/local/bin/
RUN chmod +x /usr/local/bin/cpdf

COPY trans/static/fonts/IRANSans/ttf/* /usr/local/share/fonts/
COPY trans/static/fonts/SourceSansPro/ttf/* /usr/local/share/fonts/
COPY trans/static/fonts/Korean/* /usr/local/share/fonts/
COPY trans/static/fonts/Thai/* /usr/local/share/fonts/
COPY trans/static/fonts/Taiwan/* /usr/local/share/fonts/

COPY requirements.txt /root/requirements.txt
RUN pip3 install -r /root/requirements.txt

COPY docker-entrypoint.sh /root/docker-entrypoint.sh
RUN chmod +x /root/docker-entrypoint.sh

COPY . /usr/src/app
WORKDIR /usr/src/app

ENTRYPOINT ["/root/docker-entrypoint.sh"]
