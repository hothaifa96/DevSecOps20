FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY auth.py .

ENV USERS_API_URL=http://localhost:5001
ENV PORT=5002

EXPOSE 5002

CMD [ "python3","auth.py" ]