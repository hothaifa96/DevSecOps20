FROM python

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY main.py main.py

EXPOSE 8080

CMD [ "python3","main.py" ]
