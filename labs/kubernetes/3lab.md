# Kubernetes CKA Lab Exercises

## Prerequisites
- A working Kubernetes cluster (minikube, kind, or multi-node cluster)
- kubectl configured and working
- Basic understanding of Kubernetes objects and YAML

---

### Exercise A: Multi-Container Pod with Shared Volume

**Requirements**:
- Create a namespace called `webapp-space`
- Deploy a pod named `web-logger` with two containers:
  - Container 1: `nginx` (image: `nginx:alpine`)
    - Should serve content from `/usr/share/nginx/html`
    - Expose port 80
  - Container 2: `logger` (image: `busybox`)
    - Should run command: 
    ```yaml
    volumeMounts:
        - name: *******
          mountPath: *****
        - name: *******
          mountPath: *****
    command:
        - sh
        - -c
        - |
          echo "<html><body><h1>Server Log</h1><pre>" > /usr/share/nginx/html/status.html;
          while true; do
            echo "$(date) CPU: $(top -bn1 | grep 'CPU' | awk '{print $2$3$4$5$6$7$8$9}')" >> /usr/share/nginx/html/status.html;
            echo "Requests: $(wc -l /var/log/nginx/access.log 2>/dev/null | awk '{print $1}')" >> /usr/share/nginx/html/status.html;
            echo "<br>" >> /usr/share/nginx/html/status.html;
            sleep 10;
          done
    ```
    - Mount a shared volume to `/logs` and `/usr/share/nginx/html`
- Both containers should share an `emptyDir` volume
- The nginx container should mount this volume at `/usr/share/nginx/html`
- Add appropriate resource limits: CPU: 100m, Memory: 128Mi for both containers
- Label the pod with `app=web-logger` and `tier=frontend`

**Verification**:
- Pod should be running with both containers healthy
- You should be able access the status.html and see it changes every 10 seconds

---

### Exercise B: Static Pod Configuration

**Requirements**:
- SSH into your worker node (or use your master node if single-node cluster)
- Create a static pod manifest named `static-web` with:
  - Image: `nginx:alpine`
  - Resource limits: CPU: 100m, Memory: 128Mi
  - Mount host path `/var/log` to container path `/host-logs` (readOnly)
  - Add labels: `type=static`, `app=webserver`
  - Container port: 80
- Place the manifest in the correct static pod directory
- Modify kubelet configuration if necessary to recognize static pods


---

### Exercise C: Dynamic Volume Provisioning with StorageClass
**Objective**: Configure dynamic storage provisioning using StorageClass.

**Requirements**:
- Create a new StorageClass named `fast-storage` with:
  - Provisioner: Use your cluster's available provisioner (e.g., `k8s.io/minikube-hostpath` for minikube)
  - Parameters: `type: fast`
  - ReclaimPolicy: `Retain`
  - VolumeBindingMode: `WaitForFirstConsumer`
  - AllowVolumeExpansion: true
- Create a PVC named `fast-claim` that:
  - Requests 1Gi of storage
  - Uses the `fast-storage` StorageClass
  - AccessMode: ReadWriteOnce
- Deploy a pod named `storage-test` that:
  - Uses image `nginx:alpine`
  - Mounts the PVC at `/usr/share/nginx/html`
  - Creates an index.html file in the mounted volume
- Expand the PVC to 2Gi (if supported by your provisioner)

---

### Exercise D: Multi-Pod Shared Storage

**Requirements**:
- Create a StorageClass named `shared-storage` suitable for RWX access
- Create a PVC named `shared-data` with:
  - Size: 3Gi
  - AccessMode: ReadWriteMany (use ReadWriteOnce if RWX not available, and document the limitation)
  - StorageClass: `shared-storage`
- Deploy 3 pods (`writer-1`, `writer-2`, `reader-1`) that:
  - All mount the same PVC at `/shared-data`
  - Writers: Use `busybox`, write timestamps to files
  - Reader: Use `busybox`, continuously read and display files
- Implement a mechanism to prevent write conflicts
- Add node affinity rules to spread pods across nodes (if multi-node cluster)

---

### ETGAR ::: : PV Backup and Restore Strategy

**Requirements**:
- Create a namespace `backup-demo`
- Deploy a stateful application (e.g., PostgreSQL or WordPress) with:
  - PVC of 3Gi
  - Some sample data
- Create a CronJob named `backup-scheduler` that:
  - Runs every 6 hours
  - Creates point-in-time snapshots/backups
  - Stores backups in a separate PVC
  - Maintains only last 5 backups (rotation)
  - Logs backup status
- Create a restore Job that can:
  - List available backups
  - Restore from a specific backup
  - Verify data integrity after restore
- Test disaster recovery by:
  - Deleting the original PVC
  - Restoring from backup
  - Verifying application functionality

**Verification**:
- Automated backups run on schedule
- Restore process successfully recovers data
- Application functions normally after restore

---

## Additional Challenges

### Bonus Exercise 1: CSI Driver Implementation
- Research and document how to implement a CSI driver in your cluster
- Test with different volume capabilities
- Implement volume snapshots if supported

### Bonus Exercise 2: Storage Performance Testing
- Create a Job that benchmarks different StorageClasses
- Compare IOPS, throughput, and latency
- Generate a performance report

---