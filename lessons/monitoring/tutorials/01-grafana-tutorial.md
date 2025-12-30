# Grafana Tutorial - Complete Guide

## Table of Contents

1. [Introduction to Grafana](#introduction-to-grafana)
2. [Installation](#installation)
3. [Core Concepts](#core-concepts)
4. [Data Sources](#data-sources)
5. [Creating Dashboards](#creating-dashboards)
6. [Panels and Visualizations](#panels-and-visualizations)
7. [Alerting](#alerting)
8. [Best Practices](#best-practices)

---

## Introduction to Grafana

Grafana is an open-source analytics and interactive visualization platform. It provides charts, graphs, and alerts when connected to supported data sources.

### Key Features

- **Multi-platform support**: Runs on Linux, Windows, macOS, and Docker
- **Multiple data sources**: Prometheus, InfluxDB, Elasticsearch, MySQL, PostgreSQL, and many more
- **Rich visualizations**: Time series graphs, gauges, tables, heatmaps, and more
- **Alerting**: Built-in alerting with notification channels
- **Templating**: Dynamic dashboards with variables
- **Annotations**: Mark events on graphs
- **Plugins**: Extend functionality with community plugins

---

## Installation

### Docker Installation (Recommended)

```bash
# Pull the official Grafana image
docker pull grafana/grafana:latest

# Run Grafana container
docker run -d \
  --name=grafana \
  -p 3000:3000 \
  -v grafana-storage:/var/lib/grafana \
  grafana/grafana:latest
```

### Docker Compose Installation

```yaml
# docker-compose.yml
version: "3.8"

services:
  grafana:
    image: grafana/grafana:latest
    container_name: grafana
    ports:
      - "3000:3000"
    volumes:
      - grafana-data:/var/lib/grafana
      - ./grafana/provisioning:/etc/grafana/provisioning
    environment:
      - GF_SECURITY_ADMIN_USER=admin
      - GF_SECURITY_ADMIN_PASSWORD=admin123
      - GF_USERS_ALLOW_SIGN_UP=false
    restart: unless-stopped

volumes:
  grafana-data:
```

### Linux Installation (Ubuntu/Debian)

```bash
# Add Grafana GPG key
sudo apt-get install -y apt-transport-https software-properties-common wget
wget -q -O - https://packages.grafana.com/gpg.key | sudo apt-key add -

# Add Grafana repository
echo "deb https://packages.grafana.com/oss/deb stable main" | sudo tee -a /etc/apt/sources.list.d/grafana.list

# Install Grafana
sudo apt-get update
sudo apt-get install grafana

# Start Grafana service
sudo systemctl daemon-reload
sudo systemctl start grafana-server
sudo systemctl enable grafana-server
```

### Access Grafana

- URL: `http://localhost:3000`
- Default credentials: `admin` / `admin`

---

## Core Concepts

### 1. Data Sources

Data sources are the storage backends for your metrics, logs, and traces. Common examples:

- **Prometheus**: Time-series metrics
- **Loki**: Log aggregation
- **Jaeger/Tempo**: Distributed tracing
- **InfluxDB**: Time-series database
- **Elasticsearch**: Search and analytics

### 2. Dashboards

A dashboard is a collection of panels organized on a grid. Dashboards can be:

- Created manually
- Imported from Grafana.com
- Provisioned via configuration files

### 3. Panels

Panels are the building blocks of dashboards. Each panel displays data in a specific visualization format:

- Time series
- Stat
- Gauge
- Bar chart
- Table
- Heatmap
- And many more...

### 4. Organizations

Organizations are isolated instances within Grafana that allow multi-tenancy:

- Separate data sources
- Separate dashboards
- Separate users

### 5. Users and Permissions

Grafana supports role-based access control:

- **Admin**: Full access
- **Editor**: Can create/edit dashboards
- **Viewer**: Read-only access

---

## Data Sources

### Adding Prometheus as Data Source

1. Navigate to **Configuration** → **Data Sources**
2. Click **Add data source**
3. Select **Prometheus**
4. Configure:
   ```
   Name: Prometheus
   URL: http://prometheus:9090
   Access: Server (default)
   ```
5. Click **Save & Test**

### Data Source Configuration via Provisioning

Create `/etc/grafana/provisioning/datasources/datasources.yml`:

```yaml
apiVersion: 1

datasources:
  - name: Prometheus
    type: prometheus
    access: proxy
    url: http://prometheus:9090
    isDefault: true
    editable: false

  - name: Loki
    type: loki
    access: proxy
    url: http://loki:3100
    editable: false
```

---

## Creating Dashboards

### Manual Dashboard Creation

1. Click **+** → **Dashboard**
2. Click **Add new panel**
3. Configure the query
4. Choose visualization type
5. Set panel title and options
6. Click **Apply**
7. Save dashboard with **Ctrl+S** or click the save icon

### Dashboard JSON Structure

```json
{
  "dashboard": {
    "id": null,
    "uid": "my-dashboard",
    "title": "My Dashboard",
    "tags": ["monitoring", "production"],
    "timezone": "browser",
    "refresh": "5s",
    "panels": [
      {
        "id": 1,
        "title": "CPU Usage",
        "type": "timeseries",
        "gridPos": {
          "h": 8,
          "w": 12,
          "x": 0,
          "y": 0
        },
        "targets": [
          {
            "expr": "100 - (avg(rate(node_cpu_seconds_total{mode=\"idle\"}[5m])) * 100)",
            "refId": "A"
          }
        ]
      }
    ]
  },
  "overwrite": true
}
```

### Importing Dashboards

1. Click **+** → **Import**
2. Enter Dashboard ID from grafana.com (e.g., `1860` for Node Exporter Full)
3. Select data source
4. Click **Import**

### Popular Dashboard IDs

| Dashboard          | ID   | Description                 |
| ------------------ | ---- | --------------------------- |
| Node Exporter Full | 1860 | Linux host metrics          |
| Docker Monitoring  | 893  | Docker container metrics    |
| Kubernetes Cluster | 6417 | K8s cluster overview        |
| Prometheus Stats   | 2    | Prometheus internal metrics |

---

## Panels and Visualizations

### Time Series Panel

The most common panel type for metrics over time.

```promql
# CPU Usage Query
100 - (avg by(instance) (rate(node_cpu_seconds_total{mode="idle"}[5m])) * 100)
```

Panel options:

- **Legend**: Configure legend display
- **Tooltip**: Hover information settings
- **Graph styles**: Lines, bars, points
- **Axis**: Configure Y-axis units and range
- **Thresholds**: Set color-coded thresholds

### Stat Panel

Display single values with optional sparkline.

```promql
# Total Memory
node_memory_MemTotal_bytes / 1024 / 1024 / 1024
```

Options:

- **Value options**: Show last, mean, max, etc.
- **Stat styles**: Background color mode
- **Text mode**: Value, name, or both

### Gauge Panel

Circular gauge for percentage-based metrics.

```promql
# Memory Usage Percentage
(1 - (node_memory_MemAvailable_bytes / node_memory_MemTotal_bytes)) * 100
```

### Table Panel

Display data in tabular format.

```promql
# Top 10 containers by CPU
topk(10, sum by(container_name) (rate(container_cpu_usage_seconds_total[5m])))
```

### Bar Gauge

Horizontal or vertical bar visualization.

```promql
# Disk usage per mount
100 - ((node_filesystem_avail_bytes / node_filesystem_size_bytes) * 100)
```

---

## Alerting

### Creating Alert Rules

1. Edit a panel
2. Go to **Alert** tab
3. Click **Create alert rule from this panel**
4. Configure:

```yaml
# Alert Rule Configuration
Rule name: High CPU Usage
Folder: Production Alerts

# Query and condition
A: Prometheus query - avg(rate(node_cpu_seconds_total{mode="idle"}[5m])) * 100
B: Reduce - Last value of A
C: Threshold - Is below 20 (meaning CPU > 80%)

# Evaluation
Evaluate every: 1m
For: 5m

# Labels and annotations
Labels:
  severity: warning
  team: ops

Annotations:
  summary: High CPU usage detected
  description: CPU usage is above 80% for more than 5 minutes
```

### Notification Channels

#### Slack Configuration

```yaml
# /etc/grafana/provisioning/notifiers/slack.yml
notifiers:
  - name: Slack
    type: slack
    uid: slack-notifier
    settings:
      url: https://hooks.slack.com/services/xxx/yyy/zzz
      channel: "#alerts"
      username: Grafana
```

#### Email Configuration

Add to `grafana.ini`:

```ini
[smtp]
enabled = true
host = smtp.gmail.com:587
user = alerts@example.com
password = app-password
from_address = alerts@example.com
from_name = Grafana Alerts
```

### Alert Rule via Provisioning

```yaml
# /etc/grafana/provisioning/alerting/rules.yml
apiVersion: 1

groups:
  - orgId: 1
    name: Production Alerts
    folder: alerts
    interval: 1m
    rules:
      - uid: high-cpu-alert
        title: High CPU Usage
        condition: C
        data:
          - refId: A
            relativeTimeRange:
              from: 600
              to: 0
            datasourceUid: prometheus
            model:
              expr: 100 - (avg(rate(node_cpu_seconds_total{mode="idle"}[5m])) * 100)
              refId: A
          - refId: B
            relativeTimeRange:
              from: 600
              to: 0
            datasourceUid: __expr__
            model:
              type: reduce
              expression: A
              reducer: last
              refId: B
          - refId: C
            relativeTimeRange:
              from: 600
              to: 0
            datasourceUid: __expr__
            model:
              type: threshold
              expression: B
              conditions:
                - evaluator:
                    type: gt
                    params:
                      - 80
        for: 5m
        labels:
          severity: warning
        annotations:
          summary: High CPU usage on {{ $labels.instance }}
```

---

## Best Practices

### Dashboard Design

1. **Use meaningful names**: Clear titles for dashboards and panels
2. **Organize with rows**: Group related panels using collapsible rows
3. **Consistent time ranges**: Use dashboard time picker, not per-panel
4. **Use variables**: Create dynamic dashboards with template variables
5. **Documentation**: Add text panels to explain dashboard purpose

### Variables/Templating

```yaml
# Example variable configuration
Name: instance
Type: Query
Data source: Prometheus
Query: label_values(up, instance)
Refresh: On dashboard load
Multi-value: true
Include All option: true
```

Usage in queries:

```promql
node_cpu_seconds_total{instance=~"$instance"}
```

### Performance Optimization

1. **Limit time range**: Default to 1-6 hours for real-time monitoring
2. **Use recording rules**: Pre-compute expensive queries in Prometheus
3. **Limit data points**: Set appropriate min interval (15s-1m)
4. **Avoid regex**: Use exact matches when possible

### Security

1. **Change default admin password** immediately
2. **Enable HTTPS** in production
3. **Use authentication** (LDAP, OAuth, etc.)
4. **Limit anonymous access**
5. **Regular backups** of dashboards and configurations

### Backup and Restore

```bash
# Backup dashboards via API
curl -H "Authorization: Bearer $API_KEY" \
  "http://localhost:3000/api/dashboards/uid/my-dashboard" \
  > dashboard-backup.json

# Restore dashboard
curl -X POST \
  -H "Authorization: Bearer $API_KEY" \
  -H "Content-Type: application/json" \
  -d @dashboard-backup.json \
  "http://localhost:3000/api/dashboards/db"
```

---

## Quick Reference

### Useful Keyboard Shortcuts

| Shortcut | Action             |
| -------- | ------------------ |
| `Ctrl+S` | Save dashboard     |
| `Ctrl+H` | Hide/show rows     |
| `Ctrl+F` | Find panel         |
| `d+s`    | Dashboard settings |
| `d+v`    | Toggle view mode   |
| `Esc`    | Exit edit mode     |

### Common API Endpoints

```bash
# Health check
GET /api/health

# List dashboards
GET /api/search

# Get dashboard by UID
GET /api/dashboards/uid/:uid

# Create/update dashboard
POST /api/dashboards/db

# List data sources
GET /api/datasources
```

---

## Resources

- [Grafana Documentation](https://grafana.com/docs/)
- [Grafana Dashboard Repository](https://grafana.com/grafana/dashboards/)
- [Grafana Community](https://community.grafana.com/)
- [Grafana GitHub](https://github.com/grafana/grafana)
