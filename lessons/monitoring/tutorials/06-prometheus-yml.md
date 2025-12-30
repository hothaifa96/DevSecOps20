# Prometheus Configuration (prometheus.yml) - Complete Guide

## Table of Contents

1. [Introduction](#introduction)
2. [Configuration Structure](#configuration-structure)
3. [Global Configuration](#global-configuration)
4. [Scrape Configuration](#scrape-configuration)
5. [Service Discovery](#service-discovery)
6. [Relabeling](#relabeling)
7. [Alerting Configuration](#alerting-configuration)
8. [Recording Rules](#recording-rules)
9. [Remote Storage](#remote-storage)
10. [Complete Examples](#complete-examples)

---

## Introduction

The `prometheus.yml` file is the main configuration file for Prometheus. It defines:

- Global settings
- Scrape targets and intervals
- Service discovery mechanisms
- Alerting rules and Alertmanager connections
- Remote read/write endpoints

### Configuration Reload

```bash
# Method 1: Send SIGHUP signal
kill -HUP $(pgrep prometheus)

# Method 2: HTTP POST (if --web.enable-lifecycle is enabled)
curl -X POST http://localhost:9090/-/reload

# Method 3: Restart Prometheus
systemctl restart prometheus
```

---

## Configuration Structure

```yaml
# Global configuration
global:
  scrape_interval: 15s
  evaluation_interval: 15s
  scrape_timeout: 10s
  external_labels:
    cluster: production
    region: us-east-1

# Alertmanager configuration
alerting:
  alertmanagers:
    - static_configs:
        - targets: ["alertmanager:9093"]

# Rule files
rule_files:
  - "rules/*.yml"
  - "alerts/*.yml"

# Scrape configuration
scrape_configs:
  - job_name: "prometheus"
    static_configs:
      - targets: ["localhost:9090"]

# Remote write/read (optional)
remote_write:
  - url: "http://remote-storage:9090/api/v1/write"

remote_read:
  - url: "http://remote-storage:9090/api/v1/read"
```

---

## Global Configuration

```yaml
global:
  # How frequently to scrape targets (default: 1m)
  scrape_interval: 15s

  # How frequently to evaluate rules (default: 1m)
  evaluation_interval: 15s

  # Timeout for scraping (default: 10s)
  scrape_timeout: 10s

  # Labels added to all time series and alerts
  external_labels:
    cluster: production
    environment: prod
    region: us-east-1

  # Limit on number of labels per scrape
  # label_limit: 100

  # Limit on length of label names
  # label_name_length_limit: 1024

  # Limit on length of label values
  # label_value_length_limit: 2048

  # Limit on number of scraped samples
  # sample_limit: 10000

  # Limit on samples per target
  # target_limit: 100
```

---

## Scrape Configuration

### Basic Static Configuration

```yaml
scrape_configs:
  # Self-monitoring
  - job_name: "prometheus"
    static_configs:
      - targets: ["localhost:9090"]
        labels:
          env: monitoring

  # Node exporters
  - job_name: "node-exporter"
    static_configs:
      - targets:
          - "node1.example.com:9100"
          - "node2.example.com:9100"
          - "node3.example.com:9100"
        labels:
          env: production
          team: infrastructure

  # Application servers
  - job_name: "web-servers"
    scrape_interval: 10s # Override global
    scrape_timeout: 5s
    metrics_path: /metrics
    scheme: https
    static_configs:
      - targets:
          - "web1.example.com:443"
          - "web2.example.com:443"
```

### Scrape Configuration Options

```yaml
scrape_configs:
  - job_name: "example"

    # Override global scrape interval
    scrape_interval: 30s
    scrape_timeout: 10s

    # Metrics endpoint path (default: /metrics)
    metrics_path: /metrics

    # Protocol scheme (http or https)
    scheme: https

    # HTTP parameters
    params:
      module: [http_2xx]

    # Basic authentication
    basic_auth:
      username: prometheus
      password: secret
      # Or use password file
      # password_file: /etc/prometheus/password

    # Bearer token authentication
    # authorization:
    #   type: Bearer
    #   credentials: your-token
    #   # Or use credentials file
    #   credentials_file: /etc/prometheus/token

    # TLS configuration
    tls_config:
      ca_file: /etc/prometheus/ca.crt
      cert_file: /etc/prometheus/client.crt
      key_file: /etc/prometheus/client.key
      insecure_skip_verify: false

    # Follow redirects
    follow_redirects: true

    # Enable HTTP/2
    enable_http2: true

    static_configs:
      - targets: ["example.com:443"]
```

---

## Service Discovery

### File-Based Service Discovery

```yaml
scrape_configs:
  - job_name: "file-sd"
    file_sd_configs:
      - files:
          - "/etc/prometheus/targets/*.json"
          - "/etc/prometheus/targets/*.yml"
        refresh_interval: 30s
```

**Target file (JSON format):**

```json
[
  {
    "targets": ["web1:9100", "web2:9100"],
    "labels": {
      "env": "production",
      "team": "web"
    }
  },
  {
    "targets": ["db1:9104", "db2:9104"],
    "labels": {
      "env": "production",
      "team": "database"
    }
  }
]
```

**Target file (YAML format):**

```yaml
- targets:
    - web1:9100
    - web2:9100
  labels:
    env: production
    team: web
```

### Kubernetes Service Discovery

```yaml
scrape_configs:
  # Kubernetes API server
  - job_name: "kubernetes-apiservers"
    kubernetes_sd_configs:
      - role: endpoints
    scheme: https
    tls_config:
      ca_file: /var/run/secrets/kubernetes.io/serviceaccount/ca.crt
    authorization:
      credentials_file: /var/run/secrets/kubernetes.io/serviceaccount/token
    relabel_configs:
      - source_labels:
          [
            __meta_kubernetes_namespace,
            __meta_kubernetes_service_name,
            __meta_kubernetes_endpoint_port_name,
          ]
        action: keep
        regex: default;kubernetes;https

  # Kubernetes nodes
  - job_name: "kubernetes-nodes"
    kubernetes_sd_configs:
      - role: node
    scheme: https
    tls_config:
      ca_file: /var/run/secrets/kubernetes.io/serviceaccount/ca.crt
    authorization:
      credentials_file: /var/run/secrets/kubernetes.io/serviceaccount/token
    relabel_configs:
      - action: labelmap
        regex: __meta_kubernetes_node_label_(.+)

  # Kubernetes pods with annotations
  - job_name: "kubernetes-pods"
    kubernetes_sd_configs:
      - role: pod
    relabel_configs:
      # Only scrape pods with prometheus.io/scrape: "true"
      - source_labels: [__meta_kubernetes_pod_annotation_prometheus_io_scrape]
        action: keep
        regex: true

      # Use custom port from annotation
      - source_labels: [__meta_kubernetes_pod_annotation_prometheus_io_port]
        action: replace
        target_label: __address__
        regex: (.+)
        replacement: $1

      # Use custom path from annotation
      - source_labels: [__meta_kubernetes_pod_annotation_prometheus_io_path]
        action: replace
        target_label: __metrics_path__
        regex: (.+)

      # Add pod labels
      - action: labelmap
        regex: __meta_kubernetes_pod_label_(.+)

      # Add namespace label
      - source_labels: [__meta_kubernetes_namespace]
        target_label: namespace

      # Add pod name label
      - source_labels: [__meta_kubernetes_pod_name]
        target_label: pod

  # Kubernetes services
  - job_name: "kubernetes-services"
    kubernetes_sd_configs:
      - role: service
    metrics_path: /probe
    params:
      module: [http_2xx]
    relabel_configs:
      - source_labels:
          [__meta_kubernetes_service_annotation_prometheus_io_probe]
        action: keep
        regex: true
      - source_labels: [__address__]
        target_label: __param_target
      - target_label: __address__
        replacement: blackbox-exporter:9115
```

### Docker Service Discovery

```yaml
scrape_configs:
  - job_name: "docker"
    docker_sd_configs:
      - host: unix:///var/run/docker.sock
        refresh_interval: 30s
    relabel_configs:
      # Only scrape containers with prometheus-scrape=true label
      - source_labels: [__meta_docker_container_label_prometheus_scrape]
        action: keep
        regex: true

      # Use container name as instance
      - source_labels: [__meta_docker_container_name]
        target_label: instance
        regex: /(.*)
        replacement: $1
```

### Consul Service Discovery

```yaml
scrape_configs:
  - job_name: "consul"
    consul_sd_configs:
      - server: "consul.example.com:8500"
        services: [] # Empty means all services
        tags:
          - prometheus
    relabel_configs:
      - source_labels: [__meta_consul_service]
        target_label: service
      - source_labels: [__meta_consul_dc]
        target_label: datacenter
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
          - name: instance-state-name
            values:
              - running
    relabel_configs:
      - source_labels: [__meta_ec2_tag_Name]
        target_label: instance_name
      - source_labels: [__meta_ec2_instance_type]
        target_label: instance_type
      - source_labels: [__meta_ec2_availability_zone]
        target_label: availability_zone
```

### DNS Service Discovery

```yaml
scrape_configs:
  - job_name: "dns-sd"
    dns_sd_configs:
      - names:
          - "prometheus.service.consul"
          - "node-exporter.service.consul"
        type: SRV
        refresh_interval: 30s
```

---

## Relabeling

Relabeling allows you to modify labels before scraping or storing metrics.

### Common Relabel Actions

```yaml
relabel_configs:
  # keep: Keep targets matching regex
  - source_labels: [__meta_kubernetes_pod_annotation_prometheus_io_scrape]
    action: keep
    regex: true

  # drop: Drop targets matching regex
  - source_labels: [__meta_kubernetes_namespace]
    action: drop
    regex: kube-system

  # replace: Replace label value
  - source_labels: [__meta_kubernetes_pod_name]
    target_label: pod
    action: replace
    regex: (.*)
    replacement: $1

  # labelmap: Copy labels matching regex
  - action: labelmap
    regex: __meta_kubernetes_node_label_(.+)

  # labeldrop: Drop labels matching regex
  - action: labeldrop
    regex: __meta_.*

  # labelkeep: Keep only labels matching regex
  - action: labelkeep
    regex: (job|instance|namespace|pod)

  # hashmod: Set target_label to modulus of hash
  - source_labels: [__address__]
    modulus: 4
    target_label: __tmp_hash
    action: hashmod
```

### Metric Relabeling

Applied after scraping, before storing:

```yaml
scrape_configs:
  - job_name: "example"
    static_configs:
      - targets: ["localhost:9090"]
    metric_relabel_configs:
      # Drop specific metrics
      - source_labels: [__name__]
        action: drop
        regex: go_.*

      # Keep only specific metrics
      - source_labels: [__name__]
        action: keep
        regex: (http_requests_total|http_request_duration_seconds_.*)

      # Rename metric
      - source_labels: [__name__]
        action: replace
        regex: old_metric_name
        replacement: new_metric_name
        target_label: __name__

      # Drop labels
      - action: labeldrop
        regex: (id|name)
```

---

## Alerting Configuration

### Alertmanager Connection

```yaml
alerting:
  alertmanagers:
    - static_configs:
        - targets:
            - 'alertmanager1:9093'
            - 'alertmanager2:9093'

      # Optional: timeout for sending alerts
      timeout: 10s

      # Optional: path prefix
      path_prefix: /

      # Optional: scheme
      scheme: http

      # Optional: basic auth
      # basic_auth:
      #   username: user
      #   password: pass

  # With service discovery
  alertmanagers:
    - kubernetes_sd_configs:
        - role: endpoints
          namespaces:
            names:
              - monitoring
      relabel_configs:
        - source_labels: [__meta_kubernetes_service_name]
          action: keep
          regex: alertmanager
```

### Alert Rules File

```yaml
# /etc/prometheus/rules/alerts.yml
groups:
  - name: node_alerts
    rules:
      - alert: HighCPUUsage
        expr: 100 - (avg by(instance) (rate(node_cpu_seconds_total{mode="idle"}[5m])) * 100) > 80
        for: 5m
        labels:
          severity: warning
        annotations:
          summary: "High CPU usage on {{ $labels.instance }}"
          description: 'CPU usage is above 80% (current: {{ $value | printf "%.2f" }}%)'

      - alert: HighMemoryUsage
        expr: (1 - (node_memory_MemAvailable_bytes / node_memory_MemTotal_bytes)) * 100 > 85
        for: 5m
        labels:
          severity: warning
        annotations:
          summary: "High memory usage on {{ $labels.instance }}"
          description: "Memory usage is above 85%"

      - alert: DiskSpaceLow
        expr: (1 - (node_filesystem_avail_bytes / node_filesystem_size_bytes)) * 100 > 85
        for: 10m
        labels:
          severity: critical
        annotations:
          summary: "Disk space low on {{ $labels.instance }}"
          description: 'Disk {{ $labels.mountpoint }} is {{ $value | printf "%.2f" }}% full'

      - alert: InstanceDown
        expr: up == 0
        for: 1m
        labels:
          severity: critical
        annotations:
          summary: "Instance {{ $labels.instance }} is down"
          description: "{{ $labels.job }} instance {{ $labels.instance }} has been down for more than 1 minute"

  - name: http_alerts
    rules:
      - alert: HighErrorRate
        expr: |
          sum(rate(http_requests_total{status=~"5.."}[5m])) 
          / 
          sum(rate(http_requests_total[5m])) * 100 > 5
        for: 5m
        labels:
          severity: critical
        annotations:
          summary: "High HTTP error rate"
          description: 'Error rate is {{ $value | printf "%.2f" }}%'

      - alert: HighLatency
        expr: |
          histogram_quantile(0.95, 
            sum by(le) (rate(http_request_duration_seconds_bucket[5m]))
          ) > 1
        for: 5m
        labels:
          severity: warning
        annotations:
          summary: "High request latency"
          description: '95th percentile latency is {{ $value | printf "%.2f" }}s'
```

---

## Recording Rules

Pre-compute expensive queries:

```yaml
# /etc/prometheus/rules/recording.yml
groups:
  - name: node_recording_rules
    interval: 15s
    rules:
      - record: instance:node_cpu_utilization:rate5m
        expr: |
          100 - (avg by (instance) (rate(node_cpu_seconds_total{mode="idle"}[5m])) * 100)

      - record: instance:node_memory_utilization:ratio
        expr: |
          1 - (node_memory_MemAvailable_bytes / node_memory_MemTotal_bytes)

      - record: instance:node_filesystem_utilization:ratio
        expr: |
          1 - (node_filesystem_avail_bytes / node_filesystem_size_bytes)

  - name: http_recording_rules
    rules:
      - record: job:http_requests:rate5m
        expr: sum by (job) (rate(http_requests_total[5m]))

      - record: job:http_errors:rate5m
        expr: sum by (job) (rate(http_requests_total{status=~"5.."}[5m]))

      - record: job:http_error_ratio:rate5m
        expr: |
          job:http_errors:rate5m / job:http_requests:rate5m

      - record: job:http_request_duration_seconds:p95
        expr: |
          histogram_quantile(0.95,
            sum by (job, le) (rate(http_request_duration_seconds_bucket[5m]))
          )
```

---

## Remote Storage

### Remote Write

```yaml
remote_write:
  - url: "http://thanos-receive:10908/api/v1/receive"

    # Queue configuration
    queue_config:
      capacity: 10000
      max_shards: 50
      max_samples_per_send: 2000
      batch_send_deadline: 5s
      min_backoff: 30ms
      max_backoff: 5s

    # Write relabeling
    write_relabel_configs:
      - source_labels: [__name__]
        action: keep
        regex: (up|http_.*|node_.*)

    # Optional: basic auth
    # basic_auth:
    #   username: user
    #   password: pass

    # Optional: TLS
    # tls_config:
    #   ca_file: /etc/prometheus/ca.crt
```

### Remote Read

```yaml
remote_read:
  - url: "http://thanos-query:10901/api/v1/read"

    # Don't read recent data from remote (use local)
    read_recent: false

    # Required labels for queries
    required_matchers:
      job: prometheus
```

---

## Complete Examples

### Basic Development Setup

```yaml
global:
  scrape_interval: 15s
  evaluation_interval: 15s

scrape_configs:
  - job_name: "prometheus"
    static_configs:
      - targets: ["localhost:9090"]

  - job_name: "node-exporter"
    static_configs:
      - targets: ["localhost:9100"]
```

### Production Setup

```yaml
global:
  scrape_interval: 15s
  evaluation_interval: 15s
  external_labels:
    cluster: production
    region: us-east-1

alerting:
  alertmanagers:
    - static_configs:
        - targets: ["alertmanager:9093"]

rule_files:
  - "/etc/prometheus/rules/*.yml"

scrape_configs:
  # Prometheus self-monitoring
  - job_name: "prometheus"
    static_configs:
      - targets: ["localhost:9090"]

  # Node exporters
  - job_name: "node-exporter"
    file_sd_configs:
      - files: ["/etc/prometheus/targets/nodes.json"]
        refresh_interval: 30s

  # Application metrics
  - job_name: "application"
    metrics_path: /metrics
    scheme: https
    tls_config:
      ca_file: /etc/prometheus/ca.crt
    file_sd_configs:
      - files: ["/etc/prometheus/targets/apps.json"]

  # Blackbox probes
  - job_name: "blackbox-http"
    metrics_path: /probe
    params:
      module: [http_2xx]
    file_sd_configs:
      - files: ["/etc/prometheus/targets/endpoints.json"]
    relabel_configs:
      - source_labels: [__address__]
        target_label: __param_target
      - source_labels: [__param_target]
        target_label: instance
      - target_label: __address__
        replacement: blackbox-exporter:9115

remote_write:
  - url: "http://thanos-receive:10908/api/v1/receive"
    queue_config:
      max_samples_per_send: 1000
      batch_send_deadline: 5s
```

### Docker Compose Setup

```yaml
global:
  scrape_interval: 15s
  evaluation_interval: 15s

alerting:
  alertmanagers:
    - static_configs:
        - targets: ["alertmanager:9093"]

rule_files:
  - "/etc/prometheus/rules/*.yml"

scrape_configs:
  - job_name: "prometheus"
    static_configs:
      - targets: ["prometheus:9090"]

  - job_name: "node-exporter"
    static_configs:
      - targets: ["node-exporter:9100"]

  - job_name: "cadvisor"
    static_configs:
      - targets: ["cadvisor:8080"]

  - job_name: "grafana"
    static_configs:
      - targets: ["grafana:3000"]

  - job_name: "application"
    static_configs:
      - targets: ["app:8080"]
```

---

## Configuration Validation

```bash
# Check configuration syntax
promtool check config prometheus.yml

# Check rules syntax
promtool check rules rules/*.yml

# Test rules against sample data
promtool test rules test.yml
```

---

## Resources

- [Prometheus Configuration Docs](https://prometheus.io/docs/prometheus/latest/configuration/configuration/)
- [Relabeling Guide](https://prometheus.io/docs/prometheus/latest/configuration/configuration/#relabel_config)
- [Recording Rules](https://prometheus.io/docs/prometheus/latest/configuration/recording_rules/)
- [Alerting Rules](https://prometheus.io/docs/prometheus/latest/configuration/alerting_rules/)
