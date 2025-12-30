# 🔐 Jenkins Credentials Management

Jenkins allows you to store secrets securely so they aren't hardcoded in your `Jenkinsfile`.

## 1. Supported Types
| Type | Use Case |
| :--- | :--- |
| **Secret text** | API tokens, GitHub Personal Access Tokens. |
| **Username & Password** | DockerHub login, Database credentials. |
| **Secret file** | `.kube/config` files, `.env` files, or SSL certificates. |
| **SSH Username with private key** | Securely connecting to remote servers. |

## 2. How to Add Credentials
1. Navigate to **Manage Jenkins** > **Credentials**.
2. Click **(global)** under the Stores scope.
3. Click **Add Credentials** on the left sidebar.
4. Select the **Kind**, give it a unique **ID** (this is what you use in code), and fill in the secret.

## 3. Implementation in Pipeline
Using the `withCredentials` wrapper ensures secrets are masked (shown as `****`) in the logs.

```groovy
pipeline {
    agent any
    stages {
        stage('Example Secret') {
            steps {
                // For Secret Text
                withCredentials([string(credentialsId: 'my-api-token', variable: 'TOKEN')]) {
                    sh 'curl -H "Authorization: Bearer $TOKEN" [https://api.service.com](https://api.service.com)'
                }

                // For Username and Password
                withCredentials([usernamePassword(credentialsId: 'docker-hub', 
                                 passwordVariable: 'PASS', 
                                 usernameVariable: 'USER')]) {
                    sh "docker login -u $USER -p $PASS"
                }
            }
        }
    }
}