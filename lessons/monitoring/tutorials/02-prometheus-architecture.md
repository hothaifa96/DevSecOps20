# Prometheus Architecture - Complete Guide

## Table of Contents

1. [Introduction](#introduction)
2. [Architecture Overview](#architecture-overview)
3. [Core Components](#core-components)
4. [Data Model](#data-model)
5. [Storage Architecture](#storage-architecture)
6. [Service Discovery](#service-discovery)
7. [High Availability](#high-availability)
8. [Federation](#federation)
9. [Scaling Prometheus](#scaling-prometheus)

---

## Introduction

Prometheus is an open-source systems monitoring and alerting toolkit originally built at SoundCloud. It has become the de facto standard for monitoring in cloud-native environments and is a graduated project of the Cloud Native Computing Foundation (CNCF).

### Key Characteristics

- **Multi-dimensional data model**: Time series identified by metric name and key/value pairs (labels)
- **PromQL**: Flexible query language for leveraging dimensionality
- **Pull-based model**: Prometheus scrapes metrics from targets
- **No distributed storage**: Single server nodes are autonomous
- **Service discovery**: Automatic discovery of targets to monitor
- **Built-in alerting**: Alertmanager handles alerts and notifications

---

## Architecture Overview

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                           PROMETHEUS ECOSYSTEM                               │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐    │
│  │   Target 1   │  │   Target 2   │  │   Target 3   │  │   Target N   │    │
│  │  /metrics    │  │  /metrics    │  │  /metrics    │  │  /metrics    │    │
│  └──────┬───────┘  └──────┬───────┘  └──────┬───────┘  └──────┬───────┘    │
│         │                 │                 │                 │             │
│         │    ┌────────────┴────────────┬────┴─────────────────┘             │
│         │    │         PULL            │                                     │
│         ▼    ▼                         ▼                                     │
│  ┌───────────────────────────────────────────────────────────────┐          │
│  │                      PROMETHEUS SERVER                         │          │
│  │  ┌─────────────┐  ┌─────────────┐  ┌─────────────────────┐   │          │
│  │  │  Retrieval  │  │    TSDB     │  │   HTTP Server       │   │          │
│  │  │  (Scraper)  │──│  (Storage)  │──│   (PromQL API)      │   │          │
│  │  └─────────────┘  └─────────────┘  └─────────────────────┘   │          │
│  │         │                                    │                │          │
│  │  ┌──────┴──────┐                            │                │          │
│  │  │   Service   │                            │                │          │
│  │  │  Discovery  │                            │                │          │
│  │  └─────────────┘                            │                │          │
│  └─────────────────────────────────────────────┼────────────────┘          │
│                    │                           │                            │
│                    ▼                           ▼                            │
│         ┌─────────────────┐          ┌─────────────────┐                   │
│         │  Alertmanager   │          │     Grafana     │                   │
│         │                 │          │   (Dashboards)  │                   │
│         └────────┬────────┘          └─────────────────┘                   │
│                  │                                                          │
│                  ▼                                                          │
│    ┌─────────┬─────────┬─────────┬─────────┐                               │
│    │  Email  │  Slack  │ PagerDuty│ Webhook │                               │
│    └─────────┴─────────┴─────────┴─────────┘                               │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Core Components

### 1. Prometheus Server

The main component that performs:

- **Scraping**: Collects metrics from configured targets
- **Storage**: Stores time series data locally
- **Querying**: Provides PromQL query interface
- **Rule evaluation**: Processes recording and alerting rules

```yaml
# Basic prometheus.yml structure
global:
  scrape_interval: 15s # How often to scrape targets
  evaluation_interval: 15s # How often to evaluate rules

rule_files:
  - "rules/*.yml" # Recording and alerting rules

scrape_configs:
  - job_name: "prometheus"
    static_configs:
      - targets: ["localhost:9090"]
```

### 2. Exporters

Exporters expose metrics from third-party systems in Prometheus format.

| Exporter            | Purpose            | Default Port |
| ------------------- | ------------------ | ------------ |
| Node Exporter       | Linux host metrics | 9100         |
| Blackbox Exporter   | Probe endpoints    | 9115         |
| MySQL Exporter      | MySQL metrics      | 9104         |
| PostgreSQL Exporter | PostgreSQL metrics | 9187         |
| Redis Exporter      | Redis metrics      | 9121         |
| cAdvisor            | Container metrics  | 8080         |

### 3. Pushgateway

For short-lived jobs that can't be scraped:

```
┌────────────────┐    PUSH    ┌──────────────┐    PULL    ┌────────────┐
│  Batch Job     │ ─────────► │  Pushgateway │ ◄───────── │ Prometheus │
└────────────────┘            └──────────────┘            └────────────┘
```

```bash
# Push metrics to Pushgateway
echo "batch_job_duration_seconds 42" | curl --data-binary @- \
  http://pushgateway:9091/metrics/job/batch_job/instance/server1
```

### 4. Alertmanager

Handles alerts from Prometheus servers:

- **Grouping**: Combines similar alerts
- **Inhibition**: Suppresses certain alerts when others are firing
- **Silencing**: Temporarily mute alerts
- **Routing**: Sends alerts to appropriate receivers

```yaml
# alertmanager.yml
global:
  resolve_timeout: 5m

route:
  group_by: ["alertname", "cluster", "service"]
  group_wait: 30s
  group_interval: 5m
  repeat_interval: 3h
  receiver: "slack-notifications"

  routes:
    - match:
        severity: critical
      receiver: "pagerduty-critical"

receivers:
  - name: "slack-notifications"
    slack_configs:
      - api_url: "https://hooks.slack.com/services/xxx/yyy/zzz"
        channel: "#alerts"

  - name: "pagerduty-critical"
    pagerduty_configs:
      - service_key: "your-service-key"
```

### 5. Client Libraries

Instrument your applications directly:

- Go
- Java/Scala
- Python
- Ruby
- Rust
- Node.js
- C++
- .NET

---

## Data Model

### Time Series

A time series is uniquely identified by:

- **Metric name**: Describes the general feature being measured
- **Labels**: Key-value pairs providing dimensions

```
<metric_name>{<label1>=<value1>, <label2>=<value2>, ...}
```

Example:

```
http_requests_total{method="GET", handler="/api/users", status="200"}
```

### Metric Types

#### 1. Counter

Cumulative metric that only increases (or resets to zero on restart).

```
# HELP http_requests_total Total number of HTTP requests
# TYPE http_requests_total counter
http_requests_total{method="GET", status="200"} 1234
http_requests_total{method="POST", status="201"} 567
```

#### 2. Gauge

Metric that can go up and down.

```
# HELP temperature_celsius Current temperature
# TYPE temperature_celsius gauge
temperature_celsius{location="office"} 21.5
```

#### 3. Histogram

Samples observations and counts them in buckets.

```
# HELP http_request_duration_seconds Request duration histogram
# TYPE http_request_duration_seconds histogram
http_request_duration_seconds_bucket{le="0.1"} 5000
http_request_duration_seconds_bucket{le="0.5"} 8000
http_request_duration_seconds_bucket{le="1"} 9500
http_request_duration_seconds_bucket{le="+Inf"} 10000
http_request_duration_seconds_sum 4500.5
http_request_duration_seconds_count 10000
```

#### 4. Summary

Similar to histogram but calculates configurable quantiles.

```
# HELP go_gc_duration_seconds GC duration summary
# TYPE go_gc_duration_seconds summary
go_gc_duration_seconds{quantile="0.5"} 0.000105
go_gc_duration_seconds{quantile="0.9"} 0.000232
go_gc_duration_seconds{quantile="0.99"} 0.000452
go_gc_duration_seconds_sum 1.234
go_gc_duration_seconds_count 5678
```

### Naming Conventions

```
# Format: <namespace>_<name>_<unit>

# Good examples:
prometheus_http_requests_total
node_cpu_seconds_total
http_request_duration_seconds
process_resident_memory_bytes

# Bad examples:
requests          # Too vague
cpu               # No unit
request_latency   # Non-standard unit name
```

---

## Storage Architecture

### Local Storage (TSDB)

Prometheus uses a custom time-series database optimized for:

- Append-only writes
- High compression
- Fast queries over recent data

```
┌─────────────────────────────────────────────────────────┐
│                    PROMETHEUS TSDB                       │
├─────────────────────────────────────────────────────────┤
│                                                          │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐     │
│  │   Block 1   │  │   Block 2   │  │   Block 3   │     │
│  │  (2h data)  │  │  (2h data)  │  │  (2h data)  │     │
│  └─────────────┘  └─────────────┘  └─────────────┘     │
│         ▲                                                │
│         │         ┌─────────────┐                       │
│         │         │    Head     │ ◄── Active writes     │
│         │         │   Block     │                       │
│         │         └─────────────┘                       │
│         │                │                               │
│         │       Compaction every 2h                      │
│         └────────────────┘                               │
│                                                          │
│  WAL (Write-Ahead Log) - crash recovery                 │
│  └── checkpoint/                                         │
│  └── 000001                                              │
│  └── 000002                                              │
│                                                          │
└─────────────────────────────────────────────────────────┘
```

### Block Structure

```
data/
├── 01BKGV7JBM69T2G1BGBGM6KB12/     # Block ID (ULID)
│   ├── chunks/                       # Compressed time series data
│   │   └── 000001
│   ├── index                         # Inverted index
│   ├── meta.json                     # Block metadata
│   └── tombstones                    # Deletion markers
├── 01BKGTZQ1SYQJTR4PB43C8PD98/
│   └── ...
├── chunks_head/                      # Current head block chunks
├── wal/                              # Write-ahead log
│   ├── checkpoint.000001/
│   ├── 000002
│   └── 000003
└── lock                              # Process lock file
```

### Retention Configuration

```yaml
# prometheus.yml or command line flags
storage:
  tsdb:
    path: /prometheus/data
    retention:
      time: 15d # Keep data for 15 days
      size: 50GB # Or until 50GB is used
```

Command line:

```bash
prometheus \
  --storage.tsdb.path=/prometheus/data \
  --storage.tsdb.retention.time=15d \
  --storage.tsdb.retention.size=50GB
```

### Remote Storage

For long-term storage, use remote write/read:

```yaml
# prometheus.yml
remote_write:
  - url: "http://thanos-receive:10908/api/v1/receive"
    queue_config:
      max_samples_per_send: 1000
      batch_send_deadline: 5s

remote_read:
  - url: "http://thanos-query:10901/api/v1/read"
    read_recent: false
```

Popular long-term storage solutions:

- **Thanos**: Highly available, long-term storage
- **Cortex**: Horizontally scalable, multi-tenant
- **VictoriaMetrics**: Fast, cost-effective
- **M3DB**: Distributed time series database

---

## Service Discovery

### Static Configuration

```yaml
scrape_configs:
  - job_name: "web-servers"
    static_configs:
      - targets:
          - "web1.example.com:9100"
          - "web2.example.com:9100"
        labels:
          env: production
          team: frontend
```

### File-Based Discovery

```yaml
scrape_configs:
  - job_name: "file-sd"
    file_sd_configs:
      - files:
          - "/etc/prometheus/targets/*.json"
        refresh_interval: 30s
```

Target file (`/etc/prometheus/targets/web.json`):

```json
[
  {
    "targets": ["web1:9100", "web2:9100"],
    "labels": {
      "env": "production",
      "team": "web"
    }
  }
]
```

### Kubernetes Service Discovery

```yaml
scrape_configs:
  - job_name: "kubernetes-pods"
    kubernetes_sd_configs:
      - role: pod
    relabel_configs:
      # Only scrape pods with annotation prometheus.io/scrape: "true"
      - source_labels: [__meta_kubernetes_pod_annotation_prometheus_io_scrape]
        action: keep
        regex: true

      # Use annotation for custom port
      - source_labels: [__meta_kubernetes_pod_annotation_prometheus_io_port]
        action: replace
        target_label: __address__
        regex: (.+)
        replacement: ${1}

      # Use annotation for custom path
      - source_labels: [__meta_kubernetes_pod_annotation_prometheus_io_path]
        action: replace
        target_label: __metrics_path__
        regex: (.+)

  - job_name: "kubernetes-services"
    kubernetes_sd_configs:
      - role: service
    relabel_configs:
      - source_labels:
          [__meta_kubernetes_service_annotation_prometheus_io_scrape]
        action: keep
        regex: true

  - job_name: "kubernetes-nodes"
    kubernetes_sd_configs:
      - role: node
    relabel_configs:
      - action: labelmap
        regex: __meta_kubernetes_node_label_(.+)
```

### Consul Service Discovery

```yaml
scrape_configs:
  - job_name: "consul"
    consul_sd_configs:
      - server: "consul.example.com:8500"
        services: [] # All services
    relabel_configs:
      - source_labels: [__meta_consul_tags]
        regex: .*,prometheus,.*
        action: keep
```

### AWS EC2 Service Discovery

```yaml
scrape_configs:
  - job_name: "aws-ec2"
    ec2_sd_configs:
      - region: us-east-1
        access_key: YOUR_ACCESS_KEY
        secret_key: YOUR_SECRET_KEY
        port: 9100
        filters:
          - name: tag:Environment
            values:
              - production
    relabel_configs:
      - source_labels: [__meta_ec2_tag_Name]
        target_label: instance_name
```

---

## High Availability

### Prometheus HA Setup

Run multiple identical Prometheus instances:

```
┌────────────────┐     ┌────────────────┐
│  Prometheus 1  │     │  Prometheus 2  │
│  (identical)   │     │  (identical)   │
└───────┬────────┘     └───────┬────────┘
        │                      │
        │    ┌─────────────┐   │
        └────│    Targets  │───┘
             └─────────────┘
                   │
        ┌──────────┴──────────┐
        ▼                     ▼
┌───────────────┐    ┌───────────────┐
│ Alertmanager 1│    │ Alertmanager 2│
│   (cluster)   │◄──►│   (cluster)   │
└───────────────┘    └───────────────┘
```

Alertmanager cluster configuration:

```yaml
# alertmanager.yml on node 1
cluster:
  listen-address: "0.0.0.0:9094"
  peers:
    - alertmanager2:9094
```

### Thanos for HA and Long-term Storage

```
┌─────────────────────────────────────────────────────────────────┐
│                        THANOS ARCHITECTURE                       │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  ┌────────────┐  ┌────────────┐                                 │
│  │ Prometheus │  │ Prometheus │                                 │
│  │   + Sidecar│  │   + Sidecar│                                 │
│  └─────┬──────┘  └─────┬──────┘                                 │
│        │               │                                         │
│        ▼               ▼                                         │
│  ┌─────────────────────────────┐                                │
│  │       Object Storage        │ (S3, GCS, Azure Blob)          │
│  └─────────────┬───────────────┘                                │
│                │                                                 │
│        ┌───────┴────────┐                                       │
│        ▼                ▼                                        │
│  ┌──────────┐    ┌──────────┐                                   │
│  │  Store   │    │ Compactor │                                  │
│  │ Gateway  │    │          │                                    │
│  └────┬─────┘    └──────────┘                                   │
│       │                                                          │
│       ▼                                                          │
│  ┌──────────┐                                                   │
│  │  Querier │◄──── Grafana                                      │
│  └──────────┘                                                   │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## Federation

### Hierarchical Federation

```
                    ┌──────────────────┐
                    │  Global Prometheus│
                    │   (aggregated)   │
                    └────────┬─────────┘
                             │ federate
              ┌──────────────┼──────────────┐
              ▼              ▼              ▼
       ┌───────────┐  ┌───────────┐  ┌───────────┐
       │ DC1 Prom  │  │ DC2 Prom  │  │ DC3 Prom  │
       └───────────┘  └───────────┘  └───────────┘
```

Global Prometheus configuration:

```yaml
scrape_configs:
  - job_name: "federate"
    scrape_interval: 60s
    honor_labels: true
    metrics_path: "/federate"
    params:
      "match[]":
        - '{job="prometheus"}'
        - '{__name__=~"job:.*"}' # Aggregated metrics
        - '{__name__=~"instance:.*"}'
    static_configs:
      - targets:
          - "prometheus-dc1:9090"
          - "prometheus-dc2:9090"
          - "prometheus-dc3:9090"
```

### Cross-Service Federation

```yaml
scrape_configs:
  - job_name: "federate-team-metrics"
    honor_labels: true
    metrics_path: "/federate"
    params:
      "match[]":
        - '{team="payments"}'
    static_configs:
      - targets: ["prometheus-payments:9090"]
```

---

## Scaling Prometheus

### Vertical Scaling

- Increase CPU, RAM, and SSD storage
- Single Prometheus can handle millions of time series

### Horizontal Scaling with Functional Sharding

```yaml
# prometheus-infrastructure.yml
scrape_configs:
  - job_name: 'node'
    static_configs:
      - targets: [...]
  - job_name: 'kubernetes-infra'
    kubernetes_sd_configs:
      - role: node

# prometheus-applications.yml
scrape_configs:
  - job_name: 'app-metrics'
    kubernetes_sd_configs:
      - role: pod
    relabel_configs:
      - source_labels: [__meta_kubernetes_namespace]
        regex: (production|staging)
        action: keep
```

### Hash-Based Sharding

```yaml
# prometheus-shard-0.yml
scrape_configs:
  - job_name: "all-targets"
    relabel_configs:
      - source_labels: [__address__]
        modulus: 2
        target_label: __tmp_hash
        action: hashmod
      - source_labels: [__tmp_hash]
        regex: ^0$
        action: keep
```

---

## Summary

| Component         | Purpose                    | Scaling Strategy              |
| ----------------- | -------------------------- | ----------------------------- |
| Prometheus Server | Scraping, storage, queries | Sharding, Thanos              |
| Alertmanager      | Alert routing              | Clustering                    |
| Exporters         | Expose metrics             | Per-target deployment         |
| Pushgateway       | Short-lived jobs           | Single instance per cluster   |
| Grafana           | Visualization              | Stateless, horizontal scaling |

---

## Resources

- [Prometheus Documentation](https://prometheus.io/docs/)
- [Prometheus GitHub](https://github.com/prometheus/prometheus)
- [Thanos Project](https://thanos.io/)
- [Cortex Project](https://cortexmetrics.io/)
- [VictoriaMetrics](https://victoriametrics.com/)
