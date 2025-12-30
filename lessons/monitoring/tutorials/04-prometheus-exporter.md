# Prometheus Exporters - Complete Guide

## Table of Contents

1. [Introduction to Exporters](#introduction-to-exporters)
2. [How Exporters Work](#how-exporters-work)
3. [Common Exporters](#common-exporters)
4. [Node Exporter](#node-exporter)
5. [Blackbox Exporter](#blackbox-exporter)
6. [Database Exporters](#database-exporters)
7. [Writing Custom Exporters](#writing-custom-exporters)
8. [Best Practices](#best-practices)

---

## Introduction to Exporters

Exporters are components that collect metrics from third-party systems and expose them in Prometheus format. They act as a bridge between systems that don't natively support Prometheus and the Prometheus server.

### Why Exporters?

- **Legacy systems**: Monitor systems that don't have native Prometheus support
- **Third-party software**: Databases, web servers, message queues
- **Hardware**: Network devices, storage systems
- **Cloud services**: AWS, GCP, Azure metrics

### Metrics Format

Exporters expose metrics at an HTTP endpoint (usually `/metrics`) in Prometheus text format:

```
# HELP http_requests_total Total number of HTTP requests
# TYPE http_requests_total counter
http_requests_total{method="GET",status="200"} 1234
http_requests_total{method="POST",status="201"} 567

# HELP temperature_celsius Current temperature
# TYPE temperature_celsius gauge
temperature_celsius{location="office"} 21.5
```

---

## How Exporters Work

```
┌─────────────────┐      ┌──────────────┐      ┌────────────────┐
│  Target System  │◄────►│   Exporter   │◄─────│   Prometheus   │
│  (MySQL, etc.)  │      │  /metrics    │ scrape│    Server     │
└─────────────────┘      └──────────────┘      └────────────────┘
```

### Pull vs Push Model

**Pull Model (Standard)**

- Prometheus scrapes exporters at configured intervals
- Exporter collects metrics on-demand when scraped

**Push Model (Pushgateway)**

- For short-lived jobs that can't be scraped
- Job pushes metrics to Pushgateway
- Prometheus scrapes Pushgateway

---

## Common Exporters

| Exporter               | Purpose                          | Default Port |
| ---------------------- | -------------------------------- | ------------ |
| Node Exporter          | Linux host metrics               | 9100         |
| Windows Exporter       | Windows host metrics             | 9182         |
| Blackbox Exporter      | Probe endpoints (HTTP, DNS, TCP) | 9115         |
| MySQL Exporter         | MySQL database metrics           | 9104         |
| PostgreSQL Exporter    | PostgreSQL metrics               | 9187         |
| Redis Exporter         | Redis metrics                    | 9121         |
| MongoDB Exporter       | MongoDB metrics                  | 9216         |
| Nginx Exporter         | Nginx metrics                    | 9113         |
| HAProxy Exporter       | HAProxy metrics                  | 9101         |
| Kafka Exporter         | Kafka metrics                    | 9308         |
| RabbitMQ Exporter      | RabbitMQ metrics                 | 9419         |
| Elasticsearch Exporter | Elasticsearch metrics            | 9114         |
| cAdvisor               | Container metrics                | 8080         |

---

## Node Exporter

Node Exporter is the most commonly used exporter for collecting Linux host metrics.

### Installation

**Docker:**

```bash
docker run -d \
  --name=node-exporter \
  --net="host" \
  --pid="host" \
  -v "/:/host:ro,rslave" \
  quay.io/prometheus/node-exporter:latest \
  --path.rootfs=/host
```

**Docker Compose:**

```yaml
version: "3.8"
services:
  node-exporter:
    image: quay.io/prometheus/node-exporter:latest
    container_name: node-exporter
    restart: unless-stopped
    network_mode: host
    pid: host
    volumes:
      - /:/host:ro,rslave
    command:
      - "--path.rootfs=/host"
      - "--collector.filesystem.mount-points-exclude=^/(sys|proc|dev|host|etc)($$|/)"
```

**Binary Installation:**

```bash
# Download
wget https://github.com/prometheus/node_exporter/releases/download/v1.7.0/node_exporter-1.7.0.linux-amd64.tar.gz

# Extract
tar xvfz node_exporter-1.7.0.linux-amd64.tar.gz

# Run
./node_exporter-1.7.0.linux-amd64/node_exporter
```

**Systemd Service:**

```ini
# /etc/systemd/system/node_exporter.service
[Unit]
Description=Node Exporter
Wants=network-online.target
After=network-online.target

[Service]
User=node_exporter
Group=node_exporter
Type=simple
ExecStart=/usr/local/bin/node_exporter

[Install]
WantedBy=multi-user.target
```

### Key Metrics

```promql
# CPU Usage
100 - (avg by(instance) (rate(node_cpu_seconds_total{mode="idle"}[5m])) * 100)

# Memory Usage
(1 - (node_memory_MemAvailable_bytes / node_memory_MemTotal_bytes)) * 100

# Disk Usage
100 - ((node_filesystem_avail_bytes / node_filesystem_size_bytes) * 100)

# Network Traffic
rate(node_network_receive_bytes_total[5m])
rate(node_network_transmit_bytes_total[5m])

# System Load
node_load1
node_load5
node_load15

# Disk I/O
rate(node_disk_read_bytes_total[5m])
rate(node_disk_written_bytes_total[5m])
```

### Collectors

Enable/disable specific collectors:

```bash
node_exporter \
  --collector.cpu \
  --collector.meminfo \
  --collector.filesystem \
  --no-collector.wifi \
  --no-collector.infiniband
```

---

## Blackbox Exporter

Blackbox Exporter probes endpoints over HTTP, HTTPS, DNS, TCP, ICMP, and gRPC.

### Installation

**Docker Compose:**

```yaml
version: "3.8"
services:
  blackbox-exporter:
    image: prom/blackbox-exporter:latest
    container_name: blackbox-exporter
    ports:
      - "9115:9115"
    volumes:
      - ./blackbox.yml:/etc/blackbox_exporter/config.yml
    command:
      - "--config.file=/etc/blackbox_exporter/config.yml"
```

### Configuration

```yaml
# blackbox.yml
modules:
  http_2xx:
    prober: http
    timeout: 5s
    http:
      valid_http_versions: ["HTTP/1.1", "HTTP/2.0"]
      valid_status_codes: [200, 201, 202]
      method: GET
      follow_redirects: true
      preferred_ip_protocol: "ip4"

  http_post_2xx:
    prober: http
    http:
      method: POST
      headers:
        Content-Type: application/json
      body: '{"key": "value"}'

  tcp_connect:
    prober: tcp
    timeout: 5s

  dns_lookup:
    prober: dns
    timeout: 5s
    dns:
      query_name: "example.com"
      query_type: "A"
      valid_rcodes:
        - NOERROR

  icmp_ping:
    prober: icmp
    timeout: 5s
    icmp:
      preferred_ip_protocol: "ip4"
```

### Prometheus Configuration

```yaml
# prometheus.yml
scrape_configs:
  - job_name: "blackbox-http"
    metrics_path: /probe
    params:
      module: [http_2xx]
    static_configs:
      - targets:
          - https://example.com
          - https://api.example.com/health
    relabel_configs:
      - source_labels: [__address__]
        target_label: __param_target
      - source_labels: [__param_target]
        target_label: instance
      - target_label: __address__
        replacement: blackbox-exporter:9115

  - job_name: "blackbox-tcp"
    metrics_path: /probe
    params:
      module: [tcp_connect]
    static_configs:
      - targets:
          - mysql:3306
          - redis:6379
    relabel_configs:
      - source_labels: [__address__]
        target_label: __param_target
      - source_labels: [__param_target]
        target_label: instance
      - target_label: __address__
        replacement: blackbox-exporter:9115
```

### Key Metrics

```promql
# Probe success (1 = success, 0 = failure)
probe_success

# HTTP response time
probe_http_duration_seconds

# SSL certificate expiry
probe_ssl_earliest_cert_expiry - time()

# DNS lookup time
probe_dns_lookup_time_seconds

# HTTP status code
probe_http_status_code
```

---

## Database Exporters

### MySQL Exporter

**Docker Compose:**

```yaml
services:
  mysql-exporter:
    image: prom/mysqld-exporter
    container_name: mysql-exporter
    ports:
      - "9104:9104"
    environment:
      - DATA_SOURCE_NAME=exporter:password@(mysql:3306)/
```

**Key Metrics:**

```promql
# Queries per second
rate(mysql_global_status_queries[5m])

# Connections
mysql_global_status_threads_connected

# Slow queries
rate(mysql_global_status_slow_queries[5m])

# Buffer pool usage
mysql_global_status_innodb_buffer_pool_pages_data / mysql_global_status_innodb_buffer_pool_pages_total
```

### PostgreSQL Exporter

**Docker Compose:**

```yaml
services:
  postgres-exporter:
    image: prometheuscommunity/postgres-exporter
    container_name: postgres-exporter
    ports:
      - "9187:9187"
    environment:
      - DATA_SOURCE_NAME=postgresql://user:password@postgres:5432/database?sslmode=disable
```

**Key Metrics:**

```promql
# Active connections
pg_stat_activity_count{state="active"}

# Database size
pg_database_size_bytes

# Transaction rate
rate(pg_stat_database_xact_commit[5m])

# Cache hit ratio
pg_stat_database_blks_hit / (pg_stat_database_blks_hit + pg_stat_database_blks_read)
```

### Redis Exporter

**Docker Compose:**

```yaml
services:
  redis-exporter:
    image: oliver006/redis_exporter
    container_name: redis-exporter
    ports:
      - "9121:9121"
    environment:
      - REDIS_ADDR=redis://redis:6379
```

**Key Metrics:**

```promql
# Connected clients
redis_connected_clients

# Memory usage
redis_memory_used_bytes

# Commands per second
rate(redis_commands_processed_total[5m])

# Cache hit ratio
redis_keyspace_hits_total / (redis_keyspace_hits_total + redis_keyspace_misses_total)
```

---

## Writing Custom Exporters

### Basic Structure

```python
#!/usr/bin/env python3
from prometheus_client import start_http_server, Gauge, Counter, Histogram
import time
import random

# Define metrics
REQUEST_COUNT = Counter('myapp_requests_total', 'Total requests', ['method', 'endpoint'])
REQUEST_LATENCY = Histogram('myapp_request_duration_seconds', 'Request latency')
TEMPERATURE = Gauge('myapp_temperature_celsius', 'Current temperature', ['location'])

def collect_metrics():
    """Collect metrics from your system"""
    # Simulate collecting metrics
    REQUEST_COUNT.labels(method='GET', endpoint='/api').inc()
    REQUEST_LATENCY.observe(random.uniform(0.1, 0.5))
    TEMPERATURE.labels(location='datacenter').set(random.uniform(20, 25))

if __name__ == '__main__':
    # Start HTTP server on port 8000
    start_http_server(8000)
    print("Exporter running on http://localhost:8000/metrics")

    while True:
        collect_metrics()
        time.sleep(15)
```

### With Custom Collector

```python
from prometheus_client import start_http_server
from prometheus_client.core import GaugeMetricFamily, CounterMetricFamily, REGISTRY

class CustomCollector:
    def collect(self):
        # Gauge metric
        gauge = GaugeMetricFamily(
            'myapp_queue_size',
            'Current queue size',
            labels=['queue_name']
        )
        gauge.add_metric(['orders'], 42)
        gauge.add_metric(['notifications'], 15)
        yield gauge

        # Counter metric
        counter = CounterMetricFamily(
            'myapp_processed_total',
            'Total processed items',
            labels=['type']
        )
        counter.add_metric(['success'], 1000)
        counter.add_metric(['failure'], 5)
        yield counter

# Register the collector
REGISTRY.register(CustomCollector())

if __name__ == '__main__':
    start_http_server(8000)
    print("Exporter running on http://localhost:8000/metrics")
    while True:
        time.sleep(1)
```

---

## Best Practices

### 1. Resource Management

- Run exporters with limited resources
- Use connection pooling for database exporters
- Set appropriate timeouts

### 2. Security

- Use TLS for sensitive exporters
- Implement authentication where needed
- Run with minimal privileges

```yaml
# Prometheus with basic auth
scrape_configs:
  - job_name: "secure-exporter"
    basic_auth:
      username: prometheus
      password: secret
    static_configs:
      - targets: ["exporter:9100"]
```

### 3. Labels

- Use consistent label names across exporters
- Avoid high-cardinality labels
- Include meaningful metadata

### 4. Monitoring Exporters

```promql
# Monitor exporter health
up{job="node-exporter"}

# Scrape duration
scrape_duration_seconds{job="node-exporter"}

# Samples scraped
scrape_samples_scraped{job="node-exporter"}
```

### 5. Documentation

- Document all custom metrics
- Include HELP and TYPE in metric output
- Maintain runbooks for alerts

---

## Complete Docker Compose Example

```yaml
version: "3.8"

services:
  prometheus:
    image: prom/prometheus:latest
    ports:
      - "9090:9090"
    volumes:
      - ./prometheus.yml:/etc/prometheus/prometheus.yml
    command:
      - "--config.file=/etc/prometheus/prometheus.yml"

  node-exporter:
    image: quay.io/prometheus/node-exporter:latest
    ports:
      - "9100:9100"
    pid: host
    volumes:
      - /:/host:ro,rslave
    command:
      - "--path.rootfs=/host"

  blackbox-exporter:
    image: prom/blackbox-exporter:latest
    ports:
      - "9115:9115"
    volumes:
      - ./blackbox.yml:/etc/blackbox_exporter/config.yml

  cadvisor:
    image: gcr.io/cadvisor/cadvisor:latest
    ports:
      - "8080:8080"
    volumes:
      - /:/rootfs:ro
      - /var/run:/var/run:ro
      - /sys:/sys:ro
      - /var/lib/docker/:/var/lib/docker:ro

  grafana:
    image: grafana/grafana:latest
    ports:
      - "3000:3000"
    environment:
      - GF_SECURITY_ADMIN_PASSWORD=admin
```

---

## Resources

- [Prometheus Exporters List](https://prometheus.io/docs/instrumenting/exporters/)
- [Node Exporter GitHub](https://github.com/prometheus/node_exporter)
- [Blackbox Exporter GitHub](https://github.com/prometheus/blackbox_exporter)
- [Writing Exporters Guide](https://prometheus.io/docs/instrumenting/writing_exporters/)
