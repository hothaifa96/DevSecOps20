from flask import Flask
import time
app= Flask('shwarma wrapp')
is_db_ready= False
is_s3_ready=False
app_count= 0

def check_init(counter):
    global is_db_ready,is_s3_ready,app_count
    app_count +=counter
    if app_count > 10:
        is_db_ready=True
        is_s3_ready=True


@app.get('/')
def home():
    return 'welcome to the shawarma wrapp app '

@app.get('/healthyz')
def healthyz():
    check_init(1)
    return "healthy", 200

#
# postgrs
# 

@app.get('/readyz')
def readyz():
    if is_db_ready and is_s3_ready:
        return "ready",200
    else:
        return "not ready",503
    

app.run(port=4433,host='0.0.0.0')