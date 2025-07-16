# DevSecOps Network Security Investigation Lab

## Project Overview

This lab simulates a real-world cybersecurity incident investigation where students must use their Linux system administration and networking skills to uncover a hidden message. The lab integrates networking concepts, Ubuntu permissions, file systems, piping, redirection, and package management to solve a multi-stage security puzzle.

## Learning Objectives

By completing this lab, students will demonstrate proficiency in:

1. **Linux File System Navigation**
   - Understanding directory structures
   - File permissions and ownership
   - Hidden files and directories

2. **Ubuntu Package Management**
   - Using APT for package installation
   - Managing repositories
   - Dependency resolution

3. **File Operations and Permissions**
   - chmod, chown, chgrp commands
   - Understanding octal and symbolic permissions
   - Special permissions (sticky bit, SUID, SGID)

4. **Piping and Redirection**
   - Command chaining with pipes
   - Input/output redirection
   - Text processing with grep, sed, awk

5. **Networking Concepts**
   - IP address manipulation
   - Port scanning simulation
   - Network configuration analysis

6. **Binary and Hexadecimal Operations**
   - Number base conversions
   - Hex encoding/decoding
   - Binary file analysis

## Lab Scenario

**Background**: Your organization's security team has detected suspicious activity on a Ubuntu server. As a DevSecOps engineer, you've been tasked with investigating the incident. Intelligence suggests that an attacker has hidden a secret message across multiple system components using various encoding methods.

**Mission**: Discover the hidden word by completing a series of interconnected challenges that simulate real security investigation techniques.

## Technical Requirements

### System Requirements
- Ubuntu 20.04 LTS or later
- Terminal access with sudo privileges
- Internet connection for package installation
- Basic text editor (nano, vim, or gedit)

### Required Tools
Students will need to install and use:
- `hexdump` - for binary/hex analysis
- `base64` - for encoding/decoding
- `netstat` - for network analysis
- `grep`, `sed`, `awk` - for text processing
- `curl` - for network requests
- `bc` - for mathematical calculations

### Skills Prerequisites
- Basic Linux command line navigation
- Understanding of file permissions
- Familiarity with text editors
- Basic networking concepts

## Lab Structure

### Milestone 1: System Reconnaissance (20 points)
**Objective**: Gather system information and identify suspicious files
**Skills Tested**: File system navigation, permissions, hidden files
**Expected Time**: 30 minutes

### Milestone 2: Package Investigation (25 points)
**Objective**: Use APT to investigate installed packages and find clues
**Skills Tested**: APT commands, package management, log analysis
**Expected Time**: 45 minutes

### Milestone 3: Permission Analysis (25 points)
**Objective**: Analyze file permissions and ownership patterns
**Skills Tested**: chmod, chown, octal permissions, special permissions
**Expected Time**: 40 minutes

### Milestone 4: Network Forensics (30 points)
**Objective**: Investigate network configurations and connections
**Skills Tested**: Network commands, port analysis, IP manipulation
**Expected Time**: 50 minutes

### Milestone 5: Data Processing Pipeline (35 points)
**Objective**: Use piping and redirection to process encrypted data
**Skills Tested**: Complex pipes, redirection, text processing
**Expected Time**: 60 minutes

### Milestone 6: Binary Decoding (40 points)
**Objective**: Decode binary and hexadecimal data to reveal final message
**Skills Tested**: Base conversions, hex operations, binary analysis
**Expected Time**: 45 minutes

### Final Challenge: Message Assembly (25 points)
**Objective**: Combine all discovered clues to reveal the secret word
**Skills Tested**: Integration of all previous skills
**Expected Time**: 30 minutes

## Assessment Criteria

### Technical Proficiency (70%)
- Correct command usage and syntax
- Proper understanding of file permissions
- Effective use of piping and redirection
- Accurate binary/hex conversions
- Network analysis accuracy

### Problem-Solving Approach (20%)
- Logical progression through milestones
- Creative use of commands
- Troubleshooting abilities
- Documentation of process

### Security Awareness (10%)
- Understanding of security implications
- Recognition of suspicious patterns
- Proper handling of sensitive data

## Grading Scale

| Score Range | Grade | Description |
|-------------|-------|-------------|
| 180-200 | A+ | Exceptional performance, creative solutions |
| 160-179 | A | Excellent understanding, all milestones completed |
| 140-159 | B+ | Good performance, minor issues |
| 120-139 | B | Satisfactory completion, some struggles |
| 100-119 | C+ | Basic understanding, significant help needed |
| 80-99 | C | Minimum requirements met |
| Below 80 | F | Insufficient demonstration of skills |

## Submission Requirements

### Command Documentation
Students must document:
- All commands used with explanations
- Output of key commands
- Problem-solving approach for each milestone
- Final discovered word with proof

### File Submissions
- Screenshots of terminal sessions
- Text files with command outputs
- Documentation of investigation process
- Final report with discovered clues

## Setup Instructions for Instructors

### Lab Environment Preparation
1. Create base Ubuntu VM or container
2. Install required packages
3. Set up hidden files and directories
4. Configure permissions and ownership
5. Create encoded data files
6. Set up network simulation files

### Answer Key Components
- Step-by-step solution guide
- Expected command outputs
- Common troubleshooting scenarios
- Alternative solution approaches

## Security Considerations

### Lab Safety
- All activities are contained within the lab environment
- No actual security vulnerabilities are exploited
- Simulated data only, no real sensitive information
- Network activities are local or controlled

### Educational Focus
- Emphasis on defensive security techniques
- Proper investigation methodologies
- Legal and ethical considerations
- Professional security practices

## Extension Activities

### Advanced Challenges
- Log analysis with complex patterns
- Network packet simulation
- Advanced encoding schemes
- Scripting automation

### Real-World Applications
- Incident response procedures
- Security auditing techniques
- Compliance checking
- Automation scripting

## Resources and References

### Documentation
- Ubuntu Manual Pages
- Linux File System Hierarchy
- Network Security Best Practices
- Incident Response Procedures

### Tools and Commands
- Complete reference for all required commands
- Common troubleshooting techniques
- Performance optimization tips
- Security hardening guidelines

## Timeline and Milestones

### Week 1: Setup and Milestone 1-2
- Lab environment setup
- System reconnaissance
- Package investigation

### Week 2: Milestone 3-4
- Permission analysis
- Network forensics

### Week 3: Milestone 5-6
- Data processing pipeline
- Binary decoding

### Week 4: Final Challenge and Submission
- Message assembly
- Documentation completion
- Peer review and discussion

## Success Metrics

### Individual Achievement
- Completion rate of milestones
- Accuracy of command usage
- Quality of documentation
- Discovery of final word

### Class Performance
- Average completion time
- Common challenges identified
- Skill development progression
- Engagement level

This comprehensive lab provides hands-on experience with essential DevSecOps skills while maintaining an engaging investigative narrative that motivates students to complete all challenges.