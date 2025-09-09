## 📖 Fundamental Bash Concepts

### What is Bash?
**Bash** (Bourne Again Shell) is a command processor that typically runs in a text window where users type commands. It's also a scripting language that allows you to automate tasks.

### The Shebang Line: `#!/bin/bash`
**What it is**: The shebang (`#!`) tells the system which interpreter to use for executing the script.

**Why it matters**: Without it, the system doesn't know how to run your script.

```bash
#!/bin/bash
# Basic range - numbers 1 to 5
echo "=== Creating backup files ==="
for i in {1..5}; do
    backup_file="backup_$(date +%Y%m%d)_$i.tar.gz"
    echo "Creating: $backup_file"
    # Simulate backup creation
    touch "$backup_file"
done

# Range with increment - every 2nd number from 2 to 10
echo "=== Processing even numbers ==="
for num in {2..10..2}; do
    echo "Processing number: $num"
    result=$((num * num))
    echo "  Square of $num is $result"
done

# Countdown
echo "=== Countdown to deployment ==="
for count in {5..1}; do
    echo "Deploying in $count seconds..."
    sleep 1
done
echo "🚀 Deployment started!"
```

#### C-Style For Loop
**Syntax**: `for ((initialization; condition; increment))`
**When to use**: When you need precise control over the loop counter

```bash
#!/bin/bash
# C-style for loop
echo "=== Processing files with C-style loop ==="
total_files=10

for ((i=1; i<=total_files; i++)); do
    percentage=$((i * 100 / total_files))
    echo "Processing file $i of $total_files ($percentage%)"
    
    # Simulate file processing
    sleep 0.2
    
    # Add conditional logic
    if (( i % 3 == 0 )); then
        echo "  ✅ Checkpoint reached at file $i"
    fi
done

echo "✅ All files processed!"
```

#### For Loop with Command Output
**Use case**: Process results from commands like `find`, `ls`, `grep`

```bash
#!/bin/bash
# Loop through files found by command
echo "=== Processing log files ==="

# Method 1: Using command substitution (be careful with spaces in filenames)
for file in $(find /var/log -name "*.log" -type f 2>/dev/null | head -5); do
    if [ -r "$file" ]; then
        size=$(du -h "$file" | cut -f1)
        lines=$(wc -l < "$file")
        echo "📄 $file"
        echo "   Size: $size"
        echo "   Lines: $lines"
    fi
done

# Method 2: Better approach for filenames with spaces
echo "=== Processing with while read loop ==="
find /var/log -name "*.log" -type f 2>/dev/null | head -3 | while IFS= read -r file; do
    if [ -r "$file" ]; then
        echo "📄 Processing: $file"
        echo "   Last modified: $(stat -c %y "$file" 2>/dev/null || echo "unknown")"
    fi
done
```

### While Loops - Execute While Condition is True

#### Basic While Loop Structure
**Syntax**: `while [ condition ]; do commands; done`
**Key concept**: Loop continues as long as condition is true

```bash
#!/bin/bash
# Basic counter example
echo "=== Basic While Loop ==="
counter=1
max_count=5

while [ $counter -le $max_count ]; do
    echo "Iteration $counter of $max_count"
    
    # Simulate some work
    echo "  Processing task $counter..."
    sleep 0.5
    
    # Increment counter (IMPORTANT: always update the condition variable!)
    counter=$((counter + 1))
done

echo "✅ Loop completed!"
```

#### Reading Files Line by Line
**Best practice**: Use `while IFS= read -r line` for reading files

**Why `IFS=`?** Preserves leading/trailing whitespace
**Why `-r`?** Prevents backslash escaping

```bash
#!/bin/bash
# Reading configuration file
config_file="/etc/hosts"

echo "=== Reading $config_file ==="
line_number=1

while IFS= read -r line; do
    # Skip empty lines
    if [ -z "$line" ]; then
        ((line_number++))
        continue
    fi
    
    # Skip comment lines
    if [[ "$line" =~ ^[[:space:]]*# ]]; then
        echo "Line $line_number: [COMMENT] ${line:0:50}..."
    else
        echo "Line $line_number: [ACTIVE] $line"
    fi
    
    ((line_number++))
done < "$config_file"

echo "✅ Finished reading file ($((line_number - 1)) lines total)"
```

#### Interactive Menu with While Loop
**Use case**: Create user-interactive scripts

```bash
#!/bin/bash
# Interactive system monitoring menu
echo "=== System Monitoring Tool ==="

while true; do
    echo ""
    echo "Choose an option:"
    echo "1) Check disk space"
    echo "2) Check memory usage"
    echo "3) Check running processes"
    echo "4) Check network connections"
    echo "5) Exit"
    echo ""
    
    read -p "Enter your choice (1-5): " choice
    
    case $choice in
        1)
            echo "📊 Disk Space:"
            df -h | grep -E "^/dev/" | while read line; do
                echo "  $line"
            done
            ;;
        2)
            echo "📊 Memory Usage:"
            free -h | head -2
            ;;
        3)
            echo "📊 Top 5 Processes by CPU:"
            ps aux --sort=-%cpu | head -6
            ;;
        4)
            echo "📊 Network Connections:"
            netstat -tuln 2>/dev/null | head -10 || ss -tuln | head -10
            ;;
        5)
            echo "👋 Goodbye!"
            break  # Exit the while loop
            ;;
        *)
            echo "❌ Invalid option. Please choose 1-5."
            ;;
    esac
    
    # Pause before showing menu again
    echo ""
    read -p "Press Enter to continue..."
done
```

#### Service Monitoring with While Loop
**Real-world example**: Monitor service status with retry logic

```bash
#!/bin/bash
# Service monitoring script
service_name="nginx"
max_attempts=10
wait_time=2
attempt=1

echo "=== Monitoring service: $service_name ==="

while [ $attempt -le $max_attempts ]; do
    echo "Attempt $attempt of $max_attempts: Checking $service_name..."
    
    if systemctl is-active --quiet "$service_name"; then
        echo "✅ $service_name is running successfully!"
        
        # Get additional service info
        status=$(systemctl show -p ActiveState,LoadState "$service_name")
        echo "📋 Service details:"
        echo "   $status"
        
        # Exit successfully
        exit 0
    else
        echo "❌ $service_name is not running"
        
        if [ $attempt -eq $max_attempts ]; then
            echo "🚨 CRITICAL: Failed to start $service_name after $max_attempts attempts"
            echo "📧 Sending alert notification..."
            # Here you would typically send an alert
            exit 1
        fi
        
        echo "🔄 Attempting to start $service_name..."
        # Uncomment the next line to actually start the service
        # sudo systemctl start "$service_name"
        
        echo "⏳ Waiting $wait_time seconds before next attempt..."
        sleep $wait_time
    fi
    
    attempt=$((attempt + 1))
done
```

### Until Loops - Execute Until Condition Becomes True

#### Understanding Until vs While
**While**: Continue WHILE condition is true
**Until**: Continue UNTIL condition becomes true (opposite of while)

```bash
#!/bin/bash
# Demonstration of until vs while
counter=1

echo "=== While loop (while counter <= 3) ==="
while [ $counter -le 3 ]; do
    echo "While: Counter is $counter"
    counter=$((counter + 1))
done

counter=1
echo "=== Until loop (until counter > 3) ==="
until [ $counter -gt 3 ]; do
    echo "Until: Counter is $counter"
    counter=$((counter + 1))
done

echo "Both loops produce the same result!"
```

#### Waiting for File Creation
**Use case**: Wait for another process to create a file

```bash
#!/bin/bash
# Wait for deployment completion signal
signal_file="/tmp/deployment_complete.flag"
timeout_seconds=60
check_interval=2
elapsed=0

echo "=== Waiting for deployment completion ==="
echo "Looking for signal file: $signal_file"
echo "Timeout: $timeout_seconds seconds"

# Clean up any existing signal file
rm -f "$signal_file"

until [ -f "$signal_file" ] || [ $elapsed -ge $timeout_seconds ]; do
    echo "⏳ Waiting... ($elapsed/$timeout_seconds seconds elapsed)"
    sleep $check_interval
    elapsed=$((elapsed + check_interval))
done

if [ -f "$signal_file" ]; then
    echo "✅ Deployment completed successfully!"
    echo "📄 Signal file contents:"
    cat "$signal_file"
    
    # Clean up
    rm -f "$signal_file"
    exit 0
else
    echo "❌ Timeout: Deployment did not complete within $timeout_seconds seconds"
    echo "🔍 Checking for partial completion..."
    
    # Check for other deployment-related files
    if ls /tmp/deploy_* 2>/dev/null; then
        echo "⚠️ Found partial deployment files - manual intervention required"
    fi
    
    exit 1
fi
```

#### Network Service Availability Check
**Use case**: Wait for a service to become available over the network

```bash
#!/bin/bash
# Wait for service to be available
host="example.com"
port=80
max_wait=120
check_interval=5
waited=0

echo "=== Waiting for $host:$port to be available ==="

until nc -z "$host" "$port" 2>/dev/null || [ $waited -ge $max_wait ]; do
    echo "⏳ Service not available yet... ($waited/$max_wait seconds)"
    
    # Optional: Try different diagnostic commands
    if command -v telnet >/dev/null; then
        echo "   Trying telnet test..."
        timeout 2 telnet "$host" "$port" </dev/null 2>/dev/null && break
    fi
    
    sleep $check_interval
    waited=$((waited + check_interval))
done

if nc -z "$host" "$port" 2>/dev/null; then
    echo "✅ Service at $host:$port is now available!"
    echo "🕒 Total wait time: $waited seconds"
    
    # Optional: Perform additional connectivity tests
    if command -v curl >/dev/null; then
        echo "🔍 Testing HTTP connectivity..."
        if curl -s --connect-timeout 5 "http://$host:$port" >/dev/null; then
            echo "✅ HTTP connection successful"
        else
            echo "⚠️ Port is open but HTTP request failed"
        fi
    fi
else
    echo "❌ Timeout: Service at $host:$port is still not available after $max_wait seconds"
    echo "🔍 Diagnostic information:"
    echo "   Host resolution: $(nslookup "$host" 2>/dev/null | grep "Address:" | tail -1 || echo "Failed")"
    echo "   Network route: $(ip route get 8.8.8.8 2>/dev/null | head -1 || echo "Failed")"
    exit 1
fi
```

### Loop Control Commands

#### `break` - Exit Loop Early
**Purpose**: Exit the current loop immediately

```bash
#!/bin/bash
# Finding the first error in log files
echo "=== Searching for errors in log files ==="

for log_file in /var/log/*.log; do
    if [ ! -r "$log_file" ]; then
        echo "⏭️ Skipping unreadable file: $log_file"
        continue
    fi
    
    echo "🔍 Checking $log_file..."
    
    if grep -q "ERROR" "$log_file" 2>/dev/null; then
        echo "🚨 ERROR found in $log_file!"
        echo "📄 First error:"
        grep "ERROR" "$log_file" | head -1
        break  # Stop checking other files
    else
        echo "✅ No errors in $log_file"
    fi
done

echo "🏁 Error search completed"
```

#### `continue` - Skip to Next Iteration
**Purpose**: Skip the rest of the current iteration and move to the next

```bash
#!/bin/bash
# Process only valid configuration files
echo "=== Processing configuration files ==="

for config_file in /etc/*.conf /etc/myapp/*.conf; do
    # Skip if file doesn't exist (from glob expansion)
    if [ ! -f "$config_file" ]; then
        continue
    fi
    
    # Skip if file is not readable
    if [ ! -r "$config_file" ]; then
        echo "⏭️ Skipping unreadable file: $config_file"
        continue
    fi
    
    # Skip if file is empty
    if [ ! -s "$config_file" ]; then
        echo "⏭️ Skipping empty file: $config_file"
        continue
    fi
    
    # Process the file
    echo "✅ Processing: $config_file"
    line_count=$(wc -l < "$config_file")
    echo "   Lines: $line_count"
    
    # Look for specific configuration
    if grep -q "database" "$config_file"; then
        echo "   📊 Contains database configuration"
    fi
done
```

### Nested Loops - Loops Within Loops

**Use case**: When you need to process multi-dimensional data

```bash
#!/bin/bash
# Check multiple services on multiple servers
servers=("web01" "web02" "db01")
services=("nginx" "mysql" "ssh")

echo "=== Multi-Server Service Check ==="

for server in "${servers[@]}"; do
    echo ""
    echo "🖥️ Checking server: $server"
    echo "=================="
    
    # Check if server is reachable first
    if ! ping -c 1 -W 2 "$server" >/dev/null 2>&1; then
        echo "❌ $server is unreachable - skipping service checks"
        continue
    fi
    
    echo "✅ $server is reachable"
    
    # Check each service on this server
    for service in "${services[@]}"; do
        echo "  🔍 Checking $service on $server..."
        
        # In real scenario, you'd use ssh to check remote services
        # ssh "$server" "systemctl is-active --quiet $service"
        
        # For demo, simulate random results
        if (( RANDOM % 2 )); then
            echo "    ✅ $service is running"
        else
            echo "    ❌ $service is not running"
            echo "    🔄 Would restart $service on $server"
        fi
    done
done

echo ""
echo "🏁 Multi-server check completed"
```

---

## 5. Advanced Examples and Real-World Applications

### Complete System Monitoring Script

This script demonstrates all concepts learned so far in a practical DevSecOps context.

```bash
#!/bin/bash
# Advanced System Monitoring Script
# Demonstrates: variables, arguments, conditionals, loops, file tests

set -euo pipefail  # Exit on error, undefined variables, pipe failures

# =============================================================================
# CONFIGURATION SECTION
# =============================================================================

# Script metadata
readonly SCRIPT_NAME="$(basename "$0")"
readonly SCRIPT_VERSION="1.0.0"
readonly LOG_FILE="/var/log/system_monitor.log"

# Monitoring thresholds (configurable via environment variables)
readonly CPU_THRESHOLD="${CPU_THRESHOLD:-80}"
readonly MEMORY_THRESHOLD="${MEMORY_THRESHOLD:-85}"
readonly DISK_THRESHOLD="${DISK_THRESHOLD:-90}"

# Colors for output (if terminal supports it)
if [ -t 1 ]; then
    readonly RED='\033[0;31m'
    readonly GREEN='\033[0;32m'
    readonly YELLOW='\033[1;33m'
    readonly BLUE='\033[0;34m'
    readonly NC='\033[0m' # No Color
else
    readonly RED=''
    readonly GREEN=''
    readonly YELLOW=''
    readonly BLUE=''
    readonly NC=''
fi

# =============================================================================
# FUNCTIONS SECTION
# =============================================================================

# Function to print colored output
print_color() {
    local color=$1
    local message=$2
    echo -e "${color}${message}${NC}"
}

# Function to log messages with timestamp
log_message() {
    local level=$1
    local message=$2
    local timestamp=$(date '+%Y-%m-%d %H:%M:%S')
    
    echo "[$timestamp] [$level] $message" | tee -a "$LOG_FILE"
}

# Function to show usage information
show_usage() {
    cat << EOF
Usage: $SCRIPT_NAME [OPTIONS]

Advanced System Monitoring Script v$SCRIPT_VERSION

OPTIONS:
    -c, --cpu       Check CPU usage only
    -m, --memory    Check memory usage only  
    -d, --disk      Check disk usage only
    -a, --all       Check all systems (default)
    -q, --quiet     Quiet mode (minimal output)
    -v, --verbose   Verbose mode (detailed output)
    -h, --help      Show this help message

EXAMPLES:
    $SCRIPT_NAME                    # Check all systems
    $SCRIPT_NAME --cpu --memory     # Check CPU and memory only
    $SCRIPT_NAME -v -a              # Verbose check of all systems

ENVIRONMENT VARIABLES:
    CPU_THRESHOLD      CPU usage alert threshold (default: 80%)
    MEMORY_THRESHOLD   Memory usage alert threshold (default: 85%)  
    DISK_THRESHOLD     Disk usage alert threshold (default: 90%)

EXIT CODES:
    0  All systems normal
    1  System(s) above threshold
    2  Error during execution
EOF
}

# Function to check CPU usage
check_cpu_usage() {
    local verbose=$1
    
    log_message "INFO" "Checking CPU usage..."
    
    # Get CPU usage (average over 1 second)
    local cpu_usage
    cpu_usage=$(top -bn1 | grep "Cpu(s)" | awk '{print $2}' | sed 's/%us,//' | cut -d'.' -f1)
    
    # Fallback method if top command format differs
    if [ -z "$cpu_usage" ] || ! [[ "$cpu_usage" =~ ^[0-9]+$ ]]; then
        cpu_usage=$(vmstat 1 2 | tail -1 | awk '{print 100-$15}' | cut -d'.' -f1)
    fi
    
    # Validate we got a number
    if ! [[ "$cpu_usage" =~ ^[0-9]+$ ]]; then
        log_message "ERROR" "Failed to get CPU usage"
        return 2
    fi
    
    if [ "$verbose" = true ]; then
        print_color "$BLUE" "📊 CPU Usage Details:"
        echo "   Current usage: ${cpu_usage}%"
        echo "   Threshold: ${CPU_THRESHOLD}%"
        echo "   Load average: $(uptime | awk -F'load average:' '{print $2}')"
    fi
    
    if [ "$cpu_usage" -gt "$CPU_THRESHOLD" ]; then
        print_color "$RED" "🚨 CPU ALERT: Usage is ${cpu_usage}% (threshold: ${CPU_THRESHOLD}%)"
        log_message "ALERT" "High CPU usage: ${cpu_usage}%"
        
        if [ "$verbose" = true ]; then
            echo "   Top CPU processes:"
            ps aux --sort=-%cpu | head -5 | while read line; do
                echo "     $line"
            done
        fi
        return 1
    else
        print_color "$GREEN" "✅ CPU usage is normal: ${cpu_usage}%"
        log_message "INFO" "CPU usage normal: ${cpu_usage}%"
        return 0
    fi
}

# Function to check memory usage
check_memory_usage() {
    local verbose=$1
    
    log_message "INFO" "Checking memory usage..."
    
    # Get memory information
    local memory_info
    memory_info=$(free | grep '^Mem:')
    local total_memory=$(echo "$memory_info" | awk '{print $2}')
    local used_memory=$(echo "$memory_info" | awk '{print $3}')
    local memory_percentage=$((used_memory * 100 / total_memory))
    
    if [ "$verbose" = true ]; then
        print_color "$BLUE" "📊 Memory Usage Details:"
        echo "   Used: $(echo "$memory_info" | awk '{print $3}') KB"
        echo "   Total: $(echo "$memory_info" | awk '{print $2}') KB"
        echo "   Percentage: ${memory_percentage}%"
        echo "   Threshold: ${MEMORY_THRESHOLD}%"
        free -h
    fi
    
    if [ "$memory_percentage" -gt "$MEMORY_THRESHOLD" ]; then
        print_color "$RED" "🚨 MEMORY ALERT: Usage is ${memory_percentage}% (threshold: ${MEMORY_THRESHOLD}%)"
        log_message "ALERT" "High memory usage: ${memory_percentage}%"
        
        if [ "$verbose" = true ]; then
            echo "   Top memory processes:"
            ps aux --sort=-%mem | head -5 | while read line; do
                echo "     $line"
            done
        fi
        return 1
    else
        print_color "$GREEN" "✅ Memory usage is normal: ${memory_percentage}%"
        log_message "INFO" "Memory usage normal: ${memory_percentage}%"
        return 0
    fi
}

# Function to check disk usage
check_disk_usage() {
    local verbose=$1
    local alert_triggered=false
    
    log_message "INFO" "Checking disk usage..."
    
    if [ "$verbose" = true ]; then
        print_color "$BLUE" "📊 Disk Usage Details:"
        df -h
        echo ""
    fi
    
    # Check each mounted filesystem
    while IFS= read -r line; do
        # Skip header line and non-disk filesystems
        if [[ "$line" =~ ^Filesystem ]] || [[ ! "$line" =~ ^/dev/ ]]; then
            continue
        fi
        
        local usage_percent=$(echo "$line" | awk '{print $5}' | sed 's/%//')
        local mountpoint=$(echo "$line" | awk '{print $6}')
        local filesystem=$(echo "$line" | awk '{print $1}')
        
        if [ "$usage_percent" -gt "$DISK_THRESHOLD" ]; then
            print_color "$RED" "🚨 DISK ALERT: $mountpoint is ${usage_percent}% full (threshold: ${DISK_THRESHOLD}%)"
            log_message "ALERT" "High disk usage on $mountpoint: ${usage_percent}%"
            alert_triggered=true
            
            if [ "$verbose" = true ]; then
                echo "   Filesystem: $filesystem"
                echo "   Mount point: $mountpoint"
                echo "   Usage: ${usage_percent}%"
                echo "   Largest files in $mountpoint:"
                find "$mountpoint" -type f -exec du -h {} + 2>/dev/null | sort -rh | head -5 | while read size file; do
                    echo "     $size  $file"
                done
                echo ""
            fi
        else
            print_color "$GREEN" "✅ Disk usage normal on $mountpoint: ${usage_percent}%"
            log_message "INFO" "Disk usage normal on $mountpoint: ${usage_percent}%"
        fi
    done < <(df -h)
    
    if [ "$alert_triggered" = true ]; then
        return 1
    else
        return 0
    fi
}

# =============================================================================
# MAIN SCRIPT EXECUTION
# =============================================================================

# Initialize variables
check_cpu=false
check_memory=false
check_disk=false
check_all=true
verbose=false
quiet=false

# Parse command line arguments
while [[ $# -gt 0 ]]; do
    case $1 in
        -c|--cpu)
            check_cpu=true
            check_all=false
            shift
            ;;
        -m|--memory)
            check_memory=true
            check_all=false
            shift
            ;;
        -d|--disk)
            check_disk=true
            check_all=false
            shift
            ;;
        -a|--all)
            check_all=true
            shift
            ;;
        -v|--verbose)
            verbose=true
            shift
            ;;
        -q|--quiet)
            quiet=true
            shift
            ;;
        -h|--help)
            show_usage
            exit 0
            ;;
        *)
            echo "Unknown option: $1"
            show_usage
            exit 2
            ;;
    esac
done

# Ensure log directory exists
log_dir=$(dirname "$LOG_FILE")
if [ ! -d "$log_dir" ]; then
    mkdir -p "$log_dir" || {
        echo "Error: Cannot create log directory $log_dir"
        exit 2
    }
fi

# Start monitoring
if [ "$quiet" = false ]; then
    print_color "$BLUE" "🔍 Starting system monitoring..."
    echo "Timestamp: $(date)"
    echo "Thresholds: CPU=${CPU_THRESHOLD}%, Memory=${MEMORY_THRESHOLD}%, Disk=${DISK_THRESHOLD}%"
    echo ""
fi

log_message "INFO" "System monitoring started by user $USER"

# Track overall status
overall_status=0

# Determine what to check
if [ "$check_all" = true ]; then
    check_cpu=true
    check_memory=true
    check_disk=true
fi

# Perform checks
if [ "$check_cpu" = true ]; then
    check_cpu_usage "$verbose" || overall_status=1
fi

if [ "$check_memory" = true ]; then
    check_memory_usage "$verbose" || overall_status=1
fi

if [ "$check_disk" = true ]; then
    check_disk_usage "$verbose" || overall_status=1
fi

# Final summary
if [ "$quiet" = false ]; then
    echo ""
    if [ $overall_status -eq 0 ]; then
        print_color "$GREEN" "✅ All systems are operating within normal parameters"
    else
        print_color "$RED" "⚠️ One or more systems require attention"
    fi
    
    echo "📄 Full logs available at: $LOG_FILE"
fi

log_message "INFO" "System monitoring completed with exit status $overall_status"

exit $overall_status
```

### Deployment Script with Comprehensive Error Handling

```bash
#!/bin/bash
# Production Deployment Script
# Demonstrates advanced bash scripting for DevSecOps

set -euo pipefail

# =============================================================================
# CONFIGURATION
# =============================================================================

readonly SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
readonly APP_NAME="myapp"
readonly DEPLOY_BASE="/opt"
readonly DEPLOY_DIR="$DEPLOY_BASE/$APP_NAME"
readonly BACKUP_DIR="/opt/backups"
readonly SERVICE_NAME="$APP_NAME"

# Deployment settings
readonly MAX_RETRIES=3
readonly HEALTH_CHECK_TIMEOUT=60
readonly ROLLBACK_ON_FAILURE=true

# =============================================================================
# UTILITY FUNCTIONS  
# =============================================================================

log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $*" >&2
}

error() {
    log "ERROR: $*"
    exit 1
}

warn() {
    log "WARN: $*"
}

info() {
    log "INFO: $*"
}

# Function to check if running as root
check_root() {
    if [ "$EUID" -ne 0 ]; then
        error "This script must be run as root or with sudo"
    fi
}

# Function to validate environment
validate_environment() {
    local env=$1
    
    case "$env" in
        development|dev)
            return 0
            ;;
        staging|stage)
            return 0
            ;;
        production|prod)
            return 0
            ;;
        *)
            error "Invalid environment: $env. Valid options: dev, staging, prod"
            ;;
    esac
}

# Function to create backup
create_backup() {
    local backup_name="$APP_NAME-$(date +%Y%m%d-%H%M%S)"
    local backup_path="$BACKUP_DIR/$backup_name.tar.gz"
    
    info "Creating backup: $backup_name"
    
    # Ensure backup directory exists
    mkdir -p "$BACKUP_DIR"
    
    if [ -d "$DEPLOY_DIR" ]; then
        tar -czf "$backup_path" -C "$DEPLOY_BASE" "$APP_NAME"
        info "Backup created: $backup_path"
        echo "$backup_path"  # Return backup path
    else
        warn "No existing deployment found to backup"
        echo ""
    fi
}

# Function to deploy application
deploy_application() {
    local version=$1
    local environment=$2
    
    info "Deploying $APP_NAME version $version to $environment"
    
    # Create deployment directory
    mkdir -p "$DEPLOY_DIR"
    
    # Simulate application deployment
    info "Downloading application version $version..."
    sleep 2
    
    info "Extracting application files..."
    # In real scenario: wget/curl download and extract
    echo "version=$version" > "$DEPLOY_DIR/version.txt"
    echo "environment=$environment" > "$DEPLOY_DIR/environment.txt"
    echo "deployed=$(date)" > "$DEPLOY_DIR/deployed.txt"
    
    info "Setting up configuration for $environment..."
    case "$environment" in
        production|prod)
            echo "log_level=ERROR" > "$DEPLOY_DIR/config.txt"
            echo "debug=false" >> "$DEPLOY_DIR/config.txt"
            ;;
        staging|stage)
            echo "log_level=WARN" > "$DEPLOY_DIR/config.txt"
            echo "debug=false" >> "$DEPLOY_DIR/config.txt"
            ;;
        development|dev)
            echo "log_level=DEBUG" > "$DEPLOY_DIR/config.txt"
            echo "debug=true" >> "$DEPLOY_DIR/config.txt"
            ;;
    esac
    
    # Set proper permissions
    chown -R www-data:www-data "$DEPLOY_DIR" 2>/dev/null || true
    chmod -R 755 "$DEPLOY_DIR"
    
    info "Application deployment completed"
}

# Function to manage service
manage_service() {
    local action=$1
    
    case "$action" in
        start)
            info "Starting $SERVICE_NAME service..."
            # systemctl start "$SERVICE_NAME"
            # For demo, just create a PID file
            echo $ > "/var/run/$SERVICE_NAME.pid"
            ;;
        stop)
            info "Stopping $SERVICE_NAME service..."
            # systemctl stop "$SERVICE_NAME"
            # For demo, remove PID file
            rm -f "/var/run/$SERVICE_NAME.pid"
            ;;
        restart)
            manage_service stop
            sleep 2
            manage_service start
            bin/bash
# This MUST be the first line of every bash script
# /bin/bash is the path to the bash interpreter
```

### Comments in Bash: `#`
**What it is**: The hash symbol `#` creates comments - text that bash ignores.

**Purpose**: Document your code, explain complex logic, leave notes for other developers.

```bash
#!/bin/bash
# This is a single-line comment
echo "Hello World"  # This is an inline comment

# Multi-line comments can be done like this:
# Line 1 of explanation
# Line 2 of explanation
# Line 3 of explanation
```

---

## 1. Variables in Bash - Every Detail Explained

### What is a Variable?
A **variable** is a named storage location that holds data. Think of it as a labeled box where you can store information and retrieve it later.

### The Dollar Sign `$` - Variable Reference
**What it does**: The `$` symbol tells bash "get the value stored in this variable"

**Without `$`**: You're referring to the variable name itself
**With `$`**: You're referring to the variable's value

```bash
#!/bin/bash
# Creating a variable (no $ needed)
name="Alice"

# Using a variable ($ required)
echo $name        # Outputs: Alice
echo name         # Outputs: name (literally the word "name")
```

### The Assignment Operator `=`
**Critical Rule**: NO SPACES around the equals sign!

```bash
#!/bin/bash
# ✅ CORRECT - No spaces around =
name="Alice"
age=25
city="New York"

# ❌ WRONG - These will cause errors
# name = "Alice"     # Error: command not found
# age= 25            # Error: command not found  
# city ="New York"   # Error: command not found
```

**Why no spaces?** Bash interprets spaces as command separators. `name = "Alice"` looks like a command called `name` with arguments `=` and `"Alice"`.

### Curly Braces `{}` - Variable Boundaries
**Purpose**: Define exactly where the variable name starts and ends.

**When to use**: 
- When concatenating variables with other text
- When the variable name might be ambiguous

```bash
#!/bin/bash
filename="report"

# Without braces - AMBIGUOUS
echo "Creating $filename_2024.txt"  # Looks for variable named "filename_2024"

# With braces - CLEAR
echo "Creating ${filename}_2024.txt"  # Clearly separates variable from text

# More examples
user="john"
echo "User directory: /home/${user}/documents"
echo "Backup file: ${user}_backup_$(date +%Y%m%d).tar.gz"
```

### Quotes in Bash - The Complete Guide

#### Double Quotes `""`
**Purpose**: Preserve literal value of characters but allow variable expansion and command substitution.

```bash
#!/bin/bash
name="Alice"
count=5

echo "Hello $name, you have $count messages"
# Output: Hello Alice, you have 5 messages
```

#### Single Quotes `''`
**Purpose**: Preserve literal value of ALL characters - no variable expansion.

```bash
#!/bin/bash
name="Alice"
echo 'Hello $name'  # Output: Hello $name (literally)
echo "Hello $name"  # Output: Hello Alice
```

#### No Quotes
**When safe**: Simple values without spaces or special characters
**When dangerous**: Values with spaces, special characters, or when empty

```bash
#!/bin/bash
# Safe without quotes
count=5
simple_name=alice

# Dangerous without quotes
full_name=Alice Johnson    # Error: Johnson treated as separate command
path=/home/user/my files  # Error: spaces break the assignment
```

### Variable Types Deep Dive

#### String Variables
```bash
#!/bin/bash
# String variables can contain any text
first_name="John"
last_name="Doe"
email="john.doe@company.com"
server_address="192.168.1.100:8080"

# String concatenation
full_name="$first_name $last_name"
# or
full_name="${first_name} ${last_name}"

echo "Full name: $full_name"
echo "Email: $email"
```

#### Numeric Variables
```bash
#!/bin/bash
# Bash treats everything as strings, but can do arithmetic
age=25
port=8080
count=0

# Display as strings
echo "Age: $age"
echo "Port: $port"

# Use in arithmetic (explained in detail below)
next_year=$((age + 1))
echo "Next year you'll be: $next_year"
```

### Arithmetic in Bash - The `$(())` Construct

**What it is**: Arithmetic expansion allows you to perform mathematical calculations.

**Syntax**: `$((expression))`

**Operators available**:
- `+` Addition
- `-` Subtraction  
- `*` Multiplication
- `/` Division (integer only)
- `%` Modulus (remainder)
- `**` Exponentiation
- `++` Increment
- `--` Decrement

```bash
#!/bin/bash
# Basic arithmetic
num1=10
num2=3

sum=$((num1 + num2))           # 13
difference=$((num1 - num2))    # 7
product=$((num1 * num2))       # 30
quotient=$((num1 / num2))      # 3 (integer division)
remainder=$((num1 % num2))     # 1
power=$((num1 ** 2))           # 100

echo "Sum: $sum"
echo "Difference: $difference"
echo "Product: $product"
echo "Quotient: $quotient"
echo "Remainder: $remainder"
echo "Power: $power"

# Increment/Decrement
counter=5
((counter++))    # counter becomes 6
((counter--))    # counter becomes 5
((counter += 3)) # counter becomes 8

echo "Final counter: $counter"
```

### Environment Variables

**What they are**: Variables that are available system-wide to all processes.

**How to create**: Use the `export` command.

**Common system environment variables**:
- `$USER` - Current username
- `$HOME` - User's home directory
- `$PWD` - Present working directory
- `$PATH` - Directories where system looks for commands
- `$SHELL` - User's default shell

```bash
#!/bin/bash
# Reading system environment variables
echo "Current user: $USER"
echo "Home directory: $HOME"
echo "Current directory: $PWD"
echo "Default shell: $SHELL"

# Creating custom environment variables
export DATABASE_URL="postgresql://localhost:5432/myapp"
export API_KEY="your-secret-api-key"
export ENVIRONMENT="development"

# These are now available to any child processes
echo "Database URL: $DATABASE_URL"
```

### Array Variables

**What they are**: Variables that can store multiple values.

**Syntax**: `array_name=(value1 value2 value3)`

```bash
#!/bin/bash
# Creating arrays
servers=("web01" "web02" "db01" "cache01")
ports=(80 443 3306 6379)

# Accessing array elements
echo "First server: ${servers[0]}"     # web01
echo "Second server: ${servers[1]}"    # web02

# All elements
echo "All servers: ${servers[@]}"      # web01 web02 db01 cache01

# Array length
echo "Number of servers: ${#servers[@]}"  # 4

# Loop through array
for server in "${servers[@]}"; do
    echo "Server: $server"
done
```

---

## 2. Command Line Arguments - Complete Breakdown

### What are Command Line Arguments?
**Definition**: Values passed to a script when it's executed.

**Example**: In `./script.sh web01 production 8080`, the arguments are `web01`, `production`, and `8080`.

### Special Variables for Arguments

#### `$0` - Script Name
**What it contains**: The name (or path) of the script being executed.

```bash
#!/bin/bash
echo "Script name: $0"
# If run as ./myscript.sh, outputs: Script name: ./myscript.sh
# If run as /path/to/myscript.sh, outputs: Script name: /path/to/myscript.sh
```

#### `$1, $2, $3, ...` - Positional Parameters
**What they contain**: The first, second, third (etc.) arguments passed to the script.

```bash
#!/bin/bash
echo "First argument: $1"
echo "Second argument: $2"
echo "Third argument: $3"

# Usage: ./script.sh hello world 123
# Output:
# First argument: hello
# Second argument: world  
# Third argument: 123
```

#### `$#` - Argument Count
**What it contains**: The number of arguments passed to the script.

```bash
#!/bin/bash
echo "Number of arguments: $#"

# Usage: ./script.sh one two three
# Output: Number of arguments: 3
```

#### `$@` vs `$*` - All Arguments
**`$@`**: All arguments as separate words (preserves spaces in individual arguments)
**`$*`**: All arguments as a single string

```bash
#!/bin/bash
echo "Using \$@:"
for arg in "$@"; do
    echo "  Argument: '$arg'"
done

echo "Using \$*:"
for arg in "$*"; do
    echo "  All arguments: '$arg'"
done

# Usage: ./script.sh "hello world" "foo bar"
# $@ treats "hello world" as one argument
# $* treats everything as one big string
```

### Practical Argument Handling

#### Checking Argument Count
```bash
#!/bin/bash
# Ensure user provides required arguments
if [ $# -lt 2 ]; then
    echo "Error: Not enough arguments"
    echo "Usage: $0 <server_name> <environment>"
    echo "Example: $0 web01 production"
    exit 1
fi

server=$1
environment=$2
echo "Deploying server '$server' to '$environment' environment"
```

#### Default Values
**Syntax**: `${variable:-default_value}`
**Meaning**: Use `variable` if set, otherwise use `default_value`

```bash
#!/bin/bash
server=$1
environment=$2
port=${3:-8080}  # Use $3 if provided, otherwise use 8080

echo "Server: $server"
echo "Environment: $environment"  
echo "Port: $port"

# Usage examples:
# ./script.sh web01 prod        -> Port: 8080 (default)
# ./script.sh web01 prod 9000   -> Port: 9000 (provided)
```

#### The `shift` Command
**What it does**: Removes the first argument and shifts all others down by one position.

```bash
#!/bin/bash
echo "Original arguments: $@"
echo "First argument: $1"

shift  # Remove first argument

echo "After shift: $@"
echo "New first argument: $1"

# Usage: ./script.sh one two three four
# Output:
# Original arguments: one two three four
# First argument: one
# After shift: two three four  
# New first argument: two
```

### Advanced: `getopts` Command

**What it is**: A built-in command for parsing command-line options (flags).

**Syntax**: `getopts "options" variable`

**Option string format**:
- `a` - Option `-a` with no argument
- `a:` - Option `-a` that requires an argument
- `:` at the beginning - Silent error reporting

```bash
#!/bin/bash
# Initialize variables
verbose=false
environment=""
port=8080
show_help=false

# Parse options
while getopts ":ve:p:h" opt; do
    case $opt in
        v)
            verbose=true
            echo "Verbose mode enabled"
            ;;
        e)
            environment=$OPTARG
            echo "Environment set to: $environment"
            ;;
        p)
            port=$OPTARG
            echo "Port set to: $port"
            ;;
        h)
            show_help=true
            ;;
        :)
            echo "Option -$OPTARG requires an argument"
            exit 1
            ;;
        \?)
            echo "Invalid option: -$OPTARG"
            exit 1
            ;;
    esac
done

if $show_help; then
    echo "Usage: $0 [-v] [-e environment] [-p port] [-h]"
    echo "  -v: Enable verbose output"
    echo "  -e: Set environment (dev, staging, prod)"
    echo "  -p: Set port number"
    echo "  -h: Show this help message"
    exit 0
fi

echo "Final settings:"
echo "  Verbose: $verbose"
echo "  Environment: ${environment:-not set}"
echo "  Port: $port"

# Usage examples:
# ./script.sh -v -e production -p 9000
# ./script.sh -h
# ./script.sh -e dev
```

---

## 3. Conditional Statements - Every Detail

### What are Conditionals?
**Purpose**: Allow your script to make decisions based on conditions.
**Basic structure**: "If this condition is true, do this; otherwise, do that."

### The `if` Statement Structure

#### Basic Syntax
```bash
if [ condition ]; then
    # commands to execute if condition is true
fi
```

#### Why the Spaces?
**Critical**: Spaces around brackets `[ ]` are REQUIRED!

```bash
# ✅ CORRECT
if [ $age -gt 18 ]; then

# ❌ WRONG - Will cause errors
if [$age -gt 18]; then     # No spaces around brackets
if [ $age-gt 18 ]; then    # No spaces around operator
```

**Why?** `[` is actually a command (same as `test` command), so it needs spaces like any other command.

#### Complete if-elif-else Structure
```bash
#!/bin/bash
age=20

if [ $age -lt 13 ]; then
    echo "Child"
    category="child"
elif [ $age -lt 18 ]; then
    echo "Teenager"
    category="teenager"
elif [ $age -lt 65 ]; then
    echo "Adult"
    category="adult"
else
    echo "Senior"
    category="senior"
fi

echo "Category: $category"
```

### String Comparisons - Complete Guide

#### Equality: `=` and `!=`
```bash
#!/bin/bash
environment="production"
user_role="admin"

# String equality (note: single = for comparison)
if [ "$environment" = "production" ]; then
    echo "Running in production mode"
    enable_logging=true
fi

# String inequality
if [ "$user_role" != "guest" ]; then
    echo "User has elevated privileges"
fi

# Why quotes are important
name="John Doe"
if [ "$name" = "John Doe" ]; then  # ✅ Works correctly
    echo "Name matches"
fi

if [ $name = "John Doe" ]; then    # ❌ Error! Bash sees: [ John Doe = "John Doe" ]
    echo "This will fail"
fi
```

#### Empty String Checks: `-z` and `-n`

**`-z string`**: True if string length is zero (empty)
**`-n string`**: True if string length is non-zero (not empty)

```bash
#!/bin/bash
user_input=""
password="secret123"

# Check if string is empty
if [ -z "$user_input" ]; then
    echo "User input is empty"
    echo "Please provide input"
fi

# Check if string is not empty
if [ -n "$password" ]; then
    echo "Password is provided"
    echo "Length: ${#password} characters"
fi

# Practical example: validating required variables
if [ -z "$DATABASE_URL" ]; then
    echo "Error: DATABASE_URL environment variable is not set"
    exit 1
fi
```

### Numeric Comparisons - All Operators

#### The Six Numeric Comparison Operators
- `-eq` Equal to
- `-ne` Not equal to  
- `-gt` Greater than
- `-ge` Greater than or equal to
- `-lt` Less than
- `-le` Less than or equal to

```bash
#!/bin/bash
cpu_usage=75
memory_usage=60
disk_usage=90
threshold=80

# Equal to
if [ $cpu_usage -eq 75 ]; then
    echo "CPU usage is exactly 75%"
fi

# Not equal to
if [ $memory_usage -ne 100 ]; then
    echo "Memory usage is not at maximum"
fi

# Greater than
if [ $disk_usage -gt $threshold ]; then
    echo "🚨 ALERT: Disk usage ($disk_usage%) exceeds threshold ($threshold%)"
    send_alert=true
fi

# Greater than or equal to
if [ $cpu_usage -ge $threshold ]; then
    echo "⚠️ CPU usage is at or above threshold"
fi

# Less than
if [ $memory_usage -lt $threshold ]; then
    echo "✅ Memory usage ($memory_usage%) is acceptable"
fi

# Less than or equal to
if [ $memory_usage -le $threshold ]; then
    echo "✅ Memory usage is within limits"
fi
```

### File Test Operators - Complete List

#### File Existence and Type
- `-e file` File exists (any type)
- `-f file` File exists and is a regular file
- `-d file` File exists and is a directory
- `-L file` File exists and is a symbolic link
- `-S file` File exists and is a socket
- `-p file` File exists and is a named pipe (FIFO)

```bash
#!/bin/bash
config_file="/etc/myapp/config.conf"
log_directory="/var/log/myapp"
script_file="./deploy.sh"

# Check if file exists (any type)
if [ -e "$config_file" ]; then
    echo "Config file found"
else
    echo "Config file missing - creating default"
    mkdir -p "$(dirname "$config_file")"
    touch "$config_file"
fi

# Check if it's a regular file
if [ -f "$config_file" ]; then
    echo "Config is a regular file"
    # Safe to read/write
fi

# Check if directory exists
if [ -d "$log_directory" ]; then
    echo "Log directory exists"
else
    echo "Creating log directory"
    mkdir -p "$log_directory"
fi

# Check if it's a symbolic link
if [ -L "/usr/bin/python" ]; then
    echo "Python is a symbolic link"
    echo "Points to: $(readlink /usr/bin/python)"
fi
```

#### File Permissions
- `-r file` File is readable
- `-w file` File is writable
- `-x file` File is executable
- `-s file` File exists and has size greater than zero
- `-u file` File has setuid bit set
- `-g file` File has setgid bit set

```bash
#!/bin/bash
script_file="./deployment.sh"
log_file="/var/log/app.log"

# Check if file is readable
if [ -r "$log_file" ]; then
    echo "Can read log file"
    tail -n 10 "$log_file"
else
    echo "Cannot read log file - check permissions"
fi

# Check if file is writable
if [ -w "$log_file" ]; then
    echo "Can write to log file"
    echo "$(date): Script executed" >> "$log_file"
else
    echo "Cannot write to log file"
fi

# Check if script is executable
if [ -x "$script_file" ]; then
    echo "Script is executable"
    ./"$script_file"
else
    echo "Making script executable"
    chmod +x "$script_file"
fi

# Check if file has content
if [ -s "$log_file" ]; then
    echo "Log file has content"
    echo "Size: $(wc -l < "$log_file") lines"
else
    echo "Log file is empty"
fi
```

### Logical Operators - Combining Conditions

#### AND Operator `&&`
**Both conditions must be true**

```bash
#!/bin/bash
age=25
has_license=true
country="USA"

# Method 1: Using && between separate [ ] commands
if [ $age -ge 18 ] && [ "$has_license" = true ]; then
    echo "✅ Can drive: Adult with license"
fi

# Method 2: Using [[ ]] with && inside
if [[ $age -ge 18 && "$has_license" = true ]]; then
    echo "✅ Can drive (using [[ ]])"
fi

# Complex AND condition
if [ $age -ge 21 ] && [ "$country" = "USA" ] && [ -f "id_card.txt" ]; then
    echo "✅ Can purchase alcohol in USA"
fi
```

#### OR Operator `||`
**At least one condition must be true**

```bash
#!/bin/bash
user_role="admin"
emergency_mode=false

# Method 1: Using || between separate [ ] commands
if [ "$user_role" = "admin" ] || [ "$user_role" = "superuser" ]; then
    echo "✅ User has administrative privileges"
fi

# Method 2: Using [[ ]] with || inside  
if [[ "$user_role" = "admin" || "$emergency_mode" = true ]]; then
    echo "✅ Access granted"
fi

# Practical example: multiple valid environments
environment="staging"
if [ "$environment" = "development" ] || [ "$environment" = "staging" ] || [ "$environment" = "production" ]; then
    echo "✅ Valid environment: $environment"
else
    echo "❌ Invalid environment: $environment"
    exit 1
fi
```

#### NOT Operator `!`
**Negates (reverses) the condition**

```bash
#!/bin/bash
maintenance_mode=false
lock_file="/tmp/app.lock"

# NOT with boolean
if [ ! "$maintenance_mode" = true ]; then
    echo "✅ Not in maintenance mode - proceeding"
fi

# NOT with file test
if [ ! -f "$lock_file" ]; then
    echo "✅ No lock file found - safe to proceed"
    touch "$lock_file"  # Create lock file
else
    echo "❌ Lock file exists - another process running"
    exit 1
fi

# NOT with string empty test
database_url="postgresql://localhost:5432/mydb"
if [ ! -z "$database_url" ]; then
    echo "✅ Database URL is configured"
fi
```

### Case Statements - Advanced Pattern Matching

**When to use**: When you have multiple possible values for one variable.
**Advantage**: Cleaner and more efficient than multiple if-elif statements.

#### Basic Case Statement Structure
```bash
#!/bin/bash
action=$1

case $action in
    start)
        echo "Starting the service..."
        # systemctl start myservice
        ;;
    stop)
        echo "Stopping the service..."
        # systemctl stop myservice
        ;;
    restart)
        echo "Restarting the service..."
        # systemctl restart myservice
        ;;
    status)
        echo "Checking service status..."
        # systemctl status myservice
        ;;
    *)
        echo "Unknown action: $action"
        echo "Valid actions: start, stop, restart, status"
        exit 1
        ;;
esac
```

#### Advanced Case Patterns

**Multiple patterns**: Use `|` to match multiple values
**Wildcards**: Use `*` and `?` for pattern matching
**Character classes**: Use `[...]` for character ranges

```bash
#!/bin/bash
environment=$1

case $environment in
    # Multiple exact matches
    "dev"|"development"|"devel")
        echo "🔧 Development environment"
        debug_mode=true
        log_level="DEBUG"
        ;;
    
    # Multiple staging variations
    "stage"|"staging"|"preprod")
        echo "🧪 Staging environment"
        debug_mode=true
        log_level="INFO"
        ;;
    
    # Production variations
    "prod"|"production"|"live")
        echo "🚀 Production environment"
        debug_mode=false
        log_level="ERROR"
        ;;
    
    # Pattern matching - anything starting with "test"
    test*)
        echo "🔍 Test environment: $environment"
        debug_mode=true
        log_level="DEBUG"
        ;;
    
    # Pattern matching - local environments
    local-*)
        echo "💻 Local environment: $environment"
        debug_mode=true
        log_level="DEBUG"
        ;;
    
    # Default case
    *)
        echo "❌ Unknown environment: $environment"
        echo "Valid environments:"
        echo "  - dev, development, devel"
        echo "  - stage, staging, preprod"  
        echo "  - prod, production, live"
        echo "  - test* (anything starting with 'test')"
        echo "  - local-* (anything starting with 'local-')"
        exit 1
        ;;
esac

echo "Settings applied:"
echo "  Debug mode: $debug_mode"
echo "  Log level: $log_level"
```

### The Difference Between `[ ]`, `[[ ]]`, and `(( ))`

#### `[ ]` - The Test Command
**What it is**: The original POSIX-compliant test command
**Best for**: Basic tests, maximum compatibility
**Limitations**: No pattern matching, no regex

```bash
#!/bin/bash
# Basic file and string tests
if [ -f "myfile.txt" ]; then
    echo "File exists"
fi

if [ "$USER" = "root" ]; then
    echo "Running as root"
fi

# Numeric comparisons
if [ $number -gt 10 ]; then
    echo "Number is greater than 10"
fi
```

#### `[[ ]]` - Bash Built-in Test
**What it is**: Enhanced test command built into bash
**Advantages**: Pattern matching, regex support, safer with variables
**Best for**: Complex string operations, pattern matching

```bash
#!/bin/bash
filename="error.log"

# Pattern matching (wildcards)
if [[ "$filename" == *.log ]]; then
    echo "This is a log file"
fi

# Regular expressions
email="user@example.com"
if [[ "$email" =~ ^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$ ]]; then
    echo "Valid email format"
fi

# Safer with unset variables
if [[ $undefined_variable == "test" ]]; then
    echo "This won't cause an error even if variable is unset"
fi

# Complex logical expressions  
if [[ ($age -gt 18 && "$country" == "USA") || "$admin" == "true" ]]; then
    echo "Access granted"
fi
```

#### `(( ))` - Arithmetic Evaluation
**What it is**: Arithmetic evaluation and comparison
**Best for**: Mathematical operations, numeric comparisons
**Advantages**: C-style syntax, automatic variable expansion

```bash
#!/bin/bash
number=42
counter=10

# Arithmetic comparisons (no $ needed inside)
if (( number > 40 )); then
    echo "Number is greater than 40"
fi

# Complex arithmetic conditions
if (( counter >= 10 && counter <= 20 )); then
    echo "Counter is between 10 and 20"
fi

# Arithmetic operations
(( result = number * 2 ))
(( counter++ ))
(( sum = counter + number ))

echo "Result: $result"
echo "Counter: $counter"  
echo "Sum: $sum"

# C-style conditions
if (( counter % 2 == 0 )); then
    echo "Counter is even"
else
    echo "Counter is odd"
fi
```

### When to Use Which Test Construct

```bash
#!/bin/bash
# Use [ ] for:
# - Simple file tests
# - Basic string/numeric comparisons  
# - Maximum portability (works in all POSIX shells)

if [ -f "/etc/passwd" ]; then
    echo "Password file exists"
fi

# Use [[ ]] for:
# - Pattern matching
# - Regular expressions
# - Complex string operations
# - When you need bash-specific features

if [[ "$filename" == *.conf ]]; then
    echo "Configuration file detected"
fi

# Use (( )) for:
# - Arithmetic comparisons
# - Mathematical operations
# - When you want C-style syntax

if (( cpu_usage > 80 )); then
    echo "High CPU usage detected"
fi
```

---

## 4. Loops - Mastering Repetitive Tasks

### What are Loops?
**Purpose**: Execute a block of code repeatedly until a condition is met.
**Types**: `for`, `while`, `until`
**Key concept**: Automation of repetitive tasks

### For Loops - Complete Guide

#### Basic For Loop with List
**Syntax**: `for variable in list; do commands; done`

```bash
#!/bin/bash
# Loop through a predefined list
echo "=== Checking servers ==="
for server in web01 web02 db01 cache01; do
    echo "Pinging $server..."
    if ping -c 1 -W 1 "$server" >/dev/null 2>&1; then
        echo "✅ $server is reachable"
    else
        echo "❌ $server is unreachable"
    fi
    echo "---"
done
```

#### For Loop with Arrays
**Why use arrays**: Better organization, dynamic content, easier to maintain

```bash
#!/bin/bash
# Define array of services to check
services=("nginx" "mysql" "redis" "docker" "ssh")

echo "=== Service Status Check ==="
for service in "${services[@]}"; do
    echo "Checking $service..."
    
    if systemctl is-active --quiet "$service" 2>/dev/null; then
        echo "✅ $service is running"
        # Get additional info
        status=$(systemctl show -p ActiveState "$service" --value)
        echo "   Status: $status"
    else
        echo "❌ $service is not running"
        echo "   Attempting to start..."
        # Uncomment next line to actually start service
        # sudo systemctl start "$service"
    fi
    echo "---"
done
```