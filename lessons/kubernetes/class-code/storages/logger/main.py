from flask import Flask,jsonify
from flask_cors import CORS
import psutil
import datetime
import time

app =Flask('kabab')
CORS(app)

LOG_FILE="/data/system_usage.log"

def log_system_usage():
    cpu = psutil.cpu_percent(interval=1)
    memory= psutil.virtual_memory().percent
    disk= psutil.disk_usage('/').percent
    time = datetime.datetime.now()
    
    log=f"{time}| CPU:{cpu} | Memory:{memory} | Disk{disk}"

    with open(LOG_FILE,"a") as f:
        f.write(log)
    return{
        'cpu':cpu,
        'disk':disk,
        'memory':memory,
        'time':time
    }


@app.route('/healthz',methods=['GET'])
def status2():
    return "healthy"

@app.route('/readyz',methods=['GET'])
def status3():
    for _ in range(10):
        time.sleep(1)
        data = log_system_usage()
    return jsonify(data)

@app.route('/status',methods=['GET'])
def status1():
    data = log_system_usage()
    return jsonify(data)


app.run(host='0.0.0.0',port=8080)