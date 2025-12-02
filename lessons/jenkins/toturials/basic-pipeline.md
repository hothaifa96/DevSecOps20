# Jenkins Pipeline Basics

## What is a Jenkins Pipeline?

A Jenkins Pipeline is a suite of plugins that supports implementing and integrating continuous delivery pipelines into Jenkins. It provides an extensible set of tools for modeling simple-to-complex delivery pipelines "as code."

## Why Pipeline as Code?

### Traditional Jenkins (Freestyle Jobs)

In the old approach, Jenkins jobs were configured through the web UI:

- Click buttons to add build steps
- Configure options in forms
- Settings stored in Jenkins internal XML
- No version control
- Hard to replicate or review

### Pipeline as Code Benefits

| Benefit | Description |
|---------|-------------|
| Version Controlled | Pipeline lives in your Git repository |
| Code Review | Changes go through pull requests |
| Audit Trail | Git history shows who changed what |
| Reproducible | Same pipeline runs the same way everywhere |
| Shareable | Teams can share and reuse pipeline patterns |
| Testable | Pipeline logic can be validated before running |

## Pipeline Types

### Declarative Pipeline

The newer, simpler syntax. Think of it as filling out a structured form.

**Characteristics:**
- Strict, predefined structure
- Easier to read and write
- Built-in error checking
- Recommended for most use cases
- Must start with `pipeline { }` block

**Structure Overview:**
```
pipeline {
    agent (where to run)
    stages {
        stage (what to do)
        stage (next thing)
    }
    post (cleanup actions)
}
```

### Scripted Pipeline

The original, more flexible syntax. Think of it as writing a program.

**Characteristics:**
- Full Groovy programming language
- Maximum flexibility
- Steeper learning curve
- Harder to read
- Must start with `node { }` block

**When to Use Scripted:**
- Complex conditional logic
- Dynamic stage generation
- Advanced looping requirements
- Migration from older Jenkins versions

## Core Pipeline Concepts

### 1. Agent

**What it is:** Defines WHERE the pipeline or stage runs.

**Options:**
| Agent Type | Description |
|------------|-------------|
| `any` | Run on any available agent |
| `none` | Don't allocate globally; each stage chooses |
| `label` | Run on agent with specific label |
| `docker` | Run inside a Docker container |
| `kubernetes` | Run in a Kubernetes pod |

**Key Points:**
- Every pipeline needs an agent (or `none` at top with agents per stage)
- Agent determines the workspace location
- Different stages can use different agents

### 2. Stages

**What it is:** A logical grouping of steps that represents a phase of your pipeline.

**Common Stage Names:**
- Checkout
- Build
- Test
- Static Analysis
- Security Scan
- Package
- Deploy to Dev
- Integration Tests
- Deploy to Staging
- Deploy to Production

**Key Points:**
- Stages appear in Jenkins UI as columns
- Each stage shows pass/fail status
- Stages run sequentially by default
- Stage names should be meaningful

### 3. Steps

**What it is:** The actual work that happens inside a stage.

**Common Step Types:**
| Step | Purpose |
|------|---------|
| `sh` | Run shell command (Linux/Mac) |
| `bat` | Run batch command (Windows) |
| `echo` | Print message to console |
| `checkout` | Get code from version control |
| `git` | Clone a Git repository |
| `archiveArtifacts` | Save build outputs |
| `junit` | Publish test results |
| `mail` | Send email notification |

### 4. Post Actions

**What it is:** Actions that run after stages complete, based on the outcome.

**Conditions:**
| Condition | When it Runs |
|-----------|--------------|
| `always` | Every time, regardless of status |
| `success` | Only if pipeline succeeded |
| `failure` | Only if pipeline failed |
| `unstable` | If marked unstable (e.g., test failures) |
| `changed` | If status changed from last build |
| `aborted` | If build was manually aborted |
| `cleanup` | Always runs, even after other post conditions |

**Common Uses:**
- Send notifications
- Clean up resources
- Archive artifacts
- Update external systems

## Pipeline File Location

### Jenkinsfile

The standard name for your pipeline file is `Jenkinsfile` (no extension).

**Location Options:**

| Location | Description |
|----------|-------------|
| Repository Root | Most common, easy to find |
| Subdirectory | For monorepos with multiple pipelines |
| Different Branch | Different pipelines per branch |
| Jenkins Server | Stored in Jenkins (not recommended) |

### Multi-branch Pipelines

Jenkins can automatically:
- Discover branches in your repository
- Create a job for each branch with a Jenkinsfile
- Run pipelines on pull requests
- Clean up jobs when branches are deleted

## Pipeline Execution Flow

```
┌─────────────────────────────────────────────────────────┐
│                    Pipeline Start                        │
└─────────────────────┬───────────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────────────┐
│                  Allocate Agent                          │
│            (Find matching executor)                      │
└─────────────────────┬───────────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────────────┐
│                  Stage: Build                            │
│              (Run steps in order)                        │
└─────────────────────┬───────────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────────────┐
│                  Stage: Test                             │
│              (Run steps in order)                        │
└─────────────────────┬───────────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────────────┐
│                  Stage: Deploy                           │
│              (Run steps in order)                        │
└─────────────────────┬───────────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────────────┐
│                  Post Actions                            │
│         (Based on success/failure/always)                │
└─────────────────────┬───────────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────────────┐
│                   Pipeline End                           │
│              (Release agent/workspace)                   │
└─────────────────────────────────────────────────────────┘
```

## Build Status

| Status | Meaning | Color |
|--------|---------|-------|
| Success | All stages passed | Blue/Green |
| Unstable | Passed but with warnings | Yellow |
| Failure | A stage failed | Red |
| Aborted | Manually stopped | Gray |
| Not Built | Never ran or skipped | Gray |

## Workspace

**What it is:** A directory on the agent where your pipeline runs.

**Key Points:**
- Each job gets its own workspace
- Contains checked-out code
- Build outputs created here
- Can persist between builds (be careful!)
- Path: typically `/var/jenkins_home/workspace/job-name`

**Workspace Management:**
- Use `cleanWs()` to clean workspace
- Be careful with large artifacts
- Consider cleaning before/after builds

## Jenkins UI Elements

### Blue Ocean

Modern UI for pipelines:
- Visual pipeline editor
- Better visualization of stages
- Improved log viewing
- GitHub/Bitbucket integration

### Classic UI

Traditional Jenkins interface:
- More configuration options
- Full access to all features
- Console output view
- Build history

## Best Practices Summary

| Practice | Reason |
|----------|--------|
| Keep pipelines in source control | Version history, code review |
| Use meaningful stage names | Clarity in UI and logs |
| Fail fast | Put quick checks early |
| Clean workspace when needed | Avoid stale file issues |
| Use declarative when possible | Simpler, more maintainable |
| Keep pipelines focused | One purpose per pipeline |
| Add timeouts | Prevent hung builds |
| Archive important artifacts | Preserve build outputs |

