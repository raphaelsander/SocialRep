FROM python:3.9-slim

WORKDIR /usr/src/app

COPY . .
RUN pip install --no-cache-dir -r requirements.txt && \
    chmod 755 docker-entrypoint.sh

EXPOSE 8000
CMD [ "./docker-entrypoint.sh" ]
