from flask import Flask, request, render_template_string
from flask_cors import CORS
from prometheus_client import Gauge, Histogram, Counter, generate_latest, CONTENT_TYPE_LATEST
import time
import random

# init metric
HTTP_REQUESTS = Counter('pizza_app_request_total',
                         'HTTP TOTAL',
                           ['method', 'endpoint', 'https_status'])
REQUEST_LATENCY = Histogram(
    'pizza_app_request_duration',
    'doc doc',
    ['endpoint']
)
ACTIVE_REQUEST=Gauge('pizza_app_currnet_request','doc doc')

app = Flask(__name__)
CORS(app)


@app.before_request
def before_request():
    # HTTP_REQUESTS.inc()
    request.start_time = time.time()
    ACTIVE_REQUEST.inc()
    print(dir(request))

@app.after_request
def after_request(response):
   
    latency = time.time() - request.start_time
    print (latency)
    REQUEST_LATENCY.labels(request.path).observe(latency)
    HTTP_REQUESTS.labels(request.method,request.path,response.status_code).inc()
    ACTIVE_REQUEST.dec()


    return response

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Pizza App</title>
</head>
<body>
    <h1>🍕 Pizza Order</h1>

    <form method="post">
        <label>Choose your pizza:</label><br><br>

        <select name="pizza">
            <option value="Margherita">Margherita</option>
            <option value="Pepperoni">Pepperoni</option>
            <option value="Veggie">Veggie</option>
        </select>

        <br><br>
        <button type="submit">Order</button>
    </form>

    {% if pizza %}
        <h2>You ordered: {{ pizza }} 🍕</h2>
    {% endif %}
</body>
</html>
"""


@app.route("/", methods=["GET", "POST"])
def order():
    pizza = None
    if request.method == "POST":
        pizza = request.form.get("pizza")
    return render_template_string(HTML, pizza=pizza)


@app.route("/slow-ping", methods=["GET"])
def slow_ping():
    time.sleep(random.randint(0,10))
    return "pong"

@app.route("/ping", methods=["GET"])
def ping():
    return "pong"

@app.route("/metrics")
def metrics():
    return generate_latest() , 200,{"Content-Type": CONTENT_TYPE_LATEST}


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5002)
