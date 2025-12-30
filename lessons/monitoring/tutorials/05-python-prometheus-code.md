# Python Prometheus Client - Complete Guide

## Table of Contents

1. [Introduction](#introduction)
2. [Installation](#installation)
3. [Metric Types](#metric-types)
4. [Basic Usage](#basic-usage)
5. [Flask Integration](#flask-integration)
6. [FastAPI Integration](#fastapi-integration)
7. [Django Integration](#django-integration)
8. [Advanced Patterns](#advanced-patterns)
9. [Best Practices](#best-practices)

---

## Introduction

The `prometheus_client` library is the official Python client for Prometheus. It allows you to:

- Instrument your Python applications
- Expose metrics via HTTP endpoint
- Push metrics to Pushgateway
- Create custom collectors

---

## Installation

```bash
# Install prometheus-client
pip install prometheus-client

# For Flask integration
pip install prometheus-client flask

# For FastAPI integration
pip install prometheus-client fastapi uvicorn

# For Django integration
pip install django-prometheus
```

---

## Metric Types

### 1. Counter

A counter is a cumulative metric that only increases or resets to zero on restart.

```python
from prometheus_client import Counter

# Define counter
http_requests_total = Counter(
    'http_requests_total',
    'Total HTTP requests',
    ['method', 'endpoint', 'status']
)

# Increment counter
http_requests_total.labels(method='GET', endpoint='/api/users', status='200').inc()

# Increment by specific value
http_requests_total.labels(method='POST', endpoint='/api/orders', status='201').inc(5)
```

### 2. Gauge

A gauge is a metric that can go up and down.

```python
from prometheus_client import Gauge

# Define gauge
temperature = Gauge(
    'room_temperature_celsius',
    'Current room temperature',
    ['room']
)

# Set value
temperature.labels(room='server_room').set(22.5)

# Increment/decrement
temperature.labels(room='server_room').inc()
temperature.labels(room='server_room').dec(0.5)

# Track in-progress operations
in_progress = Gauge('requests_in_progress', 'Requests currently being processed')

@in_progress.track_inprogress()
def process_request():
    # Your code here
    pass
```

### 3. Summary

A summary samples observations and provides count, sum, and configurable quantiles.

```python
from prometheus_client import Summary

# Define summary
request_latency = Summary(
    'request_latency_seconds',
    'Request latency in seconds',
    ['endpoint']
)

# Observe a value
request_latency.labels(endpoint='/api/users').observe(0.5)

# Use as decorator
@request_latency.labels(endpoint='/api/process').time()
def process_data():
    # Your code here
    pass
```

### 4. Histogram

A histogram samples observations and counts them in configurable buckets.

```python
from prometheus_client import Histogram

# Define histogram with custom buckets
request_duration = Histogram(
    'http_request_duration_seconds',
    'HTTP request duration in seconds',
    ['method', 'endpoint'],
    buckets=[0.01, 0.025, 0.05, 0.1, 0.25, 0.5, 1.0, 2.5, 5.0, 10.0]
)

# Observe a value
request_duration.labels(method='GET', endpoint='/api/users').observe(0.25)

# Use as context manager
with request_duration.labels(method='POST', endpoint='/api/orders').time():
    # Your code here
    pass

# Use as decorator
@request_duration.labels(method='GET', endpoint='/api/products').time()
def get_products():
    pass
```

### 5. Info

Info is used for static information about the application.

```python
from prometheus_client import Info

# Define info metric
app_info = Info('app', 'Application information')

# Set info
app_info.info({
    'version': '1.2.3',
    'environment': 'production',
    'python_version': '3.11'
})
```

### 6. Enum

Enum tracks which of a set of states something is in.

```python
from prometheus_client import Enum

# Define enum metric
app_state = Enum(
    'app_state',
    'Current application state',
    states=['starting', 'running', 'stopping', 'stopped']
)

# Set state
app_state.state('running')
```

---

## Basic Usage

### Simple HTTP Server

```python
from prometheus_client import start_http_server, Counter, Gauge, Histogram
import time
import random

# Define metrics
REQUEST_COUNT = Counter(
    'myapp_requests_total',
    'Total application requests',
    ['method', 'endpoint']
)

REQUEST_LATENCY = Histogram(
    'myapp_request_duration_seconds',
    'Request duration in seconds',
    ['endpoint'],
    buckets=[0.1, 0.25, 0.5, 1.0, 2.5, 5.0]
)

ACTIVE_CONNECTIONS = Gauge(
    'myapp_active_connections',
    'Number of active connections'
)

def process_request(endpoint):
    """Simulate processing a request"""
    start_time = time.time()

    # Simulate work
    time.sleep(random.uniform(0.1, 0.5))

    # Record metrics
    REQUEST_COUNT.labels(method='GET', endpoint=endpoint).inc()
    REQUEST_LATENCY.labels(endpoint=endpoint).observe(time.time() - start_time)

if __name__ == '__main__':
    # Start metrics server on port 8000
    start_http_server(8000)
    print("Metrics available at http://localhost:8000/metrics")

    # Simulate application running
    while True:
        ACTIVE_CONNECTIONS.set(random.randint(10, 100))
        process_request('/api/users')
        process_request('/api/orders')
        time.sleep(5)
```

### Push to Pushgateway

```python
from prometheus_client import CollectorRegistry, Gauge, push_to_gateway

# Create a registry for this job
registry = CollectorRegistry()

# Define metrics with the registry
duration = Gauge(
    'batch_job_duration_seconds',
    'Duration of batch job',
    registry=registry
)

records_processed = Gauge(
    'batch_job_records_processed',
    'Number of records processed',
    registry=registry
)

def run_batch_job():
    import time
    start = time.time()

    # Simulate batch processing
    processed = 1000
    time.sleep(2)

    # Set metrics
    duration.set(time.time() - start)
    records_processed.set(processed)

    # Push to gateway
    push_to_gateway(
        'localhost:9091',
        job='batch_job',
        registry=registry
    )
    print("Metrics pushed to Pushgateway")

if __name__ == '__main__':
    run_batch_job()
```

---

## Flask Integration

### Basic Flask App with Prometheus

```python
from flask import Flask, request, Response
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST
import time

app = Flask(__name__)

# Define metrics
REQUEST_COUNT = Counter(
    'flask_http_requests_total',
    'Total HTTP requests',
    ['method', 'endpoint', 'status']
)

REQUEST_LATENCY = Histogram(
    'flask_http_request_duration_seconds',
    'HTTP request duration',
    ['method', 'endpoint']
)

@app.before_request
def before_request():
    request.start_time = time.time()

@app.after_request
def after_request(response):
    latency = time.time() - request.start_time
    REQUEST_COUNT.labels(
        method=request.method,
        endpoint=request.path,
        status=response.status_code
    ).inc()
    REQUEST_LATENCY.labels(
        method=request.method,
        endpoint=request.path
    ).observe(latency)
    return response

@app.route('/metrics')
def metrics():
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/api/users')
def get_users():
    time.sleep(0.1)  # Simulate work
    return {'users': ['alice', 'bob']}

@app.route('/api/orders', methods=['POST'])
def create_order():
    time.sleep(0.2)  # Simulate work
    return {'order_id': 12345}, 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

### Using prometheus-flask-exporter

```python
from flask import Flask
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app)

# Static info
metrics.info('app_info', 'Application info', version='1.0.0')

# Custom metrics
@app.route('/api/users')
@metrics.counter('users_requests', 'Number of user requests')
def get_users():
    return {'users': ['alice', 'bob']}

@app.route('/api/orders')
@metrics.histogram('orders_latency', 'Order request latency',
                   labels={'endpoint': '/api/orders'})
def get_orders():
    return {'orders': []}

# Exclude endpoint from metrics
@app.route('/health')
@metrics.do_not_track()
def health():
    return 'OK'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

---

## FastAPI Integration

### Basic FastAPI Integration

```python
from fastapi import FastAPI, Request
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST
from starlette.responses import Response
from starlette.middleware.base import BaseHTTPMiddleware
import time

app = FastAPI()

# Define metrics
REQUEST_COUNT = Counter(
    'fastapi_requests_total',
    'Total requests',
    ['method', 'endpoint', 'status']
)

REQUEST_LATENCY = Histogram(
    'fastapi_request_duration_seconds',
    'Request duration',
    ['method', 'endpoint']
)

class MetricsMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        start_time = time.time()
        response = await call_next(request)
        duration = time.time() - start_time

        REQUEST_COUNT.labels(
            method=request.method,
            endpoint=request.url.path,
            status=response.status_code
        ).inc()

        REQUEST_LATENCY.labels(
            method=request.method,
            endpoint=request.url.path
        ).observe(duration)

        return response

app.add_middleware(MetricsMiddleware)

@app.get('/metrics')
def metrics():
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)

@app.get('/')
def home():
    return {'message': 'Hello, World!'}

@app.get('/api/users')
async def get_users():
    return {'users': ['alice', 'bob']}

@app.post('/api/orders')
async def create_order():
    return {'order_id': 12345}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000)
```

### Using prometheus-fastapi-instrumentator

```python
from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI()

# Initialize and instrument
Instrumentator().instrument(app).expose(app)

@app.get('/')
def home():
    return {'message': 'Hello, World!'}

@app.get('/api/users')
async def get_users():
    return {'users': ['alice', 'bob']}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000)
```

---

## Django Integration

### Using django-prometheus

```python
# settings.py
INSTALLED_APPS = [
    ...
    'django_prometheus',
]

MIDDLEWARE = [
    'django_prometheus.middleware.PrometheusBeforeMiddleware',
    ...
    'django_prometheus.middleware.PrometheusAfterMiddleware',
]

# Database monitoring (optional)
DATABASES = {
    'default': {
        'ENGINE': 'django_prometheus.db.backends.postgresql',
        ...
    }
}

# Cache monitoring (optional)
CACHES = {
    'default': {
        'BACKEND': 'django_prometheus.cache.backends.redis.RedisCache',
        ...
    }
}
```

```python
# urls.py
urlpatterns = [
    ...
    path('', include('django_prometheus.urls')),
]
```

### Custom Django Metrics

```python
# metrics.py
from prometheus_client import Counter, Histogram

user_signups = Counter(
    'django_user_signups_total',
    'Total user signups',
    ['source']
)

order_value = Histogram(
    'django_order_value_dollars',
    'Order value in dollars',
    buckets=[10, 25, 50, 100, 250, 500, 1000]
)

# views.py
from .metrics import user_signups, order_value

def signup_view(request):
    # Process signup
    user_signups.labels(source=request.GET.get('source', 'direct')).inc()
    return JsonResponse({'status': 'success'})

def create_order_view(request):
    amount = request.POST.get('amount', 0)
    order_value.observe(float(amount))
    return JsonResponse({'order_id': 123})
```

---

## Advanced Patterns

### Custom Collector

```python
from prometheus_client.core import GaugeMetricFamily, CounterMetricFamily, REGISTRY

class DatabaseCollector:
    def __init__(self, db_connection):
        self.db = db_connection

    def collect(self):
        # Query database for metrics
        connection_count = self.db.get_connection_count()
        query_count = self.db.get_total_queries()

        # Create gauge metric
        gauge = GaugeMetricFamily(
            'db_connections_active',
            'Number of active database connections'
        )
        gauge.add_metric([], connection_count)
        yield gauge

        # Create counter metric
        counter = CounterMetricFamily(
            'db_queries_total',
            'Total database queries executed'
        )
        counter.add_metric([], query_count)
        yield counter

# Register collector
REGISTRY.register(DatabaseCollector(db_connection))
```

### Multiprocess Mode (Gunicorn)

```python
# prometheus_multiproc.py
from prometheus_client import multiprocess, CollectorRegistry, generate_latest, CONTENT_TYPE_LATEST

def metrics_app(environ, start_response):
    registry = CollectorRegistry()
    multiprocess.MultiProcessCollector(registry)

    data = generate_latest(registry)
    status = '200 OK'
    response_headers = [
        ('Content-type', CONTENT_TYPE_LATEST),
        ('Content-Length', str(len(data)))
    ]
    start_response(status, response_headers)
    return [data]
```

```python
# gunicorn.conf.py
import os

# Required for multiprocess mode
prometheus_multiproc_dir = '/tmp/prometheus_multiproc'

def child_exit(server, worker):
    from prometheus_client import multiprocess
    multiprocess.mark_process_dead(worker.pid)
```

```bash
# Run with gunicorn
export PROMETHEUS_MULTIPROC_DIR=/tmp/prometheus_multiproc
mkdir -p $PROMETHEUS_MULTIPROC_DIR
gunicorn -c gunicorn.conf.py -w 4 myapp:app
```

### Async Context Manager

```python
import asyncio
from prometheus_client import Histogram

request_duration = Histogram(
    'async_request_duration_seconds',
    'Async request duration'
)

class AsyncTimer:
    def __init__(self, histogram):
        self.histogram = histogram

    async def __aenter__(self):
        self.start = asyncio.get_event_loop().time()
        return self

    async def __aexit__(self, *args):
        duration = asyncio.get_event_loop().time() - self.start
        self.histogram.observe(duration)

async def process_request():
    async with AsyncTimer(request_duration):
        await asyncio.sleep(0.5)  # Simulate async work
```

---

## Best Practices

### 1. Use Meaningful Names

```python
# Good
http_requests_total
http_request_duration_seconds
database_connections_active

# Bad
requests
latency
connections
```

### 2. Use Labels Wisely

```python
# Good - low cardinality labels
REQUEST_COUNT.labels(method='GET', status='200', endpoint='/api/users')

# Bad - high cardinality (user_id can have millions of values)
REQUEST_COUNT.labels(user_id='12345')
```

### 3. Pre-declare Label Values

```python
from prometheus_client import Counter

http_requests = Counter('http_requests_total', 'Total requests', ['status'])

# Initialize all expected label values
for status in ['200', '400', '404', '500']:
    http_requests.labels(status=status)
```

### 4. Use Appropriate Buckets

```python
# For API latency (milliseconds to seconds)
Histogram('api_latency', 'API latency',
          buckets=[0.01, 0.025, 0.05, 0.1, 0.25, 0.5, 1.0, 2.5, 5.0])

# For batch job duration (seconds to minutes)
Histogram('batch_duration', 'Batch duration',
          buckets=[1, 5, 10, 30, 60, 120, 300, 600])
```

### 5. Document Your Metrics

```python
Counter(
    'payment_transactions_total',
    'Total number of payment transactions processed. '
    'Use status label to filter by success/failure.',
    ['status', 'payment_method']
)
```

---

## Complete Example Application

```python
#!/usr/bin/env python3
"""
Complete Flask application with Prometheus metrics
"""
from flask import Flask, request, jsonify, Response
from prometheus_client import (
    Counter, Histogram, Gauge, Info,
    generate_latest, CONTENT_TYPE_LATEST
)
import time
import random

app = Flask(__name__)

# Application info
APP_INFO = Info('myapp', 'Application information')
APP_INFO.info({'version': '1.0.0', 'environment': 'production'})

# Request metrics
REQUEST_COUNT = Counter(
    'myapp_http_requests_total',
    'Total HTTP requests',
    ['method', 'endpoint', 'status']
)

REQUEST_LATENCY = Histogram(
    'myapp_http_request_duration_seconds',
    'HTTP request duration in seconds',
    ['method', 'endpoint'],
    buckets=[0.01, 0.05, 0.1, 0.25, 0.5, 1.0, 2.5, 5.0]
)

# Business metrics
ORDERS_CREATED = Counter(
    'myapp_orders_created_total',
    'Total orders created',
    ['product_type']
)

ORDER_VALUE = Histogram(
    'myapp_order_value_dollars',
    'Order value in dollars',
    buckets=[10, 25, 50, 100, 250, 500, 1000, 2500, 5000]
)

ACTIVE_USERS = Gauge(
    'myapp_active_users',
    'Number of active users'
)

@app.before_request
def before_request():
    request.start_time = time.time()

@app.after_request
def after_request(response):
    latency = time.time() - request.start_time
    REQUEST_COUNT.labels(
        method=request.method,
        endpoint=request.path,
        status=response.status_code
    ).inc()
    REQUEST_LATENCY.labels(
        method=request.method,
        endpoint=request.path
    ).observe(latency)
    return response

@app.route('/metrics')
def metrics():
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)

@app.route('/health')
def health():
    return jsonify({'status': 'healthy'})

@app.route('/api/users')
def get_users():
    ACTIVE_USERS.set(random.randint(100, 500))
    return jsonify({'users': ['alice', 'bob', 'charlie']})

@app.route('/api/orders', methods=['POST'])
def create_order():
    product_type = request.json.get('product_type', 'standard')
    amount = request.json.get('amount', 100)

    ORDERS_CREATED.labels(product_type=product_type).inc()
    ORDER_VALUE.observe(amount)

    return jsonify({'order_id': random.randint(1000, 9999)}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
```

---

## Resources

- [prometheus-client Documentation](https://prometheus.github.io/client_python/)
- [Prometheus Python Client GitHub](https://github.com/prometheus/client_python)
- [prometheus-flask-exporter](https://github.com/rycus86/prometheus_flask_exporter)
- [prometheus-fastapi-instrumentator](https://github.com/trallnag/prometheus-fastapi-instrumentator)
- [django-prometheus](https://github.com/korfuri/django-prometheus)
