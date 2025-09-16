# GitHub & Git Integration

## Table of Contents
1. [Authentication Setup](#authentication-setup)
2. [Cloning Repositories](#cloning-repositories)
3. [Remote Management](#remote-management)
4. [Fetching and Pulling](#fetching-and-pulling)
5. [Pushing Changes](#pushing-changes)
6. [Pull Requests Workflow](#pull-requests-workflow)
7. [GitHub CLI Integration](#github-cli-integration)
8. [Credential Caching](#credential-caching)
9. [Advanced GitHub Integration](#advanced-github-integration)
10. [Troubleshooting Guide](#troubleshooting-guide)
11. [GitHub Git Cheat Sheet](#github-git-cheat-sheet)

---

## Authentication Setup

Before working with GitHub repositories, you need proper authentication. GitHub supports multiple authentication methods.

### 1. Personal Access Tokens (Recommended)

#### Creating a Personal Access Token

1. Go to GitHub.com → Settings → Developer settings → Personal access tokens → Tokens (classic)
2. Click "Generate new token (classic)"
3. Select scopes based on your needs:

| Scope | Purpose | DevOps Use Case |
|-------|---------|-----------------|
| `repo` | Full repository access | Private repos, all operations |
| `public_repo` | Public repositories only | Open source contributions |
| `workflow` | GitHub Actions | CI/CD pipeline management |
| `write:packages` | Package registry | Docker/NPM package publishing |
| `read:org` | Organization access | Team repository access |
| `admin:repo_hook` | Repository webhooks | Deployment automation |

#### Using Personal Access Tokens

```bash
# Method 1: HTTPS with token (will prompt for password - enter token)
git clone https://github.com/username/repository.git

# Method 2: Include token in URL (less secure)
git clone https://token@github.com/username/repository.git

# Method 3: Set token as environment variable
export GITHUB_TOKEN="ghp_xxxxxxxxxxxxxxxxxxxx"
git clone https://github.com/username/repository.git
```

### 2. SSH Keys Setup

#### Generate SSH Key

```bash
# Generate new SSH key
ssh-keygen -t ed25519 -C "your.email@example.com"
# Or for older systems:
ssh-keygen -t rsa -b 4096 -C "your.email@example.com"

# Start SSH agent
eval "$(ssh-agent -s)"

# Add SSH key to agent
ssh-add ~/.ssh/id_ed25519
```

#### Add SSH Key to GitHub

```bash
# Copy public key to clipboard
cat ~/.ssh/id_ed25519.pub | pbcopy  # macOS
cat ~/.ssh/id_ed25519.pub | xclip -selection clipboard  # Linux
```

1. Go to GitHub.com → Settings → SSH and GPG keys
2. Click "New SSH key"
3. Paste your public key

#### Test SSH Connection

```bash
# Test SSH connection
ssh -T git@github.com
# Should return: "Hi username! You've successfully authenticated..."
```

### 3. GitHub CLI Authentication

```bash
# Install GitHub CLI
# macOS
brew install gh

# Ubuntu/Debian
curl -fsSL https://cli.github.com/packages/githubcli-archive-keyring.gpg | sudo dd of=/usr/share/keyrings/githubcli-archive-keyring.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | sudo tee /etc/apt/sources.list.d/github-cli.list > /dev/null
sudo apt update
sudo apt install gh

# Authenticate with GitHub
gh auth login
```

---

## Cloning Repositories

Cloning creates a local copy of a remote repository with full version history.

### Basic Cloning

```bash
# Clone with HTTPS
git clone https://github.com/username/repository.git

# Clone with SSH (recommended for frequent contributors)
git clone git@github.com:username/repository.git

# Clone to specific directory
git clone https://github.com/username/repository.git my-project

# Clone specific branch
git clone -b develop https://github.com/username/repository.git

# Shallow clone (recent commits only - faster)
git clone --depth 1 https://github.com/username/repository.git

# Clone with submodules
git clone --recurse-submodules https://github.com/username/repository.git
```

### Advanced Cloning Options

```bash
# Clone bare repository (no working directory)
git clone --bare https://github.com/username/repository.git

# Clone and set different remote name
git clone -o upstream https://github.com/username/repository.git

# Clone single branch only
git clone --single-branch --branch main https://github.com/username/repository.git

# Clone with different remote HEAD
git clone --branch develop https://github.com/username/repository.git
```

### Fork and Clone Workflow

```bash
# Using GitHub CLI to fork and clone
gh repo fork username/repository --clone

# Manual fork workflow
# 1. Fork on GitHub web interface
# 2. Clone your fork
git clone git@github.com:yourusername/repository.git
cd repository

# 3. Add upstream remote
git remote add upstream git@github.com:username/repository.git

# 4. Verify remotes
git remote -v
# origin    git@github.com:yourusername/repository.git (fetch)
# origin    git@github.com:yourusername/repository.git (push)
# upstream  git@github.com:username/repository.git (fetch)
# upstream  git@github.com:username/repository.git (push)
```

### Cloning Private Repositories

```bash
# With Personal Access Token
git clone https://token:x-oauth-basic@github.com/username/private-repo.git

# With SSH (recommended)
git clone git@github.com:username/private-repo.git

# Using GitHub CLI (handles auth automatically)
gh repo clone username/private-repo
```

---

## Remote Management

Managing multiple remotes is crucial for collaborative development and DevOps workflows.

### Viewing Remotes

```bash
# List all remotes
git remote

# List remotes with URLs
git remote -v

# Show detailed remote information
git remote show origin
git remote show upstream
```

### Adding Remotes

```bash
# Add upstream remote (for forks)
git remote add upstream https://github.com/original/repository.git

# Add remote with custom name
git remote add production git@github.com:company/prod-repo.git

# Add multiple remotes for different environments
git remote add staging git@github.com:company/staging-repo.git
git remote add development git@github.com:company/dev-repo.git
```

### Modifying Remotes

```bash
# Change remote URL
git remote set-url origin git@github.com:username/new-repository.git

# Change from HTTPS to SSH
git remote set-url origin git@github.com:username/repository.git

# Add additional URL for pushing to multiple remotes
git remote set-url --add --push origin git@github.com:username/mirror.git
git remote set-url --add --push origin git@github.com:username/repository.git
```

### Removing Remotes

```bash
# Remove a remote
git remote remove upstream
git remote rm upstream  # Same as above

# Rename a remote
git remote rename origin old-origin
```

### Multi-Remote Workflow

```bash
# Typical DevOps setup
git remote add origin git@github.com:company/main-repo.git        # Main repository
git remote add upstream git@github.com:opensource/project.git     # Upstream project
git remote add fork git@github.com:myusername/project.git         # Personal fork
git remote add staging git@github.com:company/staging.git         # Staging environment
git remote add production git@github.com:company/production.git   # Production environment

# View all remotes
git remote -v
```

### Remote Branches Management

```bash
# List all remote branches
git branch -r

# List all branches (local and remote)
git branch -a

# Track remote branch
git checkout --track origin/feature/new-feature
git checkout -b local-branch origin/remote-branch

# Push to specific remote
git push upstream main
git push origin feature/my-feature

# Delete remote branch
git push origin --delete feature/old-branch
git push origin :feature/old-branch  # Alternative syntax
```

---

## Fetching and Pulling

Understanding the difference between fetch and pull is crucial for safe collaborative development.

### Git Fetch vs Git Pull

| Command | Action | Safety | Use Case |
|---------|--------|--------|----------|
| `git fetch` | Downloads changes, doesn't merge | Safe | Review before merging |
| `git pull` | Downloads and merges automatically | Can cause conflicts | Quick updates |

### Git Fetch Operations

```bash
# Fetch from default remote (origin)
git fetch

# Fetch from specific remote
git fetch upstream
git fetch production

# Fetch all remotes
git fetch --all

# Fetch specific branch
git fetch origin main
git fetch upstream develop

# Fetch with pruning (remove deleted remote branches)
git fetch --prune
git fetch -p

# Fetch tags
git fetch --tags
git fetch origin --tags
```

### Reviewing Fetched Changes

```bash
# After fetching, review changes before merging
git fetch origin

# Compare current branch with remote
git diff HEAD origin/main
git diff main origin/main

# Show commits that are new on remote
git log HEAD..origin/main
git log --oneline HEAD..origin/main

# Show commits graphically
git log --graph --oneline --all

# Show what files changed
git diff --name-only HEAD origin/main
```

### Git Pull Operations

```bash
# Basic pull (fetch + merge)
git pull

# Pull from specific remote and branch
git pull origin main
git pull upstream develop

# Pull with rebase instead of merge
git pull --rebase
git pull --rebase origin main

# Pull all submodules
git pull --recurse-submodules

# Pull with specific merge strategy
git pull --strategy=ours origin main
```

### Advanced Pull Configurations

```bash
# Set default pull behavior globally
git config --global pull.rebase false  # merge (default)
git config --global pull.rebase true   # rebase
git config --global pull.ff only       # fast-forward only

# Set pull behavior for specific repository
git config pull.rebase true

# Set upstream for current branch
git branch --set-upstream-to=origin/main main
git push -u origin feature/new-branch  # Sets upstream when pushing
```

### Safe Update Workflow

```bash
# Recommended safe workflow
# 1. Fetch latest changes
git fetch origin

# 2. Check what's new
git log --oneline HEAD..origin/main

# 3. Check for conflicts before merging
git merge-tree $(git merge-base HEAD origin/main) HEAD origin/main

# 4. Merge if safe, or rebase for cleaner history
git merge origin/main
# OR
git rebase origin/main

# Alternative: Pull with verification
git pull --verify-signatures origin main
```

### Handling Fetch/Pull Conflicts

```bash
# When pull results in conflicts
git pull origin main
# Conflicts occur

# Option 1: Resolve conflicts manually
git status  # Shows conflicted files
# Edit files to resolve conflicts
git add resolved-file.js
git commit

# Option 2: Abort and try different approach
git merge --abort
git pull --rebase origin main

# Option 3: Use merge tool
git mergetool
git commit
```

### Fetch and Pull Workflow Diagram

```mermaid
graph TD
    A[Remote Repository] -->|git fetch| B[Local Repository]
    B -->|git merge/rebase| C[Working Directory]
    A -->|git pull| C
    
    D[git fetch origin] --> E{Review Changes}
    E -->|Safe| F[git merge origin/main]
    E -->|Conflicts Expected| G[git rebase origin/main]
    E -->|Complex Changes| H[Manual Merge Strategy]
    
    style A fill:#ffcccc
    style B fill:#ffffcc
    style C fill:#ccffcc
```

---

## Pushing Changes

Pushing uploads your local commits to remote repositories. This is crucial for sharing work and triggering CI/CD pipelines.

### Basic Push Operations

```bash
# Push current branch to origin
git push

# Push specific branch to origin
git push origin main
git push origin feature/new-api

# Push to specific remote
git push upstream main
git push production release/v1.2.0

# First push of new branch (set upstream)
git push -u origin feature/new-feature
git push --set-upstream origin feature/new-feature
```

### Advanced Push Options

```bash
# Force push (dangerous - use with caution)
git push --force origin feature/rebased-branch
git push -f origin feature/rebased-branch

# Safe force push (fails if remote has new commits)
git push --force-with-lease origin feature/my-branch

# Push all branches
git push origin --all

# Push tags
git push origin --tags
git push origin v1.0.0

# Push specific tag
git push origin tag-name

# Push to multiple remotes simultaneously
git push origin main && git push backup main
```

### Push Strategies and Configurations

```bash
# Configure default push behavior
git config --global push.default simple    # Push current branch to same name
git config --global push.default upstream  # Push to configured upstream
git config --global push.default current   # Push current branch to remote branch of same name
git config --global push.default matching  # Push all matching branches (old default)

# Configure push to automatically set upstream
git config --global push.autoSetupRemote true

# Configure push to follow tags
git config --global push.followTags true
```

### Handling Push Rejections

```bash
# When push is rejected (remote has newer commits)
git push origin main
# ! [rejected] main -> main (fetch first)

# Solution 1: Fetch and merge
git fetch origin
git merge origin/main
git push origin main

# Solution 2: Fetch and rebase (cleaner history)
git fetch origin
git rebase origin/main
git push origin main

# Solution 3: Pull (fetch + merge in one command)
git pull origin main
git push origin main

# Solution 4: Pull with rebase
git pull --rebase origin main
git push origin main
```

### DevOps Push Workflows

#### Feature Branch Workflow

```bash
# Create feature branch
git checkout -b feature/payment-integration

# Make changes and commits
git add .
git commit -m "feat(payment): add Stripe integration"

# Push feature branch
git push -u origin feature/payment-integration

# After code review and approval, merge to main
git checkout main
git pull origin main
git merge feature/payment-integration
git push origin main

# Clean up
git branch -d feature/payment-integration
git push origin --delete feature/payment-integration
```

#### Hotfix Workflow

```bash
# Create hotfix from main/production
git checkout main
git pull origin main
git checkout -b hotfix/security-patch

# Apply fix
git commit -am "fix(security): patch XSS vulnerability"

# Push hotfix
git push -u origin hotfix/security-patch

# Emergency merge to main
git checkout main
git merge hotfix/security-patch
git push origin main

# Also merge to develop if using Git Flow
git checkout develop
git merge hotfix/security-patch
git push origin develop
```

#### Release Workflow

```bash
# Create release branch
git checkout develop
git checkout -b release/v1.2.0

# Finalize release (version bumps, changelog, etc.)
git commit -am "chore(release): prepare v1.2.0"

# Push release branch
git push -u origin release/v1.2.0

# After testing, merge to main and tag
git checkout main
git merge release/v1.2.0
git tag -a v1.2.0 -m "Release version 1.2.0"
git push origin main
git push origin v1.2.0

# Merge back to develop
git checkout develop
git merge release/v1.2.0
git push origin develop
```

### Push Hooks and Automation

```bash
# Pre-push hook example (save as .git/hooks/pre-push)
#!/bin/sh
# Run tests before pushing
npm test
if [ $? -ne 0 ]; then
    echo "Tests failed. Push aborted."
    exit 1
fi

# Push with automatic testing
git config --global alias.safe-push '!git test && git push'

# Push and trigger deployment (using GitHub CLI)
git push origin main && gh workflow run deploy.yml
```

---

## Pull Requests Workflow

Pull Requests (PRs) are the cornerstone of collaborative development and code review in GitHub.

### Creating Pull Requests

#### Using GitHub Web Interface

1. Push your feature branch: `git push -u origin feature/new-feature`
2. Navigate to GitHub repository
3. Click "Compare & pull request" button
4. Fill in PR template

#### Using GitHub CLI

```bash
# Create PR from current branch
gh pr create --title "Add user authentication" --body "Implements JWT-based auth system"

# Create PR with template
gh pr create --template .github/pull_request_template.md

# Create draft PR
gh pr create --draft --title "WIP: Database optimization"

# Create PR targeting specific branch
gh pr create --base develop --title "Feature: New API endpoints"

# Create PR with reviewers and assignees
gh pr create --title "Bug fix" --reviewer @john,@jane --assignee @alice

# Create PR with labels
gh pr create --title "Security update" --label "security,urgent"
```

### Managing Pull Requests

```bash
# List PRs
gh pr list
gh pr list --state open
gh pr list --state closed
gh pr list --author @me

# View PR details
gh pr view 123
gh pr view --web 123  # Open in browser

# Check out PR locally for testing
gh pr checkout 123
git fetch origin pull/123/head:pr-123
git checkout pr-123

# Review PR
gh pr review 123 --approve
gh pr review 123 --request-changes --body "Please fix the security issue"
gh pr review 123 --comment --body "Looks good overall"

# Merge PR
gh pr merge 123
gh pr merge 123 --merge      # Create merge commit
gh pr merge 123 --squash     # Squash and merge
gh pr merge 123 --rebase     # Rebase and merge
```

### PR Templates and Automation

#### PR Template Example

Create `.github/pull_request_template.md`:

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix (non-breaking change which fixes an issue)
- [ ] New feature (non-breaking change which adds functionality)
- [ ] Breaking change (fix or feature that would cause existing functionality to not work as expected)
- [ ] Documentation update

## Testing
- [ ] Unit tests pass
- [ ] Integration tests pass
- [ ] Manual testing completed

## Checklist
- [ ] Code follows style guidelines
- [ ] Self-review completed
- [ ] Code is documented
- [ ] Tests added/updated
- [ ] No breaking changes without version bump

## Screenshots/Evidence
If applicable, add screenshots or evidence of testing

## Related Issues
Closes #123
```

#### Multiple PR Templates

Create `.github/PULL_REQUEST_TEMPLATE/` directory:

```bash
mkdir -p .github/PULL_REQUEST_TEMPLATE

# Feature template
cat > .github/PULL_REQUEST_TEMPLATE/feature.md << EOF
## Feature Description
What feature does this add?

## Implementation Details
How was this implemented?

## Testing
- [ ] Unit tests
- [ ] E2E tests
- [ ] Performance testing
EOF

# Bug fix template
cat > .github/PULL_REQUEST_TEMPLATE/bugfix.md << EOF
## Bug Description
What bug does this fix?

## Root Cause
What caused the bug?

## Fix Description
How is it fixed?

## Testing
- [ ] Bug reproduction test
- [ ] Regression tests
EOF
```

### Advanced PR Workflows

#### Auto-merge with Conditions

```bash
# Enable auto-merge when all checks pass
gh pr merge 123 --auto --squash

# Set up branch protection rules (via web interface or API)
gh api repos/:owner/:repo/branches/main/protection \
  --method PUT \
  --field required_status_checks='{"strict":true,"contexts":["ci/tests","ci/lint"]}' \
  --field enforce_admins=true \
  --field required_pull_request_reviews='{"required_approving_review_count":2}'
```

#### PR Status Checks

```bash
# View PR checks
gh pr checks 123

# Wait for checks to complete
gh pr checks 123 --watch

# Re-run failed checks (if you have permissions)
gh run rerun $(gh pr view 123 --json statusCheckRollup --jq '.statusCheckRollup[] | select(.status == "FAILED") | .workflowRun.id')
```

### PR Best Practices for DevOps

#### 1. Keep PRs Small and Focused

```bash
# Good: Single feature/fix
git checkout -b feature/add-logging
# Make focused changes
git commit -m "feat(logging): add structured logging with Winston"

# Bad: Multiple unrelated changes
git checkout -b feature/everything
# Multiple unrelated changes
git commit -m "Add logging, fix bugs, update deps, refactor auth"
```

#### 2. Use Conventional Commits

```bash
# Types: feat, fix, docs, style, refactor, test, chore, ci
git commit -m "feat(auth): implement OAuth2 integration"
git commit -m "fix(api): resolve rate limiting bug"
git commit -m "docs(readme): update installation instructions"
git commit -m "ci(github): add automated security scanning"
```

#### 3. Link PRs to Issues

```bash
# In PR description, use keywords to auto-close issues
gh pr create --body "
Fixes #123
Closes #456
Resolves #789

This PR implements the user authentication system as requested.
"
```

#### 4. Request Appropriate Reviews

```bash
# Request reviews from code owners
gh pr create --reviewer @team/backend,@security-team

# Request reviews based on files changed
gh pr create --reviewer $(git diff --name-only main | xargs -I {} gh api repos/:owner/:repo/contents/{} --jq '.owner.login' | sort -u | tr '\n' ',')
```

---

## GitHub CLI Integration

GitHub CLI (gh) provides powerful integration between your terminal and GitHub.

### Installation and Setup

```bash
# macOS
brew install gh

# Ubuntu/Debian
curl -fsSL https://cli.github.com/packages/githubcli-archive-keyring.gpg | sudo dd of=/usr/share/keyrings/githubcli-archive-keyring.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | sudo tee /etc/apt/sources.list.d/github-cli.list > /dev/null
sudo apt update && sudo apt install gh

# Login to GitHub
gh auth login
gh auth status
```

### Repository Operations

```bash
# Clone repository
gh repo clone username/repository

# Create new repository
gh repo create my-new-project --public
gh repo create my-new-project --private --clone

# Fork repository
gh repo fork username/repository --clone

# View repository info
gh repo view username/repository
gh repo view --web  # Open in browser

# Archive repository
gh repo archive username/repository

# Delete repository (be careful!)
gh repo delete username/repository
```

### Issue Management

```bash
# List issues
gh issue list
gh issue list --state open
gh issue list --assignee @me
gh issue list --label bug

# Create issue
gh issue create --title "Bug in authentication" --body "User login fails with 500 error"
gh issue create --template bug_report.md

# View issue
gh issue view 123
gh issue view 123 --web

# Close issue
gh issue close 123 --comment "Fixed in PR #456"

# Assign issue
gh issue edit 123 --add-assignee @username
gh issue edit 123 --add-label "priority:high,bug"
```

### Workflow and Actions

```bash
# List workflows
gh workflow list

# Run workflow
gh workflow run deploy.yml
gh workflow run "Deploy to Production"

# View workflow runs
gh run list
gh run list --workflow=deploy.yml

# View specific run
gh run view 123456
gh run view 123456 --log

# Watch workflow run
gh run watch 123456

# Re-run workflow
gh run rerun 123456
```

### Release Management

```bash
# Create release
gh release create v1.0.0 --title "Version 1.0.0" --notes "First stable release"
gh release create v1.0.0 dist/* --notes "Release with binaries"

# List releases
gh release list

# View release
gh release view v1.0.0

# Download release assets
gh release download v1.0.0
gh release download v1.0.0 --pattern "*.tar.gz"

# Delete release
gh release delete v1.0.0
```

### GitHub CLI Configuration

```bash
# Set default editor
gh config set editor code
gh config set editor vim

# Set default protocol
gh config set git_protocol ssh
gh config set git_protocol https

# View configuration
gh config list

# Set custom aliases
gh alias set pv 'pr view'
gh alias set co 'pr checkout'
gh alias set prs 'pr list --state open --author @me'
```

### Advanced GitHub CLI Usage

#### Bulk Operations

```bash
# Close multiple issues
gh issue list --state open --json number --jq '.[].number' | xargs -I {} gh issue close {}

# Add label to multiple PRs
gh pr list --json number --jq '.[].number' | xargs -I {} gh pr edit {} --add-label "needs-review"

# Approve multiple PRs (be careful!)
gh pr list --author trusted-contributor --json number --jq '.[].number' | xargs -I {} gh pr review {} --approve
```

#### Custom Scripts

```bash
#!/bin/bash
# Script: pr-stats.sh - Show PR statistics
echo "Open PRs: $(gh pr list --state open --json number --jq 'length')"
echo "Draft PRs: $(gh pr list --state open --draft --json number --jq 'length')"
echo "My PRs: $(gh pr list --author @me --json number --jq 'length')"
echo "PRs needing review: $(gh pr list --review-requested @me --json number --jq 'length')"
```

---

## Credential Caching

Proper credential management is essential for seamless GitHub integration and security.

### Git Credential Manager

#### Installation

```bash
# macOS (via Homebrew)
brew tap microsoft/git
brew install --cask git-credential-manager-core

# Ubuntu/Debian
curl -LO https://github.com/GitCredentialManager/git-credential-manager/releases/latest/download/gcm-linux_amd64.2.0.935.deb
sudo dpkg -i gcm-linux_amd64.2.0.935.deb

# Windows (via Winget)
winget install Microsoft.GitCredentialManager
```

#### Configuration

```bash
# Configure Git Credential Manager
git config --global credential.helper manager-core

# Set credential store (optional)
git config --global credential.credentialStore secretservice  # Linux
git config --global credential.credentialStore keychain       # macOS
git config --global credential.credentialStore wincredman     # Windows

# Configure for GitHub specifically
git config --global credential.https://github.com.provider github
```

### Personal Access Token Caching

#### Method 1: Environment Variables

```bash
# Add to ~/.bashrc, ~/.zshrc, or ~/.profile
export GITHUB_TOKEN="ghp_xxxxxxxxxxxxxxxxxxxx"
export GIT_ASKPASS="echo"
export GIT_USERNAME="your-username"

# Use in scripts
git clone https://$GITHUB_TOKEN@github.com/username/repo.git
```

#### Method 2: Git Configuration

```bash
# Store token in git config (less secure)
git config --global credential.helper store
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

# First clone will prompt for credentials, then store them
git clone https://github.com/username/private-repo.git
# Username: your-username
# Password: ghp_xxxxxxxxxxxxxxxxxxxx (your token)
```

#### Method 3: Secure Token Storage

```bash
# Using macOS Keychain
security add-generic-password -a "your-username" -s "github.com" -w "ghp_xxxxxxxxxxxxxxxxxxxx"

# Using Linux Secret Service
echo "ghp_xxxxxxxxxxxxxxxxxxxx" | secret-tool store --label="GitHub Token" service github username your-username

# Retrieve token in scripts
TOKEN=$(security find-generic-password -a "your-username" -s "github.com" -w)  # macOS
TOKEN=$(secret-tool lookup service github username your-username)              # Linux
```

### SSH Key Management

#### SSH Agent Configuration

```bash
# Start SSH agent automatically (add to ~/.bashrc or ~/.zshrc)
if [ -z "$SSH_AUTH_SOCK" ]; then
    eval "$(ssh-agent -s)"
    ssh-add ~/.ssh/id_ed25519
fi

# Or use keychain for persistent agent
# Install keychain: brew install keychain (macOS) or apt install keychain (Ubuntu)
eval "$(keychain --eval --agents ssh id_ed25519)"
```

#### Multiple SSH Keys

```bash
# Create SSH config file
cat > ~/.ssh/config << EOF
# Personal GitHub
Host github.com
    HostName github.com
    User git
    IdentityFile ~/.ssh/id_ed25519_personal
    IdentitiesOnly yes

# Work GitHub
Host github-work
    HostName github.com
    User git
    IdentityFile ~/.ssh/id_ed25519_work
    IdentitiesOnly yes

# GitHub Enterprise
Host github.company.com
    HostName github.company.com
    User git
    IdentityFile ~/.ssh/id_ed25519_company
    IdentitiesOnly yes
EOF

# Clone with specific SSH key
git clone git@github-work:company/private-repo.git
git clone git@github.company.com:enterprise/repo.git
```

### Credential Helpers Comparison

| Method | Security | Convenience | Cross-Platform | Use Case |
|--------|----------|-------------|----------------|----------|
| Git Credential Manager | High | High | Yes | Recommended for all users |
| SSH Keys | High | High | Yes | Power users, automation |
| Personal Access Token | Medium | Medium | Yes | Scripts, CI/CD |
| Keychain/Secret Service | High | High | No | OS-specific integration |
| Environment Variables | Low | High | Yes | Development only |

### Troubleshooting Credential Issues

#### Common Problems and Solutions

```bash
# Problem: "Authentication failed"
# Check credential helper
git config --global credential.helper

# Reset stored credentials
git config --global --unset credential.helper
# Or for specific host
git credential reject <<< "url=https://github.com"

# Problem: SSH connection failed
# Test SSH connection
ssh -T git@github.com
ssh -vT git@github.com  # Verbose output for debugging

# Check SSH key is loaded
ssh-add -l

# Problem: Token expired
# Generate new token and update
git config --global credential.helper manager-core
# Next operation will prompt for new token
```

#### Credential Debugging

```bash
# Enable credential debugging
git config --global credential.debug true

# Test credential helper
echo "protocol=https
host=github.com
username=your-username" | git credential fill

# Clear all cached credentials
git credential-manager-core erase <<< "url=https://github.com"

# View stored credentials (be careful with output!)
git config --global credential.helper store
cat ~/.git-credentials  # Only if using store helper
```

---

## Advanced GitHub Integration

### GitHub Actions Integration

#### Triggering Workflows from Git

```bash
# Trigger workflow on push
git push origin main  # Triggers workflows on push to main

# Create release to trigger deployment
git tag -a v1.0.0 -m "Release v1.0.0"
git push origin v1.0.0

# Trigger workflow manually
gh workflow run deploy.yml --ref main
gh workflow run deploy.yml -f environment=production -f version=1.2.3
```

#### Repository Dispatch Events

```bash
# Trigger custom workflow event
gh api repos/:owner/:repo/dispatches \
  --field event_type=deploy \
  --field client_payload='{"environment":"production","version":"1.2.3"}'

# Webhook-style trigger
curl -X POST \
  -H "Accept: application/vnd.github.v3+json" \
  -H "Authorization: token $GITHUB_TOKEN" \
  https://api.github.com/repos/owner/repo/dispatches \
  -d '{"event_type":"custom-event","client_payload":{"key":"value"}}'
```

### GitHub API Integration

#### Basic API Operations

```bash
# Get repository information
gh api repos/:owner/:repo

# List issues
gh api repos/:owner/:repo/issues

# Create issue via API
gh api repos/:owner/:repo/issues \
  --method POST \
  --field title="API Created Issue" \
  --field body="This issue was created via the GitHub API"

# Update pull request
gh api repos/:owner/:repo/pulls/123 \
  --method PATCH \
  --field title="Updated PR Title"
```

#### Advanced API Usage

```bash
# GraphQL queries
gh api graphql --field query='
query {
  repository(owner: "owner", name: "repo") {
    issues(first: 10, states: OPEN) {
      nodes {
        title
        number
        author {
          login
        }
      }
    }
  }
}'

# Bulk operations with API
for repo in $(gh repo list --json name --jq '.[].name'); do
  gh api repos/:owner/$repo/issues --method POST \
    --field title="Automated Issue" \
    --field body="This is an automated issue"
done
```

### Webhooks and Integration

#### Setting up Webhooks

```bash
# Create webhook
gh api repos/:owner/:repo/hooks \
  --method POST \
  --field name=web \
  --field config='{"url":"https://example.com/webhook","content_type":"json"}' \
  --field events='["push","pull_request"]'

# List webhooks
gh api repos/:owner/:repo/hooks

# Test webhook
gh api repos/:owner/:repo/hooks/123/tests --method POST
```

### GitHub Apps and OAuth

#### GitHub App Authentication

```bash
# Install GitHub CLI extension for apps
gh extension install github/gh-app

# Authenticate as GitHub App
export GITHUB_APP_ID="123456"
export GITHUB_APP_PRIVATE_KEY_PATH="/path/to/private-key.pem"
gh app auth --app-id $GITHUB_APP_ID --private-key $GITHUB_APP_PRIVATE_KEY_PATH
```

---

## Troubleshooting Guide

### Common Issues and Solutions

#### Authentication Issues

```bash
# Issue: "remote: Invalid username or password"
# Solution: Use Personal Access Token instead of password
git remote set-url origin https://token@github.com/username/repo.git

# Issue: "Permission denied (publickey)"
# Solution: Check SSH key setup
ssh-add -l  # List loaded keys
ssh-add ~/.ssh/id_ed25519  # Add key to agent
ssh -T git@github.com  # Test connection
```

#### Push/Pull Issues

```bash
# Issue: "failed to push some refs"
# Solution: Pull latest changes first
git pull origin main
git push origin main

# Issue: "Your branch is behind"
# Solution: Fast-forward merge
git pull --ff-only origin main

# Issue: Large file errors
# Solution: Use Git LFS
git lfs track "*.zip"
git add .gitattributes
git add large-file.zip
git commit -m "Add large file with LFS"
```

#### Remote Issues

```bash
# Issue: "fatal: remote origin already exists"
# Solution: Update existing remote
git remote set-url origin https://github.com/username/new-repo.git

# Issue: "fatal: repository not found"
# Solutions:
# 1. Check repository URL
git remote -v
# 2. Verify access permissions
gh repo view username/repo
# 3. Check authentication
gh auth status
```

#### Merge Conflicts

```bash
# Issue: Complex merge conflicts
# Solutions:
# 1. Use merge tool
git mergetool

# 2. Abort and use different strategy
git merge --abort
git rebase origin/main

# 3. Manual resolution
git status  # See conflicted files
# Edit files manually
git add resolved-file.js
git commit
```

### Performance Optimization

```bash
# Speed up clones
git clone --depth 1 --single-branch https://github.com/large/repo.git

# Optimize repository
git gc --aggressive --prune=now

# Clean up remote tracking branches
git remote prune origin

# Reduce repository size
git filter-branch --tree-filter 'rm -rf path/to/large/files' HEAD
# Or use git-filter-repo (recommended)
pip install git-filter-repo
git filter-repo --path-glob '*.large' --invert-paths
```

### Security Best Practices

```bash
# Audit repository for secrets
git log -p | grep -i "password\|secret\|key\|token"

# Remove sensitive data from history
git filter-branch --force --index-filter \
  'git rm --cached --ignore-unmatch path/to/secret/file' \
  --prune-empty --tag-name-filter cat -- --all

# Sign commits
git config --global user.signingkey YOUR_KEY_ID
git config --global commit.gpgsign true
git commit -S -m "Signed commit"

# Verify signatures
git log --show-signature
```

---

## GitHub Git Cheat Sheet

### Quick Authentication

```bash
# Generate SSH key
ssh-keygen -t ed25519 -C "email@example.com"

# Test SSH connection
ssh -T git@github.com

# Login with GitHub CLI
gh auth login

# Set Personal Access Token
export GITHUB_TOKEN="ghp_xxxxxxxxxxxxxxxxxxxx"
```

### Repository Operations

| Command | Description |
|---------|-------------|
| `gh repo clone user/repo` | Clone repository |
| `gh repo create name` | Create new repository |
| `gh repo fork user/repo --clone` | Fork and clone |
| `git remote -v` | List remotes |
| `git remote add name url` | Add remote |
| `git remote remove name` | Remove remote |

### Fetch/Pull/Push

| Command | Description |
|---------|-------------|
| `git fetch origin` | Fetch from origin |
| `git fetch --all --prune` | Fetch all remotes, prune deleted branches |
| `git pull origin main` | Pull and merge |
| `git pull --rebase origin main` | Pull and rebase |
| `git push -u origin branch` | Push and set upstream |
| `git push --force-with-lease` | Safe force push |

### Pull Requests

| Command | Description |
|---------|-------------|
| `gh pr create` | Create pull request |
| `gh pr list` | List pull requests |
| `gh pr view 123` | View PR details |
| `gh pr checkout 123` | Checkout PR locally |
| `gh pr review 123 --approve` | Approve PR |
| `gh pr merge 123 --squash` | Squash and merge |

### Issue Management

| Command | Description |
|---------|-------------|
| `gh issue create` | Create issue |
| `gh issue list` | List issues |
| `gh issue view 123` | View issue |
| `gh issue close 123` | Close issue |
| `gh issue edit 123 --add-label bug` | Add label |

### Workflow Commands

| Command | Description |
|---------|-------------|
| `gh workflow list` | List workflows |
| `gh workflow run name` | Trigger workflow |
| `gh run list` | List workflow runs |
| `gh run view 123` | View run details |
| `gh run watch` | Watch latest run |

### Common Workflows

#### Feature Development
```bash
git checkout main
git pull origin main
git checkout -b feature/new-feature
# Make changes
git add .
git commit -m "feat: add new feature"
git push -u origin feature/new-feature
gh pr create --title "Add new feature"
```

#### Hotfix
```bash
git checkout main
git pull origin main
git checkout -b hotfix/urgent-fix
# Make fix
git commit -am "fix: resolve urgent issue"
git push -u origin hotfix/urgent-fix
gh pr create --title "Urgent hotfix" --label urgent
```

#### Code Review
```bash
gh pr list --review-requested @me
gh pr checkout 123
# Test locally
gh pr review 123 --approve --body "LGTM!"
```

### Credential Management

```bash
# SSH key setup
ssh-keygen -t ed25519 -C "email@example.com"
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519

# Git Credential Manager
git config --global credential.helper manager-core

# Personal Access Token
git config --global credential.helper store
# Then clone with token as password
```

### Emergency Commands

| Situation | Solution |
|-----------|----------|
| Wrong commit pushed | `git revert commit-hash && git push` |
| Sensitive data committed | `git filter-branch` or `git filter-repo` |
| Lost local changes | `git reflog` then `git reset --hard HEAD@{n}` |
| Broken authentication | `gh auth refresh` or `ssh-add ~/.ssh/id_ed25519` |
| Large repository | `git clone --depth 1` for shallow clone |
