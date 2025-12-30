# PromQL Tutorial - Complete Guide

## Table of Contents

1. [Introduction to PromQL](#introduction-to-promql)
2. [Data Types](#data-types)
3. [Selectors and Matchers](#selectors-and-matchers)
4. [Operators](#operators)
5. [Functions](#functions)
6. [Aggregation Operators](#aggregation-operators)
7. [Recording Rules](#recording-rules)
8. [Common Queries](#common-queries)
9. [Best Practices](#best-practices)

---

## Introduction to PromQL

PromQL (Prometheus Query Language) is a powerful functional query language for selecting and aggregating time series data in Prometheus. It's essential for:

- Creating dashboards in Grafana
- Writing alerting rules
- Ad-hoc debugging and analysis
- Building recording rules

### Basic Syntax

```promql
# Simple metric query
up

# Metric with label filter
http_requests_total{method="GET"}

# Metric with multiple labels
http_requests_total{method="GET", status="200"}
```

---

## Data Types

PromQL has four data types:

### 1. Instant Vector

A set of time series with a single sample value at a specific point in time.

```promql
# Returns current value of all time series matching this metric
http_requests_total
```

### 2. Range Vector

A set of time series with a range of samples over time.

```promql
# Returns all samples from the last 5 minutes
http_requests_total[5m]
```

Time durations:
| Unit | Meaning |
|------|---------|
| `ms` | milliseconds |
| `s` | seconds |
| `m` | minutes |
| `h` | hours |
| `d` | days |
| `w` | weeks |
| `y` | years |

### 3. Scalar

A simple floating-point number.

```promql
42
3.14
```

### 4. String

A string value (limited use in PromQL).

```promql
"hello world"
```

---

## Selectors and Matchers

### Label Matchers

| Operator | Description    | Example               |
| -------- | -------------- | --------------------- |
| `=`      | Exact match    | `job="prometheus"`    |
| `!=`     | Not equal      | `status!="500"`       |
| `=~`     | Regex match    | `method=~"GET\|POST"` |
| `!~`     | Negative regex | `path!~"/api/.*"`     |

### Examples

```promql
# Exact match
http_requests_total{method="GET"}

# Not equal
http_requests_total{status!="200"}

# Regex match (GET or POST)
http_requests_total{method=~"GET|POST"}

# Regex match (starts with /api)
http_requests_total{path=~"/api/.*"}

# Multiple matchers (AND logic)
http_requests_total{method="GET", status="200", env="production"}
```

### Time Offset

```promql
# Value from 1 hour ago
http_requests_total offset 1h

# Rate from 1 day ago
rate(http_requests_total[5m] offset 1d)
```

---

## Operators

### Arithmetic Operators

| Operator | Description    |
| -------- | -------------- |
| `+`      | Addition       |
| `-`      | Subtraction    |
| `*`      | Multiplication |
| `/`      | Division       |
| `%`      | Modulo         |
| `^`      | Power          |

```promql
# Memory usage percentage
(node_memory_MemTotal_bytes - node_memory_MemAvailable_bytes) / node_memory_MemTotal_bytes * 100

# Disk usage in GB
node_filesystem_size_bytes / 1024 / 1024 / 1024
```

### Comparison Operators

| Operator | Description      |
| -------- | ---------------- |
| `==`     | Equal            |
| `!=`     | Not equal        |
| `>`      | Greater than     |
| `<`      | Less than        |
| `>=`     | Greater or equal |
| `<=`     | Less or equal    |

```promql
# Filter series where value > 100
http_requests_total > 100

# Disk usage > 80%
(node_filesystem_size_bytes - node_filesystem_avail_bytes) / node_filesystem_size_bytes * 100 > 80
```

### Logical/Set Operators

| Operator | Description  |
| -------- | ------------ |
| `and`    | Intersection |
| `or`     | Union        |
| `unless` | Complement   |

```promql
# Targets that are up AND have high memory
up == 1 and node_memory_MemAvailable_bytes < 1000000000

# All services except those starting with "test"
up unless up{job=~"test.*"}
```

### Vector Matching

```promql
# Ignore some labels
method_code:http_errors:rate5m / ignoring(code) method:http_requests:rate5m

# Only match on specific labels
method_code:http_errors:rate5m / on(method) method:http_requests:rate5m

# group_left: left side has more labels
method_code:http_errors:rate5m / ignoring(code) group_left method:http_requests:rate5m
```

---

## Functions

### Rate and Increase Functions

```promql
# rate(): Per-second rate of increase (for counters)
rate(http_requests_total[5m])

# irate(): Instant rate using last two data points
irate(http_requests_total[5m])

# increase(): Total increase over time range
increase(http_requests_total[1h])

# delta(): Difference between first and last value (for gauges)
delta(temperature_celsius[1h])
```

### Aggregation Over Time

```promql
# Average value over time
avg_over_time(node_cpu_seconds_total[5m])

# Maximum value over time
max_over_time(node_memory_MemAvailable_bytes[1h])

# Minimum value over time
min_over_time(process_cpu_seconds_total[5m])

# Sum of values over time
sum_over_time(http_requests_total[1h])

# Quantile over time
quantile_over_time(0.95, http_request_duration_seconds[5m])
```

### Math Functions

```promql
# Absolute value
abs(delta(temperature_celsius[1h]))

# Ceiling (round up)
ceil(request_duration_seconds)

# Floor (round down)
floor(request_duration_seconds)

# Clamp values to range
clamp(cpu_usage, 0, 100)
clamp_min(temperature, 0)
clamp_max(cpu_percent, 100)
```

### Histogram Functions

```promql
# Calculate histogram quantile (e.g., 95th percentile)
histogram_quantile(0.95, rate(http_request_duration_seconds_bucket[5m]))

# With aggregation by label
histogram_quantile(0.95, sum by(le, handler) (rate(http_request_duration_seconds_bucket[5m])))
```

### Label Functions

```promql
# Add/modify a label
label_replace(up, "host", "$1", "instance", "(.*):.*")

# Join labels into a new label
label_join(up, "full_address", ":", "instance", "job")
```

### Other Useful Functions

```promql
# Predict value in N seconds using linear regression
predict_linear(node_filesystem_avail_bytes[1h], 4 * 3600)

# Check if vector is empty
absent(nonexistent_metric)

# Sort ascending/descending
sort(http_requests_total)
sort_desc(http_requests_total)
```

---

## Aggregation Operators

### Basic Aggregations

```promql
# Sum all values
sum(http_requests_total)

# Average
avg(node_cpu_seconds_total)

# Minimum / Maximum
min(node_memory_MemAvailable_bytes)
max(response_time_seconds)

# Count number of series
count(up)

# Standard deviation
stddev(response_time_seconds)
```

### Aggregation with Grouping

```promql
# Sum by specific labels (keep these labels)
sum by (method, status) (http_requests_total)

# Sum without specific labels (remove these labels)
sum without (instance) (http_requests_total)

# Average by job
avg by (job) (rate(http_requests_total[5m]))

# Count by status code
count by (status) (http_requests_total)
```

### TopK and BottomK

```promql
# Top 10 by request count
topk(10, http_requests_total)

# Bottom 5 by available memory
bottomk(5, node_memory_MemAvailable_bytes)

# Top 10 request rates by handler
topk(10, sum by (handler) (rate(http_requests_total[5m])))
```

---

## Recording Rules

Recording rules precompute frequently used or expensive queries.

```yaml
# /etc/prometheus/rules/recording_rules.yml
groups:
  - name: example_recording_rules
    interval: 15s
    rules:
      # CPU usage percentage per instance
      - record: instance:node_cpu_utilization:rate5m
        expr: |
          100 - (avg by (instance) (rate(node_cpu_seconds_total{mode="idle"}[5m])) * 100)

      # Memory usage percentage per instance
      - record: instance:node_memory_utilization:ratio
        expr: |
          1 - (node_memory_MemAvailable_bytes / node_memory_MemTotal_bytes)

      # Request rate per job
      - record: job:http_requests:rate5m
        expr: sum by (job) (rate(http_requests_total[5m]))

      # Error percentage per job
      - record: job:http_error_ratio:rate5m
        expr: |
          sum by (job) (rate(http_requests_total{status=~"5.."}[5m])) 
          / 
          sum by (job) (rate(http_requests_total[5m]))
```

### Naming Conventions

```
level:metric:operations

# Examples:
job:http_requests:rate5m           # Aggregated at job level
instance:node_cpu:utilization      # Aggregated at instance level
```

---

## Common Queries

### CPU Metrics

```promql
# CPU usage percentage (single instance)
100 - (avg(rate(node_cpu_seconds_total{mode="idle"}[5m])) * 100)

# CPU usage per instance
100 - (avg by (instance) (rate(node_cpu_seconds_total{mode="idle"}[5m])) * 100)

# High CPU usage alert condition
100 - (avg by (instance) (rate(node_cpu_seconds_total{mode="idle"}[5m])) * 100) > 80
```

### Memory Metrics

```promql
# Memory usage percentage
(1 - (node_memory_MemAvailable_bytes / node_memory_MemTotal_bytes)) * 100

# Used memory in GB
(node_memory_MemTotal_bytes - node_memory_MemAvailable_bytes) / 1024 / 1024 / 1024
```

### Disk Metrics

```promql
# Disk usage percentage per mount
100 - ((node_filesystem_avail_bytes / node_filesystem_size_bytes) * 100)

# Disk space running out prediction (4 hours)
predict_linear(node_filesystem_avail_bytes[1h], 4 * 3600) < 0
```

### HTTP Metrics

```promql
# Request rate
sum(rate(http_requests_total[5m]))

# Error rate (5xx errors)
sum(rate(http_requests_total{status=~"5.."}[5m]))

# Error percentage
sum(rate(http_requests_total{status=~"5.."}[5m])) / sum(rate(http_requests_total[5m])) * 100

# Latency percentiles (histogram)
histogram_quantile(0.50, sum by (le) (rate(http_request_duration_seconds_bucket[5m])))
histogram_quantile(0.95, sum by (le) (rate(http_request_duration_seconds_bucket[5m])))
histogram_quantile(0.99, sum by (le) (rate(http_request_duration_seconds_bucket[5m])))

# Average latency
sum(rate(http_request_duration_seconds_sum[5m])) / sum(rate(http_request_duration_seconds_count[5m]))
```

### Container Metrics (cAdvisor)

```promql
# Container CPU usage
sum by (container_name) (rate(container_cpu_usage_seconds_total{container_name!=""}[5m])) * 100

# Container memory usage
container_memory_usage_bytes{container_name!=""}
```

### Kubernetes Metrics

```promql
# Pod CPU usage
sum by (pod, namespace) (rate(container_cpu_usage_seconds_total{container!=""}[5m]))

# Pods not ready
sum by (namespace) (kube_pod_status_ready{condition="false"})

# Deployment replicas mismatch
kube_deployment_status_replicas_available != kube_deployment_spec_replicas
```

---

## Best Practices

### 1. Use Recording Rules for Complex Queries

Pre-compute expensive queries to improve dashboard performance.

### 2. Use Appropriate Rate Windows

```promql
# For alerting: 5m or more to reduce noise
rate(http_requests_total[5m])

# Never use rate() on a range smaller than 2x scrape_interval
```

### 3. Always Use rate() with Counters

```promql
# WRONG: Raw counter value keeps increasing
http_requests_total

# CORRECT: Rate of change per second
rate(http_requests_total[5m])
```

### 4. Handle Missing Data

```promql
# Use 'or' to provide defaults
sum(rate(http_requests_total[5m])) or vector(0)

# Use absent() for alerting on missing metrics
absent(up{job="myservice"})
```

### 5. Avoid High-Cardinality Labels

```promql
# BAD: user_id as label (millions of unique values)
http_requests_total{user_id="123"}

# GOOD: Use aggregated labels
http_requests_total{user_type="premium"}
```

---

## Quick Reference

| Pattern         | Query                                                                |
| --------------- | -------------------------------------------------------------------- |
| Rate of counter | `rate(counter[5m])`                                                  |
| Percentage      | `(a / b) * 100`                                                      |
| Top N           | `topk(N, metric)`                                                    |
| Group by label  | `sum by (label) (metric)`                                            |
| P95 latency     | `histogram_quantile(0.95, sum by (le) (rate(histogram_bucket[5m])))` |
| Absent metric   | `absent(metric{labels})`                                             |

---

## Resources

- [Prometheus Query Docs](https://prometheus.io/docs/prometheus/latest/querying/basics/)
- [PromQL Cheat Sheet](https://promlabs.com/promql-cheat-sheet/)
- [Robust Perception Blog](https://www.robustperception.io/blog/)
