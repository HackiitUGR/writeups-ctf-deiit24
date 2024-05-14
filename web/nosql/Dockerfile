FROM mongo

RUN apt-get update && \
    apt-get install -y python3.9 python3-pip && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .

RUN pip3 install --no-cache-dir -r requirements.txt

COPY app /app

COPY init.sh /

EXPOSE 6002

ENTRYPOINT ["sh", "/init.sh"]
