FROM python:3.10.5-alpine

WORKDIR /usr/src/app/rutabaga

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

ENV PYTHONUNBUFFERED=1

COPY . .

CMD [ "python", "main.py" ]