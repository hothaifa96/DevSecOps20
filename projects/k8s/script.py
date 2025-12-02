import time
import requests
import os

api = os.environ.get('API_URL')

try:
    response = requests.get(api,timeout=5)
    time.sleep(2)
    print(response.json)
except Exception as e:
    print(f' error: {e}')