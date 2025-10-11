FROM python:3.12-alpine

WORKDIR /app

COPY main.py requirements.txt ./

RUN pip install -r requirements.txt

EXPOSE 5010

CMD [ "python","main.py" ]