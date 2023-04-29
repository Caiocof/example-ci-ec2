FROM python:3.9

WORKDIR /api

COPY . .

RUN ["pip", "install", "-r", "requirements.txt"]

CMD [ "uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000" ]
