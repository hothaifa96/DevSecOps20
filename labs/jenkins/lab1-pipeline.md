# Jenkins Pipeline Exercises

## Exercise 1: Hello Pipeline

### Objective

Create your first Jenkins pipeline that prints messages to the console and demonstrates the basic pipeline structure.

### Requirements

Create a pipeline that:

1. Has three stages named:
   - "Start"
   - "Build"
   - "End"

2. In the "Start" stage:
   - Print a welcome message
   - Print the current date and time
   - Print a separator line (use dashes or equals signs)

3. In the "Build" stage:
   - Print "Building the application..."
   - Print the Jenkins build number (hint: it's a built-in variable)
   - Print the workspace path

4. In the "End" stage:
   - Print a completion message
   - Print "Pipeline finished successfully!"



Your pipeline needs:
- `pipeline { }` wrapper
- `agent any` to run on any available agent
- `stages { }` block containing your three stages


---

## Exercise 2: Parameterized Deployment

### Objective

Create a pipeline that accepts user input through parameters and changes its behavior based on those inputs.

### Requirements

Create a pipeline with the following parameters:

1. **ENVIRONMENT** (Choice parameter)
   - Options: dev, staging, production
   - Description: "Select target environment"

2. **VERSION** (String parameter)
   - Default: "1.0.0"
   - Description: "Version to deploy"

3. **RUN_TESTS** (Boolean parameter)
   - Default: true
   - Description: "Run tests before deployment?"

4. **NOTIFY_TEAM** (Boolean parameter)
   - Default: false
   - Description: "Send notification to team?"

Create stages that:

1. **"Print Parameters"** stage:
   - Print all parameter values
   - Print a summary like "Deploying version X to Y environment"

2. **"Run Tests"** stage:
   - Only execute if RUN_TESTS is true
   - Print "Running test suite..."
   - Print "All tests passed!"

3. **"Deploy"** stage:
   - Print different messages based on ENVIRONMENT:
     - dev: "Deploying to development server..."
     - staging: "Deploying to staging server..."
     - production: "Deploying to PRODUCTION server - be careful!"
   - Print the version being deployed

4. **"Notify"** stage:
   - Only execute if NOTIFY_TEAM is true
   - Print "Sending notification to team..."
   - Print "Team notified about deployment of version X to Y"

## Exercise 3: Environment Configuration

### Objective

Create a pipeline that uses environment variables effectively, demonstrating global variables, stage-specific variables, credential handling, and computed values.

### Requirements

1. **Global Environment Variables:**
   Define these at the pipeline level:
   - APP_NAME = "my-awesome-app"
   - COMPANY = "TechCorp"
   - BUILD_TIMESTAMP = current timestamp (computed)

2. **Parameters:**
   - ENVIRONMENT (choice): dev, staging, prod
   - DEBUG_MODE (boolean): default false

3. **Stage: "Setup"**
   - Print all global environment variables
   - Print built-in Jenkins variables:
     - BUILD_NUMBER
     - JOB_NAME
     - WORKSPACE
     - NODE_NAME

4. **Stage: "Configure"**
   Define stage-specific environment variables based on ENVIRONMENT parameter:
   
   | Variable | dev | staging | prod |
   |----------|-----|---------|------|
   | API_URL | http://localhost:8080 | https://staging-api.com | https://api.company.com |
   | LOG_LEVEL | DEBUG | INFO | WARN |
   | REPLICAS | 1 | 2 | 5 |
   
   Print all configuration values.

5. **Stage: "Build Info"**
   Create and print computed variables:
   - FULL_APP_NAME = "{COMPANY}-{APP_NAME}"
   - BUILD_TAG = "{APP_NAME}-{VERSION}-{BUILD_NUMBER}"
   - DEPLOY_PATH = "/opt/{ENVIRONMENT}/{APP_NAME}"

6. **Stage: "Debug"** (conditional)
   - Only run if DEBUG_MODE is true
   - Print ALL environment variables (use `printenv` or `env` command)

7. **Post Section:**
   - Always print the BUILD_TAG
   - On success, print the DEPLOY_PATH


## Exercise 4: Complete CI/CD Simulation

### Objective

Combine everything you've learned to create a realistic CI/CD pipeline that simulates building, testing, and deploying an application.

### Requirements

This is a comprehensive exercise. Your pipeline should simulate a complete workflow:

### Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| ENVIRONMENT | choice | - | dev, staging, production |
| VERSION | string | 1.0.0 | Application version |
| SKIP_TESTS | boolean | false | Skip test execution |
| CLEAN_BUILD | boolean | true | Clean workspace before build |
| DEPLOY_APPROVAL | boolean | false | Require deployment approval |

### Environment Variables

**Global:**
- APP_NAME
- TEAM_NAME
- BUILD_TIMESTAMP

**Computed:**
- ARTIFACT_NAME = "{APP_NAME}-{VERSION}.tar.gz"
- DEPLOY_URL (based on environment)

### Stages

1. **"Initialization"**
   - Print pipeline banner (ASCII art or formatted header)
   - Print all parameters
   - Print build information (number, timestamp, node)
   - If CLEAN_BUILD is true, print "Cleaning workspace..."

2. **"Checkout"**
   - Print "Checking out source code..."
   - Print simulated git information:
     - Branch: main
     - Commit: abc123 (simulated)
   - Print "Checkout complete"

3. **"Build"**
   - Print build start message
   - Print 3-5 simulated build steps with slight delays:
     - "Compiling source files..."
     - "Processing resources..."
     - "Creating artifact..."
   - Print the ARTIFACT_NAME that would be created
   - Print build completion message

4. **"Test"** (conditional: skip if SKIP_TESTS is true)
   - Print "Running test suite..."
   - Simulate test execution:
     - "Unit tests: 45 passed, 0 failed"
     - "Integration tests: 12 passed, 0 failed"
     - "Code coverage: 87%"
   - Print test summary

5. **"Security Scan"**
   - Print "Running security scan..."
   - Simulate scan results:
     - "Dependencies scanned: 127"
     - "Vulnerabilities found: 0 critical, 2 medium, 5 low"
   - Print scan completion

6. **"Approval"** (conditional: only if DEPLOY_APPROVAL is true AND ENVIRONMENT is production)
   - Print warning about production deployment
   - Print "Waiting for approval..."
   - Use `input` step to pause for approval
   - Print "Deployment approved by user"

7. **"Deploy"**
   - Print environment-specific deployment message
   - Print deployment steps:
     - "Uploading artifact..."
     - "Updating configuration..."
     - "Restarting services..."
   - Print the DEPLOY_URL
   - Print deployment success message

8. **"Smoke Test"**
   - Print "Running smoke tests..."
   - Print "Health check: PASSED"
   - Print "API response: 200 OK"


