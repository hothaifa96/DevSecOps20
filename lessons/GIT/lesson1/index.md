# Git Fundamentals

## Table of Contents

1. [Introduction to Git](#introduction-to-git)
2. [Git Architecture: Working Directory, Staging Area, and Repository](#git-architecture)
3. [Git Configuration](#git-configuration)
4. [Basic Git Commands](#basic-git-commands)
5. [Git Status and Logs](#git-status-and-logs)
6. [Practical Examples](#practical-examples)
7. [Best Practices](#best-practices)

## Introduction to Git

**Git** is a distributed version control system that tracks changes in files and coordinates work among multiple people. It's essential for software development and project management.

### Why Use Git?

- **Version Control**: Track changes over time
- **Collaboration**: Multiple developers can work on the same project
- **Backup**: Distributed nature provides multiple copies
- **Branching**: Create separate lines of development
- **History**: Complete record of all changes

### Key Concepts

- **Repository (Repo)**: A directory that contains your project files and Git metadata
- **Commit**: A snapshot of your project at a specific point in time
- **Branch**: A parallel version of your repository
- **Remote**: A version of your repository hosted elsewhere (like GitHub)

---

## Git Architecture: Working Directory, Staging Area, and Repository

![git-staging](/DevSecOps20/assets/images/git-staging.png)
Git has a three-stage architecture that's crucial to understand:

```
Working Directory  →  Staging Area  →  Local Repository  →  Remote Repository
     (Modified)         (Staged)        (Committed)         (Pushed)
```

### 1. Working Directory

**Definition**: The working directory is your local file system where you actually edit files.

**Characteristics**:

- Contains the actual files you're working on
- Files here can be in different states: untracked, modified, or unchanged
- This is where you make your changes before telling Git about them

**Example**:

```bash
# Your project folder structure
my-project/
├── src/
│   ├── main.py
│   └── utils.py
├── README.md
└── .git/          # Hidden Git metadata folder
```

### 2. Staging Area (Index)

**Definition**: The staging area is a intermediate space where you prepare changes before committing them.

**Characteristics**:

- Acts as a "preview" of your next commit
- You can selectively choose which changes to include
- Allows you to craft meaningful, focused commits
- Files here are "staged for commit"

**Think of it as**: A loading dock where you prepare packages (changes) before shipping them (committing)

### 3. Local Repository

**Definition**: The local repository contains the complete history of your project stored in the `.git` folder.

**Characteristics**:

- Contains all commits (snapshots) of your project
- Stores branches, tags, and configuration
- Works offline - no network connection needed
- Complete backup of your project history

### 4. Remote Repository (Optional)

**Definition**: A version of your repository hosted on a server (like GitHub, GitLab, Bitbucket).

**Characteristics**:

- Enables collaboration with others
- Serves as a backup
- Can be synchronized with your local repository

### The Git Workflow

```
1. EDIT files in Working Directory
     ↓ (git add)
2. STAGE changes in Staging Area
     ↓ (git commit)
3. COMMIT snapshots to Local Repository
     ↓ (git push)
4. PUSH changes to Remote Repository
```

### File States in Git

```
Untracked → Modified → Staged → Committed
    ↑         ↓         ↓         ↓
    └─────────┴─────────┴─────────┘
           (Continuous cycle)
```

**File States Explained**:

- **Untracked**: New files that Git doesn't know about
- **Modified**: Files that have been changed but not staged
- **Staged**: Files that are ready to be committed
- **Committed**: Files that are safely stored in the repository

![git-commands](/DevSecOps20/assets/images/commands.png)

---

## Git Configuration

Git configuration works on three different scopes, each overriding the previous one:

### Configuration Scopes

#### 1. System Level (`--system`)

**Scope**: Applies to all users on the computer and all repositories
**Location**: `/etc/gitconfig` (Linux/Mac) or `C:\Program Files\Git\etc\gitconfig` (Windows)
**Usage**: Rarely used, mainly for system-wide policies

```bash
# Set system-wide configuration (requires admin privileges)
git config --system user.name "Default System User"
git config --system core.editor "nano"

# View system config
git config --system --list
```

#### 2. Global Level (`--global`)

**Scope**: Applies to all repositories for the current user
**Location**: `~/.gitconfig` or `~/.config/git/config`
**Usage**: Most common for personal settings

```bash
# Set global configuration for your user account
git config --global user.name "John Doe"
git config --global user.email "john.doe@example.com"
git config --global core.editor "code --wait"  # VS Code
git config --global core.autocrlf true         # Windows line endings

# View global config
git config --global --list
```

#### 3. Local Level (`--local`)

**Scope**: Applies only to the current repository
**Location**: `.git/config` in the repository root
**Usage**: Project-specific settings, overrides global settings

```bash
# Set local configuration for current repository
git config --local user.name "Work Account"
git config --local user.email "work@company.com"

# View local config
git config --local --list
```

### Configuration Priority

```
Local (highest priority)
  ↓
Global
  ↓
System (lowest priority)
```

### Essential Configuration Settings

#### User Identity

```bash
# Required for making commits
git config --global user.name "Your Full Name"
git config --global user.email "your.email@example.com"

# Verify settings
git config user.name
git config user.email
```

#### Editor Configuration

```bash
# Set default editor for commit messages
git config --global core.editor "nano"           # Nano editor
git config --global core.editor "code --wait"    # VS Code
git config --global core.editor "vim"            # Vim editor
git config --global core.editor "subl -n -w"     # Sublime Text
```

#### Line Ending Configuration (CRLF)

**Problem**: Different operating systems use different line endings:

- **Windows**: CRLF (`\r\n`)
- **Linux/Mac**: LF (`\n`)

```bash
# Windows users (converts LF to CRLF on checkout, CRLF to LF on commit)
git config --global core.autocrlf true

# Linux/Mac users (converts CRLF to LF on commit, no conversion on checkout)
git config --global core.autocrlf input

# No conversion (not recommended for cross-platform projects)
git config --global core.autocrlf false
```

### Editing Configuration Files

#### Using Git Config Command

```bash
# Edit global config file in your default editor
git config --global -e

# Edit local config file
git config --local -e

# Edit system config file (requires admin)
git config --system -e
```

#### Direct File Editing

Global config file (`~/.gitconfig`) example:

```ini
[user]
    name = John Doe
    email = john.doe@example.com
[core]
    editor = code --wait
    autocrlf = true
[init]
    defaultBranch = main
[color]
    ui = auto
```

### Viewing Configuration

```bash
# View all configuration (all scopes)
git config --list

# View configuration with origins
git config --list --show-origin

# View specific configuration value
git config user.name
git config user.email

# View configuration for specific scope
git config --global --list
git config --local --list
```

### Removing Configuration

```bash
# Remove specific configuration
git config --global --unset user.name
git config --local --unset user.email

# Remove entire section
git config --global --remove-section user
```

---

## Basic Git Commands

### Repository Initialization

#### Creating a New Repository

```bash
# Initialize a new Git repository in current directory
git init

# Initialize with specific branch name
git init --initial-branch=main
# or
git init -b main

# Initialize in a new directory
git init my-new-project
cd my-new-project
```

**What happens when you run `git init`**:

1. Creates a `.git` folder containing all Git metadata
2. Sets up the basic repository structure
3. Creates the initial branch (usually `main` or `master`)
4. Repository is ready to track files

#### Cloning an Existing Repository

```bash
# Clone from remote repository
git clone https://github.com/user/repository.git

# Clone with custom directory name
git clone https://github.com/user/repository.git my-project

# Clone specific branch
git clone -b feature-branch https://github.com/user/repository.git
```

### Adding Changes to Staging Area

The `git add` command moves changes from the working directory to the staging area.

#### Basic Add Operations

```bash
# Add a specific file
git add filename.txt

# Add multiple files
git add file1.txt file2.py file3.html

# Add all files in current directory and subdirectories
git add .

# Add all files (including deleted ones)
git add -A
# or
git add --all

# Add all modified and deleted files (not new files)
git add -u
# or
git add --update
```

#### Advanced Add Operations

```bash
# Add files matching a pattern
git add "*.py"          # All Python files
git add "src/*.js"      # All JavaScript files in src directory

# Interactive staging (choose what to stage)
git add -i
# or
git add --interactive

# Patch mode (stage parts of files)
git add -p filename.txt
# or
git add --patch filename.txt

# Add and commit in one command (for tracked files only)
git commit -am "commit message"
```

#### Understanding What Gets Added

```bash
# Before adding
echo "Hello World" > hello.txt
echo "Python script" > script.py

# Check status
git status
# Shows:
# Untracked files:
#   hello.txt
#   script.py

# Add specific file
git add hello.txt

# Check status again
git status
# Shows:
# Changes to be committed:
#   new file: hello.txt
# Untracked files:
#   script.py
```

### Committing Changes

The `git commit` command creates a snapshot of staged changes.

#### Basic Commit Operations

```bash
# Commit with inline message
git commit -m "Add hello world file"

# Commit with detailed message (opens editor)
git commit

# Add and commit tracked files in one step
git commit -am "Update existing files"

# Commit with both short and detailed message
git commit -m "Short description" -m "Detailed explanation of changes"
```

#### Commit Message Best Practices

```bash
# Good commit message structure
git commit -m "Add user authentication feature

- Implement login/logout functionality
- Add password validation
- Include session management
- Update user database schema"

# Use imperative mood (like giving commands)
git commit -m "Fix login bug"           # Good
git commit -m "Fixed login bug"         # Less preferred
git commit -m "Fixes login bug"         # Less preferred
```

#### Commit Message Templates

```bash
# Set up commit template
git config --global commit.template ~/.gitmessage

# Example template file (~/.gitmessage):
# [TYPE] Short description (max 50 chars)
#
# Detailed explanation (wrap at 72 chars)
# - What was changed
# - Why it was changed
# - Any side effects
#
# [TYPE] can be: feat, fix, docs, style, refactor, test, chore
```

#### Advanced Commit Options

```bash
# Amend the last commit (change message or add files)
git add forgotten-file.txt
git commit --amend -m "Updated commit message"

# Commit with specific author
git commit -m "Fix bug" --author="Jane Doe <jane@example.com>"

# Commit with specific date
git commit -m "Historical commit" --date="2023-01-01T12:00:00"

# Empty commit (useful for triggering CI/CD)
git commit --allow-empty -m "Trigger deployment"
```

---

## Git Status and Logs

### Git Status

The `git status` command shows the current state of your working directory and staging area.

#### Basic Status Information

```bash
# Show current status
git status

# Short format status
git status -s
# or
git status --short
```

#### Understanding Status Output

**Full Status Example**:

```bash
$ git status
On branch main
Your branch is up to date with 'origin/main'.

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
    new file:   feature.py
    modified:   README.md

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
    modified:   config.json
    deleted:    old-file.txt

Untracked files:
  (use "git add <file>..." to include in what will be committed)
    temp.log
```

**Short Status Format**:

```bash
$ git status -s
A  feature.py      # Added to staging area
M  README.md       # Modified and staged
 M config.json     # Modified but not staged
 D old-file.txt    # Deleted but not staged
?? temp.log        # Untracked file
```

**Status Indicators**:

- `??` - Untracked files
- `A` - Added (new files in staging area)
- `M` - Modified
- `D` - Deleted
- `R` - Renamed
- `C` - Copied
- `U` - Updated but unmerged

#### Status Options

```bash
# Show status with branch information
git status -b

# Show ignored files too
git status --ignored

# Porcelain format (machine-readable)
git status --porcelain
```

### Git Logs

The `git log` command shows the commit history of your repository.

#### Basic Log Commands

```bash
# Show all commits
git log

# Show last n commits
git log -n 5
git log -5

# One-line format
git log --oneline

# Show commits with file changes
git log --stat

# Show actual changes in commits
git log -p
git log --patch
```

#### Log Formatting Options

```bash
# Custom format
git log --pretty=format:"%h - %an, %ar : %s"
# Output: a1b2c3d - John Doe, 2 hours ago : Add user authentication

# Predefined formats
git log --pretty=oneline
git log --pretty=short
git log --pretty=full
git log --pretty=fuller

# Graph view (useful for branches)
git log --graph
git log --oneline --graph --all

# Decorate with branch and tag names
git log --decorate
```

#### Filtering Commits

```bash
# Commits by author
git log --author="John Doe"
git log --author="john@example.com"

# Commits by date
git log --since="2023-01-01"
git log --until="2023-12-31"
git log --since="2 weeks ago"
git log --after="2023-01-01" --before="2023-02-01"

# Commits by message content
git log --grep="bug fix"
git log --grep="feature" --grep="add" --all-match

# Commits that modified specific files
git log -- filename.txt
git log --follow -- filename.txt  # Follow file renames

# Commits in a range
git log HEAD~5..HEAD    # Last 5 commits
git log main..feature   # Commits in feature but not in main
```

#### Advanced Log Options

```bash
# Show commits with file statistics
git log --stat --oneline

# Show commits that changed specific lines
git log -L 10,20:filename.txt    # Lines 10-20 in file
git log -L :functionName:file.py # Specific function

# Show merge commits only
git log --merges

# Exclude merge commits
git log --no-merges

# Show first-parent only (useful for merge commits)
git log --first-parent

# Reverse chronological order
git log --reverse
```

#### Useful Log Aliases

You can create aliases for commonly used log commands:

```bash
# Set up useful aliases
git config --global alias.lg "log --oneline --graph --decorate --all"
git config --global alias.ll "log --pretty=format:'%C(yellow)%h%Creset -%C(red)%d%Creset %s %C(green)(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit"
git config --global alias.ls "log --stat --oneline"

# Usage
git lg    # Pretty graph view
git ll    # Detailed one-line format
git ls    # One-line with statistics
```

---

## Practical Examples

### Setting Up a New Project

```bash
# 1. Create and navigate to project directory
mkdir my-awesome-project
cd my-awesome-project

# 2. Initialize Git repository
git init

# 3. Configure Git (if not done globally)
git config --local user.name "Your Name"
git config --local user.email "your.email@example.com"

# 4. Create initial files
echo "# My Awesome Project" > README.md
echo "print('Hello, World!')" > main.py
echo "*.pyc" > .gitignore

# 5. Check status
git status
# Output:
# Untracked files:
#   README.md
#   main.py
#   .gitignore

# 6. Add files to staging area
git add README.md main.py .gitignore

# 7. Check status again
git status
# Output:
# Changes to be committed:
#   new file:   .gitignore
#   new file:   README.md
#   new file:   main.py

# 8. Make initial commit
git commit -m "Initial commit: Add project structure

- Add README with project description
- Add main.py with hello world
- Add .gitignore for Python files"

# 9. View commit history
git log --oneline
# Output: a1b2c3d (HEAD -> main) Initial commit: Add project structure
```

### Working with Changes

```bash
# Make changes to existing file
echo "This project demonstrates Git basics." >> README.md

# Create new file
echo "def greet(name): return f'Hello, {name}!'" > utils.py

# Check what changed
git status
# Shows modified README.md and untracked utils.py

# See specific changes
git diff README.md
# Shows the line that was added

# Stage specific changes
git add README.md
git add utils.py

# Check status
git status
# Both files are now staged

# Commit changes
git commit -m "feat: Enhance project documentation and add utility functions

- Update README with project description
- Add utils.py with greeting function"

# View history
git log --oneline -3
```

### Configuration Example

```bash
# Check current configuration
git config --list

# Set up global configuration
git config --global user.name "DevOps Engineer"
git config --global user.email "devops@company.com"
git config --global core.editor "code --wait"
git config --global core.autocrlf true
git config --global init.defaultBranch main

# Set up project-specific configuration
git config --local user.email "project-specific@company.com"

# Edit global config
git config --global -e
# This opens your configured editor with the global config file

# View configuration with origins
git config --list --show-origin
```

---

## Best Practices

### Repository Management

1. **Always initialize with .gitignore**: Include files/patterns that shouldn't be tracked
2. **Meaningful repository structure**: Organize files logically
3. **Regular commits**: Commit frequently with meaningful messages
4. **Atomic commits**: Each commit should represent one logical change

### Commit Messages

1. **Use imperative mood**: "Add feature" not "Added feature"
2. **Keep first line under 50 characters**: Summary should be concise
3. **Separate subject from body**: Use blank line between summary and details
4. **Explain what and why**: Don't just describe what changed, explain why

### Configuration

1. **Set up global config first**: Configure name, email, and editor globally
2. **Use project-specific configs when needed**: Override global settings for specific projects
3. **Configure line endings properly**: Use appropriate CRLF settings for your platform
4. **Use aliases for common commands**: Create shortcuts for frequently used commands

### File Management

1. **Stage changes deliberately**: Review what you're adding before committing
2. **Use .gitignore effectively**: Keep unnecessary files out of the repository
3. **Review changes before committing**: Use `git diff` and `git status`
4. **Keep commits focused**: Don't mix unrelated changes in a single commit

### Example Workflow

```bash
# Daily workflow example
git status                    # Check current state
git add .                     # Stage all changes (or specific files)
git status                    # Verify what will be committed
git commit -m "Descriptive message"  # Commit changes
git log --oneline -5          # Review recent commits
```

### Common Git Ignore Patterns

```gitignore
# Python
*.pyc
__pycache__/
*.pyo
*.pyd
.Python
env/
venv/
.venv

# Node.js
node_modules/
npm-debug.log*
yarn-debug.log*
yarn-error.log*

# IDEs
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db

# Logs
*.log
logs/

# Environment
.env
.env.local
```

---

## Common Commands Quick Reference

```bash
# Repository setup
git init                      # Initialize repository
git clone <url>               # Clone remote repository

# Configuration
git config --global user.name "Name"     # Set global username
git config --global user.email "email"   # Set global email
git config --list             # View all configuration

# Basic workflow
git status                    # Check repository status
git add <file>                # Stage specific file
git add .                     # Stage all changes
git commit -m "message"       # Commit with message
git log                       # View commit history
git log --oneline             # Compact commit history

# Viewing changes
git diff                      # Show unstaged changes
git diff --staged             # Show staged changes
git show <commit>             # Show specific commit

# Information
git status -s                 # Short status format
git log --graph --oneline     # Visual commit tree
git config --show-origin --list  # Config with file locations
```

This tutorial provides a comprehensive foundation for understanding Git's core concepts and essential commands. Practice these commands regularly to build muscle memory and confidence with Git workflows.
