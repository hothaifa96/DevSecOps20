FROM python

WORKDIR /wrapp

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY main.py .

EXPOSE 4433

CMD [ "python3","main.py" ]