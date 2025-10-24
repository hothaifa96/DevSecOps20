# Complete Docker Compose Tutorial

A comprehensive guide for DevOps students - from basics to advanced scenarios

---

## Table of Contents

1. [Introduction to Docker Compose](#introduction)
2. [Installation](#installation)
3. [Basic Concepts](#basic-concepts)
4. [Your First Compose File](#first-compose)
5. [Core Commands](#core-commands)
6. [Service Configuration](#service-configuration)
7. [Networks in Compose](#networks)
8. [Volumes in Compose](#volumes)
9. [Environment Variables](#environment-variables)
10. [Hands-On Examples](#hands-on-examples)
11. [Best Practices](#best-practices)
12. [Troubleshooting](#troubleshooting)
13. [Real-World Projects](#real-world-projects)

---

## Introduction to Docker Compose

### What is Docker Compose?

Docker Compose is a tool for defining and running multi-container Docker applications. Instead of running multiple `docker run` commands, you define your entire application stack in a single YAML file.

### Why Use Docker Compose?

**Without Compose:**
```bash
docker network create my-network
docker volume create db-data
docker run -d --name database --network my-network -v db-data:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=secret mysql:8.0
docker run -d --name backend --network my-network -p 3000:3000 -e DB_HOST=database my-api
docker run -d --name frontend --network my-network -p 8080:80 my-web
```

**With Compose:**
```yaml
# docker-compose.yml
version: '3.8'
services:
  database:
    image: mysql:8.0
    environment:
      MYSQL_ROOT_PASSWORD: secret
    volumes:
      - db-data:/var/lib/mysql
  
  backend:
    image: my-api
    environment:
      DB_HOST: database
    ports:
      - "3000:3000"
    depends_on:
      - database
  
  frontend:
    image: my-web
    ports:
      - "8080:80"
    depends_on:
      - backend

volumes:
  db-data:
```

Then just run: `docker-compose up`

---

## Installation

### Docker Desktop (Recommended for Beginners)

Docker Desktop includes Docker Compose automatically.

**Check if installed:**
```bash
docker-compose --version
```

### Linux Installation

```bash
# Download the latest version
sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose

# Make it executable
sudo chmod +x /usr/local/bin/docker-compose

# Verify installation
docker-compose --version
```

---

## Basic Concepts

### Compose File Structure

```yaml
version: '3.8'                    # Compose file version

services:                         # Define your containers
  service-name:                   # Custom name for your service
    image: image-name:tag         # Docker image to use
    # ... more configuration

networks:                         # Define custom networks
  network-name:                   # Custom network name
    driver: bridge                # Network driver

volumes:                          # Define named volumes
  volume-name:                    # Custom volume name
```

### Version History

- `3.8` - Latest version 3 (recommended)
- `3.7`, `3.6`, `3.5` - Older but still supported
- `2.x` - Legacy, avoid for new projects
- `1.x` - Deprecated

**Use version 3.8 for new projects!**

---

## Your First Compose File

### Example 1: Simple Web Server

Create a file named `docker-compose.yml`:

```yaml
version: '3.8'

services:
  web:
    image: nginx:latest
    ports:
      - "8080:80"
```

**Run it:**
```bash
docker-compose up
```

**Access:** Open browser to `http://localhost:8080`

**Stop it:**
```bash
# Press Ctrl+C or in another terminal:
docker-compose down
```

---

## Core Commands

### Essential Commands

```bash
# Start services in foreground
docker-compose up

# Start services in background (detached)
docker-compose up -d

# Stop and remove containers, networks
docker-compose down

# Stop and remove containers, networks, AND volumes
docker-compose down -v

# View running services
docker-compose ps

# View logs
docker-compose logs

# Follow logs in real-time
docker-compose logs -f

# View logs for specific service
docker-compose logs -f service-name

# Execute command in running service
docker-compose exec service-name command

# Build or rebuild services
docker-compose build

# Build without cache
docker-compose build --no-cache

# Pull latest images
docker-compose pull

# Start services
docker-compose start

# Stop services (without removing)
docker-compose stop

# Restart services
docker-compose restart

# Pause services
docker-compose pause

# Unpause services
docker-compose unpause

# Remove stopped containers
docker-compose rm

# Scale a service
docker-compose up -d --scale service-name=3
```

---

## Service Configuration

### Complete Service Options

```yaml
version: '3.8'

services:
  myservice:
    # Image to use
    image: nginx:latest
    
    # OR build from Dockerfile
    build:
      context: ./app
      dockerfile: Dockerfile
      args:
        - BUILD_VERSION=1.0
    
    # Container name (optional, defaults to project_service_number)
    container_name: my-nginx-container
    
    # Port mapping (HOST:CONTAINER)
    ports:
      - "8080:80"
      - "443:443"
    
    # Expose ports without publishing (only to linked services)
    expose:
      - "3000"
    
    # Environment variables
    environment:
      - NODE_ENV=production
      - API_KEY=secret123
      - DEBUG=true
    
    # OR from .env file
    env_file:
      - ./config.env
    
    # Volumes
    volumes:
      - ./data:/app/data              # Bind mount
      - app-logs:/var/log              # Named volume
      - /var/run/docker.sock:/var/run/docker.sock  # System mount
    
    # Networks
    networks:
      - frontend
      - backend
    
    # Dependencies (start order)
    depends_on:
      - database
      - cache
    
    # Command to run
    command: npm start
    
    # Working directory
    working_dir: /app
    
    # Restart policy
    restart: always
    # Options: no, always, on-failure, unless-stopped
    
    # Health check
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost"]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 40s
    
    # Resource limits
    deploy:
      resources:
        limits:
          cpus: '0.5'
          memory: 512M
        reservations:
          cpus: '0.25'
          memory: 256M
    
    # User to run as
    user: "1000:1000"
    
    # Hostname
    hostname: myservice
    
    # DNS
    dns:
      - 8.8.8.8
      - 8.8.4.4
    
    # Extra hosts
    extra_hosts:
      - "somehost:162.242.195.82"
    
    # Labels
    labels:
      - "com.example.description=My Service"
      - "com.example.version=1.0"
```

---

## Networks in Compose

### Default Network

By default, Compose creates a single network for your app. All services can communicate using service names as hostnames.

```yaml
version: '3.8'

services:
  web:
    image: nginx
  
  api:
    image: node:latest
    # Can reach web at: http://web:80
```

### Custom Networks

```yaml
version: '3.8'

services:
  frontend:
    image: nginx
    networks:
      - frontend-net
  
  backend:
    image: node:latest
    networks:
      - frontend-net
      - backend-net
  
  database:
    image: postgres
    networks:
      - backend-net

networks:
  frontend-net:
    driver: bridge
  backend-net:
    driver: bridge
    internal: true  # No external access
```

### Network Configuration Options

```yaml
networks:
  my-network:
    driver: bridge
    driver_opts:
      com.docker.network.bridge.name: my-bridge
    ipam:
      config:
        - subnet: 172.28.0.0/16
          gateway: 172.28.0.1
    labels:
      - "com.example.description=My Network"
```

### Using Existing Networks

```yaml
networks:
  existing-network:
    external: true
```

---

## Volumes in Compose

### Volume Types

```yaml
version: '3.8'

services:
  app:
    image: myapp
    volumes:
      # Named volume
      - app-data:/app/data
      
      # Bind mount (absolute path)
      - /host/path:/container/path
      
      # Bind mount (relative path)
      - ./local-dir:/app/config
      
      # Read-only mount
      - ./config.yml:/app/config.yml:ro
      
      # Anonymous volume
      - /app/node_modules

volumes:
  app-data:
    driver: local
```

### Volume Configuration

```yaml
volumes:
  db-data:
    driver: local
    driver_opts:
      type: none
      o: bind
      device: /path/on/host
  
  backup-data:
    external: true
    name: actual-volume-name
```

### Volume Best Practices

```yaml
version: '3.8'

services:
  database:
    image: postgres:15
    volumes:
      # Data persistence
      - db-data:/var/lib/postgresql/data
      
      # Initialization scripts
      - ./init-scripts:/docker-entrypoint-initdb.d:ro
      
      # Backup location
      - ./backups:/backups

volumes:
  db-data:
```

---

## Environment Variables

### Method 1: Inline

```yaml
services:
  app:
    image: myapp
    environment:
      - NODE_ENV=production
      - DB_HOST=database
      - DB_PORT=5432
```

### Method 2: Environment File

**.env file:**
```env
NODE_ENV=production
DB_HOST=database
DB_PORT=5432
API_KEY=secret123
```

**docker-compose.yml:**
```yaml
services:
  app:
    image: myapp
    env_file:
      - .env
```

### Method 3: Multiple Environment Files

```yaml
services:
  app:
    image: myapp
    env_file:
      - ./common.env
      - ./production.env
```

### Variable Substitution

**.env:**
```env
TAG=latest
DB_PASSWORD=secret123
```

**docker-compose.yml:**
```yaml
services:
  app:
    image: myapp:${TAG}
    environment:
      - DB_PASSWORD=${DB_PASSWORD}
```

---

## Hands-On Examples

### Example 1: WordPress with MySQL

```yaml
version: '3.8'

services:
  wordpress:
    image: wordpress:latest
    ports:
      - "8080:80"
    environment:
      WORDPRESS_DB_HOST: db
      WORDPRESS_DB_USER: wordpress
      WORDPRESS_DB_PASSWORD: wordpress
      WORDPRESS_DB_NAME: wordpress
    volumes:
      - wordpress-data:/var/www/html
    depends_on:
      - db
    restart: always

  db:
    image: mysql:8.0
    environment:
      MYSQL_DATABASE: wordpress
      MYSQL_USER: wordpress
      MYSQL_PASSWORD: wordpress
      MYSQL_ROOT_PASSWORD: rootpassword
    volumes:
      - db-data:/var/lib/mysql
    restart: always

volumes:
  wordpress-data:
  db-data:
```

**Run:**
```bash
docker-compose up -d
```

**Access:** `http://localhost:8080`

---

### Example 2: Node.js App with MongoDB and Redis

```yaml
version: '3.8'

services:
  app:
    build: .
    ports:
      - "3000:3000"
    environment:
      - NODE_ENV=production
      - MONGO_URL=mongodb://mongo:27017/myapp
      - REDIS_URL=redis://redis:6379
    depends_on:
      - mongo
      - redis
    volumes:
      - ./logs:/app/logs
    restart: unless-stopped

  mongo:
    image: mongo:6
    ports:
      - "27017:27017"
    environment:
      MONGO_INITDB_ROOT_USERNAME: admin
      MONGO_INITDB_ROOT_PASSWORD: secret
    volumes:
      - mongo-data:/data/db
    restart: unless-stopped

  redis:
    image: redis:7-alpine
    ports:
      - "6379:6379"
    volumes:
      - redis-data:/data
    restart: unless-stopped

volumes:
  mongo-data:
  redis-data:
```

---

### Example 3: Python Flask with PostgreSQL

```yaml
version: '3.8'

services:
  web:
    build: ./flask-app
    command: python app.py
    ports:
      - "5000:5000"
    environment:
      - FLASK_ENV=development
      - DATABASE_URL=postgresql://user:password@db:5432/mydb
    volumes:
      - ./flask-app:/app
    depends_on:
      db:
        condition: service_healthy
    restart: on-failure

  db:
    image: postgres:15-alpine
    environment:
      POSTGRES_USER: user
      POSTGRES_PASSWORD: password
      POSTGRES_DB: mydb
    volumes:
      - postgres-data:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U user"]
      interval: 10s
      timeout: 5s
      retries: 5
    restart: always

volumes:
  postgres-data:
```

---

### Example 4: Full Stack with Nginx Reverse Proxy

```yaml
version: '3.8'

services:
  nginx:
    image: nginx:alpine
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf:ro
      - ./ssl:/etc/nginx/ssl:ro
    depends_on:
      - frontend
      - backend
    networks:
      - frontend-net
    restart: always

  frontend:
    build: ./react-app
    expose:
      - "3000"
    networks:
      - frontend-net
    restart: always

  backend:
    build: ./api
    expose:
      - "5000"
    environment:
      - DB_HOST=postgres
      - REDIS_HOST=redis
    depends_on:
      - postgres
      - redis
    networks:
      - frontend-net
      - backend-net
    restart: always

  postgres:
    image: postgres:15
    environment:
      POSTGRES_PASSWORD: secret
    volumes:
      - db-data:/var/lib/postgresql/data
    networks:
      - backend-net
    restart: always

  redis:
    image: redis:7-alpine
    networks:
      - backend-net
    restart: always

networks:
  frontend-net:
  backend-net:
    internal: true

volumes:
  db-data:
```

---

### Example 5: Development Environment with Hot Reload

```yaml
version: '3.8'

services:
  frontend:
    build:
      context: ./frontend
      dockerfile: Dockerfile.dev
    ports:
      - "3000:3000"
    volumes:
      - ./frontend/src:/app/src
      - /app/node_modules
    environment:
      - CHOKIDAR_USEPOLLING=true
      - REACT_APP_API_URL=http://localhost:5000
    stdin_open: true
    tty: true

  backend:
    build:
      context: ./backend
      dockerfile: Dockerfile.dev
    ports:
      - "5000:5000"
    volumes:
      - ./backend:/app
      - /app/node_modules
    environment:
      - NODE_ENV=development
      - DB_HOST=postgres
    depends_on:
      - postgres
    command: npm run dev

  postgres:
    image: postgres:15
    environment:
      POSTGRES_PASSWORD: devpassword
      POSTGRES_DB: devdb
    ports:
      - "5432:5432"
    volumes:
      - dev-db:/var/lib/postgresql/data

volumes:
  dev-db:
```

---

## Best Practices

### 1. Use .env Files for Secrets

**DO NOT commit secrets to git!**

**.env (add to .gitignore):**
```env
DB_PASSWORD=secret123
API_KEY=your-api-key
```

**.env.example (commit this):**
```env
DB_PASSWORD=changeme
API_KEY=your-api-key-here
```

### 2. Use Health Checks

```yaml
services:
  database:
    image: postgres:15
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U postgres"]
      interval: 10s
      timeout: 5s
      retries: 5
```

### 3. Proper Restart Policies

```yaml
services:
  web:
    restart: unless-stopped  # Production
  
  dev-tools:
    restart: no  # Development tools
```

### 4. Use Named Volumes

```yaml
# Good
volumes:
  - db-data:/var/lib/mysql

# Avoid (anonymous volumes)
volumes:
  - /var/lib/mysql
```

### 5. Network Isolation

```yaml
services:
  frontend:
    networks:
      - public
  
  backend:
    networks:
      - public
      - private
  
  database:
    networks:
      - private  # Not accessible from frontend

networks:
  public:
  private:
    internal: true
```

### 6. Use Specific Image Tags

```yaml
# Good
image: postgres:15.2-alpine

# Avoid (unpredictable)
image: postgres:latest
```

### 7. Resource Limits

```yaml
services:
  web:
    deploy:
      resources:
        limits:
          cpus: '0.50'
          memory: 512M
```

### 8. Logging Configuration

```yaml
services:
  web:
    logging:
      driver: "json-file"
      options:
        max-size: "10m"
        max-file: "3"
```

---

## Troubleshooting

### Common Issues and Solutions

#### 1. Port Already in Use

**Error:**
```
ERROR: for web  Cannot start service web: driver failed programming external connectivity
```

**Solution:**
```bash
# Find what's using the port
sudo lsof -i :8080

# Change port in docker-compose.yml
ports:
  - "8081:80"  # Use different host port
```

#### 2. Container Exits Immediately

**Check logs:**
```bash
docker-compose logs service-name
```

**Common causes:**
- Missing environment variables
- Wrong command
- Application error

#### 3. Services Can't Communicate

**Check networks:**
```bash
docker network ls
docker network inspect projectname_default
```

**Verify service names are correct:**
```yaml
environment:
  - DB_HOST=database  # Must match service name
```

#### 4. Volume Permission Issues

**Solution:**
```yaml
services:
  app:
    user: "${UID}:${GID}"
    volumes:
      - ./data:/app/data
```

#### 5. Build Cache Issues

**Rebuild without cache:**
```bash
docker-compose build --no-cache
docker-compose up -d --force-recreate
```

### Debugging Commands

```bash
# View service details
docker-compose ps

# Check service logs
docker-compose logs -f service-name

# Execute command in service
docker-compose exec service-name bash

# Inspect configuration
docker-compose config

# Validate compose file
docker-compose config --quiet

# View service IPs
docker-compose ps -q | xargs docker inspect --format='{{.Name}} - {{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}'
```

---

## Real-World Projects

### Project 1: E-Commerce Application

```yaml
version: '3.8'

services:
  # Frontend
  storefront:
    build: ./storefront
    ports:
      - "80:80"
    depends_on:
      - api-gateway
    networks:
      - frontend

  # API Gateway
  api-gateway:
    build: ./api-gateway
    ports:
      - "8080:8080"
    environment:
      - PRODUCT_SERVICE_URL=http://product-service:3001
      - ORDER_SERVICE_URL=http://order-service:3002
      - USER_SERVICE_URL=http://user-service:3003
    networks:
      - frontend
      - backend

  # Microservices
  product-service:
    build: ./services/products
    environment:
      - DB_HOST=postgres
      - REDIS_HOST=redis
    depends_on:
      - postgres
      - redis
    networks:
      - backend

  order-service:
    build: ./services/orders
    environment:
      - DB_HOST=postgres
      - RABBITMQ_HOST=rabbitmq
    depends_on:
      - postgres
      - rabbitmq
    networks:
      - backend

  user-service:
    build: ./services/users
    environment:
      - DB_HOST=postgres
    depends_on:
      - postgres
    networks:
      - backend

  # Databases
  postgres:
    image: postgres:15
    environment:
      POSTGRES_PASSWORD: ${DB_PASSWORD}
    volumes:
      - postgres-data:/var/lib/postgresql/data
      - ./init-db:/docker-entrypoint-initdb.d
    networks:
      - backend

  redis:
    image: redis:7-alpine
    volumes:
      - redis-data:/data
    networks:
      - backend

  # Message Queue
  rabbitmq:
    image: rabbitmq:3-management
    ports:
      - "15672:15672"
    volumes:
      - rabbitmq-data:/var/lib/rabbitmq
    networks:
      - backend

networks:
  frontend:
  backend:

volumes:
  postgres-data:
  redis-data:
  rabbitmq-data:
```

### Project 2: CI/CD Pipeline

```yaml
version: '3.8'

services:
  jenkins:
    image: jenkins/jenkins:lts
    ports:
      - "8080:8080"
      - "50000:50000"
    volumes:
      - jenkins-data:/var/jenkins_home
      - /var/run/docker.sock:/var/run/docker.sock
    networks:
      - cicd

  gitlab:
    image: gitlab/gitlab-ce:latest
    ports:
      - "80:80"
      - "443:443"
      - "22:22"
    volumes:
      - gitlab-config:/etc/gitlab
      - gitlab-logs:/var/log/gitlab
      - gitlab-data:/var/opt/gitlab
    networks:
      - cicd

  sonarqube:
    image: sonarqube:community
    ports:
      - "9000:9000"
    environment:
      - SONAR_JDBC_URL=jdbc:postgresql://postgres:5432/sonar
      - SONAR_JDBC_USERNAME=sonar
      - SONAR_JDBC_PASSWORD=sonar
    depends_on:
      - postgres
    volumes:
      - sonarqube-data:/opt/sonarqube/data
      - sonarqube-extensions:/opt/sonarqube/extensions
      - sonarqube-logs:/opt/sonarqube/logs
    networks:
      - cicd

  postgres:
    image: postgres:15
    environment:
      POSTGRES_USER: sonar
      POSTGRES_PASSWORD: sonar
      POSTGRES_DB: sonar
    volumes:
      - postgresql-data:/var/lib/postgresql/data
    networks:
      - cicd

  nexus:
    image: sonatype/nexus3
    ports:
      - "8081:8081"
    volumes:
      - nexus-data:/nexus-data
    networks:
      - cicd

networks:
  cicd:

volumes:
  jenkins-data:
  gitlab-config:
  gitlab-logs:
  gitlab-data:
  sonarqube-data:
  sonarqube-extensions:
  sonarqube-logs:
  postgresql-data:
  nexus-data:
```

### Project 3: Monitoring Stack

```yaml
version: '3.8'

services:
  prometheus:
    image: prom/prometheus:latest
    ports:
      - "9090:9090"
    volumes:
      - ./prometheus.yml:/etc/prometheus/prometheus.yml
      - prometheus-data:/prometheus
    command:
      - '--config.file=/etc/prometheus/prometheus.yml'
      - '--storage.tsdb.path=/prometheus'
    networks:
      - monitoring

  grafana:
    image: grafana/grafana:latest
    ports:
      - "3000:3000"
    environment:
      - GF_SECURITY_ADMIN_PASSWORD=admin
      - GF_USERS_ALLOW_SIGN_UP=false
    volumes:
      - grafana-data:/var/lib/grafana
      - ./grafana/dashboards:/etc/grafana/provisioning/dashboards
      - ./grafana/datasources:/etc/grafana/provisioning/datasources
    depends_on:
      - prometheus
    networks:
      - monitoring

  node-exporter:
    image: prom/node-exporter:latest
    ports:
      - "9100:9100"
    volumes:
      - /proc:/host/proc:ro
      - /sys:/host/sys:ro
      - /:/rootfs:ro
    command:
      - '--path.procfs=/host/proc'
      - '--path.sysfs=/host/sys'
      - '--collector.filesystem.mount-points-exclude=^/(sys|proc|dev|host|etc)($$|/)'
    networks:
      - monitoring

  alertmanager:
    image: prom/alertmanager:latest
    ports:
      - "9093:9093"
    volumes:
      - ./alertmanager.yml:/etc/alertmanager/alertmanager.yml
      - alertmanager-data:/alertmanager
    networks:
      - monitoring

  loki:
    image: grafana/loki:latest
    ports:
      - "3100:3100"
    volumes:
      - ./loki-config.yml:/etc/loki/local-config.yaml
      - loki-data:/loki
    networks:
      - monitoring

networks:
  monitoring:

volumes:
  prometheus-data:
  grafana-data:
  alertmanager-data:
  loki-data:
```

---

## Advanced Topics

### Using Profiles

```yaml
version: '3.8'

services:
  app:
    image: myapp
    profiles:
      - production
  
  debug-tools:
    image: debug-image
    profiles:
      - development

  test-db:
    image: postgres:15
    profiles:
      - testing
```

**Usage:**
```bash
# Start only production services
docker-compose --profile production up

# Start development services
docker-compose --profile development up

# Start multiple profiles
docker-compose --profile production --profile development up
```

### Override Files

**docker-compose.yml (base):**
```yaml
version: '3.8'
services:
  app:
    image: myapp
    environment:
      - NODE_ENV=production
```

**docker-compose.override.yml (auto-loaded):**
```yaml
version: '3.8'
services:
  app:
    environment:
      - DEBUG=true
    ports:
      - "3000:3000"
```

**docker-compose.prod.yml:**
```yaml
version: '3.8'
services:
  app:
    environment:
      - NODE_ENV=production
      - DEBUG=false
    restart: always
```

**Usage:**
```bash
# Development (uses override automatically)
docker-compose up

# Production (explicit file)
docker-compose -f docker-compose.yml -f docker-compose.prod.yml up -d
```

### Extension Fields

```yaml
version: '3.8'

x-logging: &default-logging
  driver: "json-file"
  options:
    max-size: "10m"
    max-file: "3"

x-common-environment: &common-env
  NODE_ENV: production
  LOG_LEVEL: info

services:
  service1:
    image: service1
    logging: *default-logging
    environment:
      <<: *common-env
      SERVICE_NAME: service1
  
  service2:
    image: service2
    logging: *default-logging
    environment:
      <<: *common-env
      SERVICE_NAME: service2
```

---

## Student Exercises

### Exercise 1: Basic Multi-Container App
Create a compose file with nginx and a simple HTML page served from a volume.

### Exercise 2: Database-Backed Application
Deploy WordPress with MySQL and ensure data persists.

### Exercise 3: Network Isolation
Create a 3-tier application with proper network isolation.

### Exercise 4: Development Environment
Set up a hot-reload development environment for a Node.js application.

### Exercise 5: Production Stack
Build a complete production-ready stack with monitoring, logging, and backups.

---

## Cheat Sheet

```bash
# Start services
docker-compose up -d

# Stop services
docker-compose down

# View logs
docker-compose logs -f

# Execute command
docker-compose exec service bash

# Rebuild services
docker-compose build

# Scale service
docker-compose up -d --scale web=3

# View running services
docker-compose ps

# Restart service
docker-compose restart service

# Remove everything including volumes
docker-compose down -v

# Validate compose file
docker-compose config
```

---

## Summary

Docker Compose simplifies multi-container application management by:
- Defining infrastructure as code
- Enabling one-command deployment
- Managing dependencies and networks automatically
- Supporting different environments through profiles and override files

**Key Takeaways:**
1. Always use version 3.8 for new projects
2. Use named volumes for persistence
3. Implement proper network isolation
4. Use health checks for critical services
5. Never commit secrets to version control
6. Use specific image tags, not 'latest'
7. Implement proper restart policies
8. Test locally before deploying to production

---