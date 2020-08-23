FROM python:3.7.8

WORKDIR /usr/src/app

COPY req.txt ./
RUN pip install --no-cache-dir -r req.txt

COPY . .

CMD [ "./bin/entrypoint" ]
