# 🔐 Jenkins Pipeline Guide

A Jenkins Pipeline is a suite of plugins that supports implementing and integrating continuous delivery pipelines into Jenkins.

## 📋 Pipeline Types

### 1. Declarative Pipeline (Recommended)

```groovy
pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                echo 'Building..'
                sh 'mvn clean package'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
                sh 'mvn test'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
                sh 'scp target/*.jar user@server:/path/'
            }
        }
    }
}
```

### 2. Scripted Pipeline

```groovy
node {
    stage('Build') {
        echo 'Building..'
        sh 'mvn clean package'
    }
    stage('Test') {
        echo 'Testing..'
        sh 'mvn test'
    }
    stage('Deploy') {
        echo 'Deploying....'
        sh 'scp target/*.jar user@server:/path/'
    }
}
```

## 🏗️ Pipeline Components

### Agent

Specifies where the entire Pipeline will execute:

```groovy
agent any                    // Any available agent
agent none                   // No global agent, each stage needs its own
agent { label 'linux' }     // Specific agent with label
agent { docker 'maven:3' }  // Docker container
```

### Stages

Contains a sequence of one or more stage directives:

```groovy
stages {
    stage('Build') {
        steps {
            echo 'Building application'
        }
    }
    stage('Test') {
        steps {
            echo 'Running tests'
        }
    }
}
```

### Steps

The actual work to be performed:

```groovy
steps {
    sh 'echo "Hello World"'        // Shell command
    echo 'Hello from Groovy'       // Groovy command
    script {                       // Complex Groovy script
        def message = "Dynamic message"
        echo message
    }
}
```

## 🔧 Advanced Features

### Environment Variables

```groovy
pipeline {
    agent any
    environment {
        CC = 'clang'
        CXX = 'clang++'
        CFLAGS = '-O2 -Wall'
    }
    stages {
        stage('Build') {
            steps {
                sh 'printenv'
                sh "echo $CC"
            }
        }
    }
}
```

### Parameters

```groovy
pipeline {
    agent any
    parameters {
        string(name: 'PERSON', defaultValue: 'Mr Jenkins', description: 'Who should I say hello to?')
        booleanParam(name: 'TOGGLE', defaultValue: true, description: 'Toggle this value')
        choice(name: 'CHOICE', choices: ['one', 'two', 'three'], description: 'Pick something')
    }
    stages {
        stage('Parameters') {
            steps {
                echo "Hello ${params.PERSON}"
                echo "Toggle: ${params.TOGGLE}"
                echo "Choice: ${params.CHOICE}"
            }
        }
    }
}
```

### Triggers

```groovy
pipeline {
    agent any
    triggers {
        cron('H */4 * * 1-5')  // Every 4 hours on weekdays
        pollSCM('H */2 * * 1-5') // Poll SCM every 2 hours
    }
    stages {
        stage('Build') {
            steps {
                echo 'Building on schedule or SCM change'
            }
        }
    }
}
```

### Post Actions

```groovy
pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'mvn clean package'
            }
        }
    }
    post {
        always {
            echo 'This will always run'
            cleanWs()  // Clean workspace
        }
        success {
            echo 'This will run only if successful'
            mail to: 'team@example.com',
                 subject: "Success: ${env.JOB_NAME}",
                 body: "Build succeeded in ${env.JOB_NAME}"
        }
        failure {
            echo 'This will run only if failed'
            mail to: 'team@example.com',
                 subject: "Failed: ${env.JOB_NAME}",
                 body: "Build failed in ${env.JOB_NAME}"
        }
        unstable {
            echo 'This will run only if the run was marked as unstable'
        }
        changed {
            echo 'This will run only if the state of the Pipeline has changed'
        }
    }
}
```

## 🐳 Docker Pipeline

### Using Docker Agents

```groovy
pipeline {
    agent {
        docker {
            image 'maven:3.8.4-openjdk-11'
            args '-v /root/.m2:/root/.m2'
        }
    }
    stages {
        stage('Build') {
            steps {
                sh 'mvn -B -DskipTests clean package'
            }
        }
        stage('Test') {
            steps {
                sh 'mvn test'
            }
        }
    }
}
```

### Multi-Stage Docker Build

```groovy
pipeline {
    agent any
    stages {
        stage('Build Docker Image') {
            steps {
                script {
                    def app = docker.build('my-app:${env.BUILD_NUMBER}')
                    app.push()
                    app.push('latest')
                }
            }
        }
        stage('Deploy to Kubernetes') {
            steps {
                sh 'kubectl apply -f k8s/'
            }
        }
    }
}
```

## 🔍 Parallel Execution

```groovy
pipeline {
    agent any
    stages {
        stage('Parallel Tests') {
            parallel {
                stage('Unit Tests') {
                    steps {
                        sh 'mvn test'
                    }
                }
                stage('Integration Tests') {
                    steps {
                        sh 'mvn verify -P integration-tests'
                    }
                }
                stage('Security Scan') {
                    steps {
                        sh 'security-scan.sh'
                    }
                }
            }
        }
    }
}
```

## 📁 File Operations

```groovy
pipeline {
    agent any
    stages {
        stage('File Operations') {
            steps {
                // Archive artifacts
                archiveArtifacts artifacts: 'target/*.jar', fingerprint: true

                // Archive test results
                junit 'target/surefire-reports/*.xml'

                // Stash files for later use
                stash includes: 'target/*.jar', name: 'app-jar'

                // Unstash files
                unstash 'app-jar'

                // Read file content
                def content = readFile 'config.properties'
                echo "Config: ${content}"

                // Write to file
                writeFile file: 'output.txt', text: 'Build completed successfully'
            }
        }
    }
}
```

## 🔄 Conditional Execution

```groovy
pipeline {
    agent any
    stages {
        stage('Conditional Build') {
            steps {
                script {
                    if (env.BRANCH_NAME == 'main') {
                        echo 'Building main branch - full pipeline'
                        sh 'mvn clean deploy'
                    } else if (env.BRANCH_NAME.startsWith('feature/')) {
                        echo 'Building feature branch - test only'
                        sh 'mvn clean test'
                    } else {
                        echo 'Other branch - minimal build'
                        sh 'mvn compile'
                    }
                }
            }
        }
    }
}
```

## 📊 Best Practices

1. **Use Declarative Pipeline** for better readability and maintainability
2. **Keep pipelines simple** - complex logic should be in shared libraries
3. **Use proper error handling** with try-catch blocks
4. **Archive important artifacts** for traceability
5. **Use credentials management** instead of hardcoding secrets
6. **Implement proper cleanup** in post sections
7. **Use parallel stages** for faster builds
8. **Parameterize pipelines** for reusability

## 🚀 Example Complete Pipeline

```groovy
pipeline {
    agent any
    parameters {
        string(name: 'BRANCH', defaultValue: 'main', description: 'Git branch to build')
        choice(name: 'ENVIRONMENT', choices: ['dev', 'staging', 'prod'], description: 'Target environment')
    }

    environment {
        APP_NAME = 'my-application'
        DOCKER_REGISTRY = 'my-registry.com'
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: params.BRANCH, url: 'https://github.com/myorg/myapp.git'
            }
        }

        stage('Build') {
            steps {
                sh 'mvn clean package -DskipTests'
            }
        }

        stage('Test') {
            parallel {
                stage('Unit Tests') {
                    steps {
                        sh 'mvn test'
                    }
                    post {
                        always {
                            junit 'target/surefire-reports/*.xml'
                        }
                    }
                }
                stage('Code Analysis') {
                    steps {
                        sh 'mvn sonar:sonar'
                    }
                }
            }
        }

        stage('Build Image') {
            steps {
                script {
                    def image = docker.build("${DOCKER_REGISTRY}/${APP_NAME}:${BUILD_NUMBER}")
                    image.push()
                    if (params.ENVIRONMENT == 'prod') {
                        image.push('latest')
                    }
                }
            }
        }

        stage('Deploy') {
            when {
                branch 'main'
            }
            steps {
                sh "kubectl apply -f k8s/${params.ENVIRONMENT}/"
                sh "kubectl set image deployment/${APP_NAME} ${APP_NAME}=${DOCKER_REGISTRY}/${APP_NAME}:${BUILD_NUMBER} -n ${params.ENVIRONMENT}"
            }
        }
    }

    post {
        always {
            cleanWs()
        }
        success {
            slackSend(
                channel: '#deployments',
                color: 'good',
                message: "✅ ${APP_NAME} deployed to ${params.ENVIRONMENT}"
            )
        }
        failure {
            slackSend(
                channel: '#deployments',
                color: 'danger',
                message: "❌ ${APP_NAME} deployment failed"
            )
        }
    }
}
```

This comprehensive pipeline demonstrates modern CI/CD practices with Jenkins, including multi-stage builds, parallel execution, Docker integration, and Kubernetes deployment.
