# Kubernetes Multi-Tier Application Hackathon

## Overview

The hackathon is your chance to spend some decent time modelling and deploying a Kubernetes app on your own.

You'll use all the key skills you've learned in the course, and:
* 😣 you will get stuck
* 💥 you will have errors and broken apps
* 📑 you will need to research and troubleshoot

That's why the hackathon is so useful!

It will help you understand which areas you're comfortable with and where you need to spend some more time.
And it will give you an app that you modelled yourself, which you can use as a reference next time you model a new app.

ℹ️ There are several parts to the hackathon - you're not expected to complete them all. In some classes we have a whole day for this, in others just a few hours. Get as far as you can in the time, it's all great experience.

---

## Choose Your Application

You can choose from three different applications. All have verified working images on Docker Hub:

### **Option 1: Docker Voting App** ⭐ RECOMMENDED
**Best for:** Students who want a cool, interactive frontend

**Application Components:**
- **Vote (Frontend)** - Python Flask web app with a modern UI
- **Redis** - In-memory queue for collecting votes
- **Worker** - .NET service that processes votes
- **PostgreSQL** - Database for storing results
- **Result (Frontend)** - Node.js real-time results dashboard

**Why it's great:**
- ✅ Official Docker sample application
- ✅ Cool interactive voting interface (Cats vs Dogs)
- ✅ Real-time results visualization
- ✅ Uses multiple programming languages
- ✅ All images verified and working

---

### **Option 2: RSVP App**
**Best for:** Students who want something simpler

**Application Components:**
- **Frontend** - Python Flask RSVP application
- **MongoDB** - Database for storing RSVPs

**Why it's good:**
- ✅ Simpler 2-tier architecture
- ✅ Good for beginners
- ✅ Clean interface

---

# Deploy Your Application (Docker Voting App)

We'll use the **Docker Voting App** for this tutorial. If you chose a different app, adapt the instructions accordingly.

## Architecture Overview

```
┌─────────────────────────────────────────────────────────────┐
│                    Internet / Users                          │
└────────────────────┬──────────────────┬─────────────────────┘
                     │                  │
              ┌──────▼────────┐  ┌──────▼────────┐
              │  Vote App     │  │  Result App   │
              │  (Frontend)   │  │  (Frontend)   │
              │  NodePort     │  │  NodePort     │
              │  Port: 31000  │  │  Port: 31001  │
              └──────┬────────┘  └──────┬────────┘
                     │                  │
              ┌──────▼────────┐         │
              │     Redis     │         │
              │  (ClusterIP)  │         │
              │   Port: 6379  │         │
              └──────┬────────┘         │
                     │                  │
              ┌──────▼──────────────────▼──┐
              │        Worker              │
              │     (ClusterIP)            │
              │    No external port        │
              └──────┬────────────────────┘
                     │
              ┌──────▼────────┐
              │   PostgreSQL  │
              │  (ClusterIP)  │
              │   Port: 5432  │
              └───────────────┘
```

## Docker Images to Use

| Component | Docker Image | Replicas | Port |
|-----------|-------------|----------|------|
| Vote | `dockersamples/examplevotingapp_vote:latest` | 2 | 80 |
| Redis | `redis:alpine` | 1 | 6379 |
| Worker | `dockersamples/examplevotingapp_worker:latest` | 1 | N/A |
| PostgreSQL | `postgres:15-alpine` | 1 | 5432 |
| Result | `dockersamples/examplevotingapp_result:latest` | 1 | 80 |

## Service Requirements

| Service | Type | Port | Target Port | NodePort |
|---------|------|------|-------------|----------|
| vote | NodePort | 80 | 80 | 31000 |
| redis | ClusterIP | 6379 | 6379 | - |
| db | ClusterIP | 5432 | 5432 | - |
| result | NodePort | 80 | 80 | 31001 |

**Note:** Worker doesn't need a service as it's a background processor.

## Your Tasks

1. Create a namespace called `voting-app`
2. Create Deployment manifests for all 5 components
3. Create Service manifests for vote, redis, db, and result
4. Deploy everything to your cluster
5. Access the vote frontend at `http://localhost:31000`
6. Access the result dashboard at `http://localhost:31001`

### Hints

- DNS names for services: `redis`, `db`, `vote`, `result`
- The Vote app connects to Redis using hostname `redis`
- The Worker connects to both Redis (`redis`) and PostgreSQL (`db`)
- The Result app connects to PostgreSQL (`db`)
- PostgreSQL needs environment variables:
  - `POSTGRES_USER=postgres`
  - `POSTGRES_PASSWORD=postgres` (we'll secure this in Part 2!)

### Expected Result

When you're done:
- Navigate to `http://localhost:31000` - You should see the voting page (Cats vs Dogs)
- Cast your vote
- Navigate to `http://localhost:31001` - You should see live results updating

### Solution Directory Structure

```
hackathon/
└── part-1/
    ├── namespace.yaml
    ├── vote/
    │   ├── deployment.yaml
    │   └── service.yaml
    ├── redis/
    │   ├── deployment.yaml
    │   └── service.yaml
    ├── worker/
    │   └── deployment.yaml
    ├── db/
    │   ├── deployment.yaml
    │   └── service.yaml
    └── result/
        ├── deployment.yaml
        └── service.yaml
```

**Deploy everything:**
```bash
kubectl apply -f hackathon/part-1/namespace.yaml
kubectl apply -f hackathon/part-1/ -R
```

---

## Part 2 - Configuration Management

Great job! Now let's make this production-ready by externalizing configuration.

### Problems to Solve

1. **Database credentials are hardcoded** - Anyone with access to the deployment can see the password
2. **Service connections are hardcoded** - Hard to change environments
3. **Application behavior** - No way to customize options without rebuilding images

### Configuration Requirements

#### 1. Create Secrets for Sensitive Data

**Database Secret:**
- `POSTGRES_USER=postgres`
- `POSTGRES_PASSWORD=postgres123!`

#### 2. Create ConfigMaps for Non-Sensitive Data

**Vote App ConfigMap:**
- `OPTION_A=Cats`
- `OPTION_B=Dogs`
- `REDIS_HOST=redis`

**Worker ConfigMap:**
- `REDIS_HOST=redis`
- `POSTGRES_HOST=db`

**Result App ConfigMap:**
- `POSTGRES_HOST=db`

### Your Tasks

1. Create a Secret for database credentials
2. Create ConfigMaps for each application component
3. Update your Deployments to use ConfigMaps and Secrets
4. Use fully-qualified domain names (FQDN) for service connections
   - Example: `redis.voting-app.svc.cluster.local`
5. Customize the voting options (change from Cats/Dogs to something fun!)

### Hints

**Using Secrets in Deployments:**
```yaml
env:
  - name: POSTGRES_PASSWORD
    valueFrom:
      secretKeyRef:
        name: db-secret
        key: POSTGRES_PASSWORD
```

**Using ConfigMaps in Deployments:**
```yaml
env:
  - name: OPTION_A
    valueFrom:
      configMapKeyRef:
        name: vote-config
        key: OPTION_A
```

**Testing your ConfigMaps:**
```bash
# Check if ConfigMap exists
kubectl get configmap -n voting-app

# View ConfigMap contents
kubectl describe configmap vote-config -n voting-app

# Test environment variables in a pod
kubectl exec -it deployment/vote -n voting-app -- printenv
```

### Expected Result

- Same functionality but with externalized configuration
- You should see your custom voting options
- Database password is no longer visible in deployments
- All services use FQDNs for communication

### Solution

```bash
kubectl apply -f hackathon/part-2/secrets.yaml -n voting-app
kubectl apply -f hackathon/part-2/configmaps.yaml -n voting-app
kubectl apply -f hackathon/part-2/ -R -n voting-app
```

---

## Part 3 - Persistent Storage & Volumes optinal 

Time to add persistence and caching!

### Requirements

#### 1. Database Persistence
The PostgreSQL database needs persistent storage so data survives Pod restarts.

**Your tasks:**
- Add a PersistentVolumeClaim (PVC) for PostgreSQL
- Mount the volume to `/var/lib/postgresql/data`
- Size: 1Gi
- AccessMode: ReadWriteOnce

#### 2. Redis Caching
Redis could benefit from a volume for cache persistence (though not critical).

**Your tasks:**
- Add an `emptyDir` volume for Redis
- Mount to `/data`
- This survives container restarts but not Pod deletions (good for cache)

### Hints

**PersistentVolumeClaim example:**
```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: db-data
spec:
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 1Gi
```

**Using PVC in Deployment:**
```yaml
volumes:
  - name: db-data
    persistentVolumeClaim:
      claimName: db-data
```

**EmptyDir volume:**
```yaml
volumes:
  - name: redis-data
    emptyDir: {}
```

**Check PVC status:**
```bash
kubectl get pvc -n voting-app
kubectl describe pvc db-data -n voting-app
```

### Expected Result

- Database data persists even if Pod is deleted
- Vote counts remain after database Pod restart
- Redis has a temporary cache volume

### Solution

```bash
kubectl apply -f hackathon/part-3/db/pvc.yaml -n voting-app
kubectl apply -f hackathon/part-3/ -R -n voting-app
```

---

## Part 4 - Ingress & DNS optinal

Let's set up proper DNS names instead of using NodePorts!

### Requirements

Deploy an Ingress Controller and create Ingress rules for:
- `vote.local` → Vote application
- `result.local` → Result application

### Your Tasks

1. Deploy NGINX Ingress Controller
2. Create Ingress resource with rules for both applications
3. Update your `/etc/hosts` file
4. Change Services from NodePort to ClusterIP
5. Test access via DNS names

### Sample Ingress Resource

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: voting-app-ingress
  namespace: voting-app
  annotations:
    nginx.ingress.kubernetes.io/rewrite-target: /
spec:
  ingressClassName: nginx
  rules:
  - host: vote.local
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: vote
            port:
              number: 80
  - host: result.local
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: result
            port:
              number: 80
```

### Deploy NGINX Ingress Controller

```bash
kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/controller-v1.8.1/deploy/static/provider/cloud/deploy.yaml
```

### Update /etc/hosts

```bash
# Linux/macOS
echo "127.0.0.1 vote.local result.local" | sudo tee -a /etc/hosts

# Windows (PowerShell as Admin)
Add-Content -Path C:\Windows\System32\drivers\etc\hosts -Value "127.0.0.1 vote.local"
Add-Content -Path C:\Windows\System32\drivers\etc\hosts -Value "127.0.0.1 result.local"
```

### Expected Result

- Access vote at `http://vote.local`
- Access results at `http://result.local`
- No more NodePorts needed!

### Solution

```bash
kubectl apply -f hackathon/part-4/ingress-controller/
kubectl apply -f hackathon/part-4/ingress.yaml -n voting-app
kubectl apply -f hackathon/part-4/ -R -n voting-app
```

---

## Part 5 - Production Readiness

Time to productionize! Add the following to ALL your Deployments:

### 1. Health Checks

**Liveness Probes** (restart if unhealthy):
```yaml
livenessProbe:
  httpGet:
    path: /
    port: 80
  initialDelaySeconds: 15
  periodSeconds: 10
```

**Readiness Probes** (don't send traffic if not ready):
```yaml
readinessProbe:
  httpGet:
    path: /
    port: 80
  initialDelaySeconds: 5
  periodSeconds: 5
```

### 2. Resource Limits

```yaml
resources:
  requests:
    memory: "64Mi"
    cpu: "50m"
  limits:
    memory: "128Mi"
    cpu: "100m"
```


### 4. Pod Disruption Budget

```yaml
apiVersion: policy/v1
kind: PodDisruptionBudget
metadata:
  name: vote-pdb
spec:
  minAvailable: 1
  selector:
    matchLabels:
      app: vote
```

### Your Tasks

Add all production features to:
- Vote deployment
- Result deployment
- Worker deployment
- Redis deployment
- PostgreSQL deployment

### Health Check Endpoints

| Component | Path | Port |
|-----------|------|------|
| Vote | `/` | 80 |
| Result | `/` | 80 |
| Redis | TCP Socket | 6379 |
| PostgreSQL | `pg_isready` | 5432 |

### Expected Result

- All Pods have health checks
- Resources are limited
- Security contexts applied
- High availability ensured

### Solution

```bash
kubectl apply -f hackathon/part-5/ -R -n voting-app
```

---



### Useful Commands

```bash
# Check all resources in namespace
kubectl get all -n voting-app

# View logs
kubectl logs -n voting-app deployment/vote
kubectl logs -n voting-app deployment/vote --follow

# Execute commands in pod
kubectl exec -it -n voting-app deployment/vote -- /bin/sh

# Port forward (for debugging)
kubectl port-forward -n voting-app svc/vote 8080:80

# Scale deployment
kubectl scale deployment vote --replicas=5 -n voting-app

# Rollout status
kubectl rollout status deployment/vote -n voting-app

# Rollout history
kubectl rollout history deployment/vote -n voting-app

# Restart deployment
kubectl rollout restart deployment/vote -n voting-app

# Describe resources
kubectl describe pod -n voting-app
kubectl describe svc vote -n voting-app
kubectl get endpoints -n voting-app
```

### Troubleshooting

**Pod not starting?**
```bash
kubectl describe pod <pod-name> -n voting-app
kubectl logs <pod-name> -n voting-app
kubectl get events -n voting-app --sort-by=.metadata.creationTimestamp
```

**Service not accessible?**
```bash
kubectl get endpoints vote -n voting-app
kubectl describe svc vote -n voting-app
```

**Database connection issues?**
```bash
kubectl exec -it -n voting-app deployment/worker -- nslookup db
kubectl exec -it -n voting-app deployment/worker -- nc -zv db 5432
```

**Check ConfigMaps and Secrets:**
```bash
kubectl get configmap -n voting-app
kubectl get secret -n voting-app
kubectl describe configmap vote-config -n voting-app
```

---

### Option 2: RSVP App

**Docker Images:**
- Frontend: `teamcloudyuga/rsvpapp`
- Database: `mongo:4.4`

**Service DNS:**
- Frontend: `rsvp`
- Database: `mongodb`

**Ports:**
- Frontend: 5000
- MongoDB: 27017

**Environment Variable:**
```yaml
env:
  - name: MONGODB_HOST
    value: mongodb
```

---

### Option 3: Guestbook App

**Docker Images:**
- Frontend: `gcr.io/google-samples/gb-frontend:v5`
- Redis Leader: `redis:6.0`
- Redis Follower: `redis:6.0`

**Service DNS:**
- Frontend: `frontend`
- Redis Leader: `redis-leader`
- Redis Follower: `redis-follower`

**Ports:**
- Frontend: 80
- Redis: 6379

---
