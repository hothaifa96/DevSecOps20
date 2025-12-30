# Jenkins Kubernetes Pod Agents

To use this, you must have the **Kubernetes Plugin** installed and configured in "Manage Jenkins > Clouds".

## Multi-Container Pod Template
This template uses an `ubuntu` container for shell scripts and a `maven` container for builds.

```groovy
pipeline {
    agent {
        kubernetes {
            yaml '''
apiVersion: v1
kind: Pod
spec:
  containers:
  - name: shell
    image: ubuntu
    command: ["sleep"]
    args: ["infinity"]
  - name: maven
    image: maven:3.8.1-jdk-11
    command: ["sleep"]
    args: ["infinity"]
'''
        }
    }
    stages {
        stage('Shell Work') {
            steps {
                container('shell') {
                    sh 'hostname'
                    sh 'uptime'
                }
            }
        }
        stage('Build Java') {
            steps {
                container('maven') {
                    sh 'mvn --version'
                }
            }
        }
    }
}