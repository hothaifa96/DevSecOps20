# Jenkins Credentials Guide

## Types of Credentials
- **Username and Password:** Common for DockerHub, Bitbucket, etc.
- **Secret Text:** API tokens (e.g., GitHub Personal Access Token).
- **Secret File:** Configuration files or `.env` files.
- **SSH Username with Private Key:** For SSH access to servers.

## Adding Credentials (UI)
1. Go to **Manage Jenkins** > **Credentials**.
2. Click on the **(global)** domain.
3. Click **Add Credentials**.
4. Select the **Kind**, enter an **ID** (used in scripts), and the secret value.

## Using Credentials in a Pipeline
```groovy
pipeline {
    agent any
    environment {
        // Method 1: Global Environment Variable
        DOCKER_HUB = credentials('docker-hub-id')
    }
    stages {
        stage('Login') {
            steps {
                // Method 2: Scope-limited block
                withCredentials([usernamePassword(credentialsId: 'my-id', 
                                 passwordVariable: 'PASS', 
                                 usernameVariable: 'USER')]) {
                    sh "echo Logging in as $USER"
                    // Jenkins masks $PASS in logs automatically
                }
            }
        }
    }
}