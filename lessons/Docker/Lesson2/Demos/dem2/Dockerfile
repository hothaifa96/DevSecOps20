FROM python:3.12.10-alpine

WORKDIR /first-flask

COPY . .

RUN pip3 install -r requirements.txt

EXPOSE 5000

CMD [ "python3","application.py" ]