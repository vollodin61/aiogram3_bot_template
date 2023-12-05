FROM python:3.11.5-alpine3.18

WORKDIR /sarafanka

COPY . .

RUN pip install -r requirements.txt

CMD ["python", "bot/main.py"]
