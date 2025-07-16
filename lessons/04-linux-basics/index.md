# Complete Networking Tutorial for DevOps

## Table of Contents
1. [Introduction to Networking Fundamentals](#introduction)
2. [OSI Model](#osi-model)
3. [IP Addresses](#ip-addresses)
4. [MAC Addresses](#mac-addresses)
5. [Subnet Masks and Subnetting](#subnet-masks)
6. [Hosts and Networking](#hosts)
7. [Ports and Port Management](#ports)
8. [TCP and UDP Protocols](#tcp-udp)
9. [Linux Networking Commands](#linux-commands)
10. [Practical Examples and Exercises](#practical-examples)

---

## 1. Introduction to Networking Fundamentals {#introduction}

Computer networking is the foundation of modern IT infrastructure. Understanding networking concepts is crucial for DevOps engineers who need to manage, deploy, and troubleshoot distributed systems.

### Key Networking Concepts

**Network**: A collection of interconnected devices that can communicate with each other.

**Protocol**: A set of rules that govern how data is transmitted over a network. Common protocols include TCP/IP, HTTP, SSH, and DNS.

**Packet**: A unit of data that is transmitted over a network, containing both the actual data and routing information.

**Router**: A device that forwards data packets between computer networks.

**Switch**: A device that connects devices within a single network and uses MAC addresses to forward data.

---

## 2. OSI Model {#osi-model}
[osi](./img/osi.png)

The OSI (Open Systems Interconnection) model is a conceptual framework that describes how network communications occur in seven layers.

### Layer 7: Application Layer
- **Purpose**: Provides network services directly to applications
- **Protocols**: HTTP, HTTPS, FTP, SMTP, DNS, SSH
- **Examples**: Web browsers, email clients, file transfer applications
- **DevOps Relevance**: Application deployment, API communication, web services

### Layer 6: Presentation Layer
- **Purpose**: Data translation, encryption, and compression
- **Functions**: Character encoding, data encryption/decryption, compression
- **Examples**: SSL/TLS encryption, JPEG compression, ASCII encoding
- **DevOps Relevance**: Certificate management, data security

### Layer 5: Session Layer
- **Purpose**: Manages sessions between applications
- **Functions**: Session establishment, maintenance, and termination
- **Examples**: SQL sessions, RPC calls, NetBIOS
- **DevOps Relevance**: Database connections, API session management

### Layer 4: Transport Layer
- **Purpose**: Reliable data transfer between systems
- **Protocols**: TCP, UDP
- **Functions**: Segmentation, flow control, error detection
- **DevOps Relevance**: Port management, load balancing, service communication

### Layer 3: Network Layer
- **Purpose**: Routing packets between different networks
- **Protocols**: IP, ICMP, OSPF, BGP
- **Functions**: Logical addressing, path determination, packet forwarding
- **DevOps Relevance**: Network routing, VPN configuration, cloud networking

### Layer 2: Data Link Layer
- **Purpose**: Node-to-node data transfer within the same network
- **Protocols**: Ethernet, Wi-Fi, PPP
- **Functions**: MAC addressing, frame synchronization, error detection
- **DevOps Relevance**: Switch configuration, VLAN management

### Layer 1: Physical Layer
- **Purpose**: Transmission of raw bits over physical medium
- **Components**: Cables, hubs, repeaters, network interface cards
- **Functions**: Electrical signals, cable specifications, connector types
- **DevOps Relevance**: Hardware troubleshooting, cable management

---

## 3. IP Addresses {#ip-addresses}

IP (Internet Protocol) addresses are unique identifiers assigned to devices on a network.

### IPv4 Addresses
[osi](./img/ip.png)
IPv4 addresses are 32-bit numbers represented in dotted decimal notation (e.g., 192.168.1.100).

**Structure:**
- 4 octets (8 bits each)
- Range: 0.0.0.0 to 255.255.255.255
- Total possible addresses: ~4.3 billion

**Address Classes:**
- **Class A**: 1.0.0.0 to 126.255.255.255 (Large networks, /8 subnet)
- **Class B**: 128.0.0.0 to 191.255.255.255 (Medium networks, /16 subnet)
- **Class C**: 192.0.0.0 to 223.255.255.255 (Small networks, /24 subnet)
- **Class D**: 224.0.0.0 to 239.255.255.255 (Multicast)
- **Class E**: 240.0.0.0 to 255.255.255.255 (Reserved)

**Private IP Ranges:**
- Class A: 10.0.0.0 to 10.255.255.255
- Class B: 172.16.0.0 to 172.31.255.255
- Class C: 192.168.0.0 to 192.168.255.255

**Special Addresses:**
- **127.0.0.1**: Localhost (loopback)
- **0.0.0.0**: Default route or "any" address
- **255.255.255.255**: Broadcast address

### IPv6 Addresses

IPv6 addresses are 128-bit numbers represented in hexadecimal notation.

**Structure:**
- 8 groups of 4 hexadecimal digits
- Example: 2001:0db8:85a3:0000:0000:8a2e:0370:7334
- Shortened: 2001:db8:85a3::8a2e:370:7334

**Types:**
- **Unicast**: One-to-one communication
- **Multicast**: One-to-many communication
- **Anycast**: One-to-nearest communication

---

## 4. MAC Addresses {#mac-addresses}
[osi](./img/mac.png)
MAC (Media Access Control) addresses are unique identifiers assigned to network interface cards.

### MAC Address Structure

**Format**: 48-bit address represented in hexadecimal
**Example**: 00:1A:2B:3C:4D:5E or 00-1A-2B-3C-4D-5E

**Components:**
- **OUI (Organizationally Unique Identifier)**: First 3 bytes (identifies manufacturer)
- **NIC (Network Interface Controller)**: Last 3 bytes (unique device identifier)

### MAC Address Types

**Unicast**: First bit of first byte is 0 (individual device)
**Multicast**: First bit of first byte is 1 (group of devices)
**Broadcast**: All bits set to 1 (FF:FF:FF:FF:FF:FF)

### MAC vs IP Addresses

| MAC Address | IP Address |
|-------------|------------|
| Layer 2 (Data Link) | Layer 3 (Network) |
| Hardware-based | Software-based |
| Permanent | Can change |
| Local network scope | Global scope |
| 48-bit | 32-bit (IPv4) or 128-bit (IPv6) |

---

## 5. Subnet Masks and Subnetting {#subnet-masks}
[osi](./img/subnet.png)
Subnet masks divide IP networks into smaller subnetworks to improve security and performance.

### Subnet Mask Basics

**Purpose**: Determines which part of an IP address is the network portion and which is the host portion.

**Default Subnet Masks:**
- Class A: 255.0.0.0 (/8)
- Class B: 255.255.0.0 (/16)
- Class C: 255.255.255.0 (/24)

### CIDR Notation

**CIDR (Classless Inter-Domain Routing)**: Modern way to represent subnet masks.

**Examples:**
- 192.168.1.0/24 (subnet mask: 255.255.255.0)
- 10.0.0.0/8 (subnet mask: 255.0.0.0)
- 172.16.0.0/16 (subnet mask: 255.255.0.0)

### Subnetting Examples

**Example 1**: Subnet 192.168.1.0/24 into 4 subnets
- Original: 192.168.1.0/24 (256 hosts)
- Subnets: /26 (64 hosts each)
  - 192.168.1.0/26 (192.168.1.1 - 192.168.1.62)
  - 192.168.1.64/26 (192.168.1.65 - 192.168.1.126)
  - 192.168.1.128/26 (192.168.1.129 - 192.168.1.190)
  - 192.168.1.192/26 (192.168.1.193 - 192.168.1.254)

**Example 2**: Calculate usable hosts
- Network: 10.0.0.0/22
- Hosts per subnet: 2^(32-22) - 2 = 1022 usable hosts
- Network range: 10.0.0.0 - 10.0.3.255

### Subnet Calculation Formula

```
Number of subnets = 2^(subnet bits)
Number of hosts per subnet = 2^(host bits) - 2
```

---

## 6. Hosts and Networking {#hosts}

A host is any device connected to a network that can send or receive data.

### Types of Hosts

**End Hosts**: Devices that generate or consume data
- Computers, smartphones, servers, IoT devices

**Intermediate Hosts**: Devices that forward data
- Routers, switches, gateways, proxy servers

### Host Identification

**Hostname**: Human-readable name (e.g., web-server-01)
**FQDN (Fully Qualified Domain Name)**: Complete hostname (e.g., web-server-01.example.com)
**Host Resolution**: Process of converting hostnames to IP addresses (DNS)

### Host File

Location and examples:
- **Linux/Unix**: /etc/hosts
- **Windows**: C:\Windows\System32\drivers\etc\hosts

Example host file entries:
```
127.0.0.1       localhost
192.168.1.10    web-server
192.168.1.20    database-server
::1             localhost
```

### Network Host Configuration

**Static IP Configuration**:
- IP address: 192.168.1.100
- Subnet mask: 255.255.255.0
- Default gateway: 192.168.1.1
- DNS servers: 8.8.8.8, 8.8.4.4

**Dynamic IP Configuration (DHCP)**:
- Automatic assignment of IP configuration
- Lease time management
- Reservation for specific devices

---

## 7. Ports and Port Management {#ports}

Ports are logical endpoints for network communication, allowing multiple services to run on a single host.

### Port Basics
[osi](./img/ports.png)

**Port Number**: 16-bit number (0-65535)
**Socket**: Combination of IP address and port number (192.168.1.100:80)

### Port Categories

**Well-Known Ports (0-1023)**:
- 20/21: FTP (File Transfer Protocol)
- 22: SSH (Secure Shell)
- 23: Telnet
- 25: SMTP (Simple Mail Transfer Protocol)
- 53: DNS (Domain Name System)
- 80: HTTP (HyperText Transfer Protocol)
- 110: POP3 (Post Office Protocol)
- 143: IMAP (Internet Message Access Protocol)
- 443: HTTPS (HTTP Secure)
- 993: IMAPS (IMAP Secure)
- 995: POP3S (POP3 Secure)

**Registered Ports (1024-49151)**:
- 1433: Microsoft SQL Server
- 1521: Oracle Database
- 3306: MySQL
- 3389: Remote Desktop Protocol (RDP)
- 5432: PostgreSQL
- 5672: AMQP (Advanced Message Queuing Protocol)
- 6379: Redis
- 8080: HTTP Alternative
- 8443: HTTPS Alternative

**Dynamic/Private Ports (49152-65535)**:
- Used for client-side connections
- Ephemeral ports assigned automatically

### Port States

**Open**: Port is accepting connections
**Closed**: Port is not accepting connections
**Filtered**: Port is blocked by firewall

### Port Security

**Firewall Rules**: Control which ports are accessible
**Port Scanning**: Technique to discover open ports
**Service Hardening**: Disable unnecessary services and ports

---

## 8. TCP and UDP Protocols {#tcp-udp}
[osi](./img/udptcp.png)
TCP and UDP are the primary transport layer protocols in the TCP/IP suite.

### TCP (Transmission Control Protocol)

**Characteristics**:
- Connection-oriented protocol
- Reliable data delivery
- Ordered data transmission
- Error detection and correction
- Flow control and congestion control

**TCP Header Structure**:
- Source Port (16 bits)
- Destination Port (16 bits)
- Sequence Number (32 bits)
- Acknowledgment Number (32 bits)
- Control Flags (URG, ACK, PSH, RST, SYN, FIN)
- Window Size (16 bits)
- Checksum (16 bits)

**TCP Three-Way Handshake**:
1. Client sends SYN packet
2. Server responds with SYN-ACK packet
3. Client sends ACK packet
4. Connection established

**TCP Connection Termination**:
1. Client sends FIN packet
2. Server responds with ACK packet
3. Server sends FIN packet
4. Client responds with ACK packet
5. Connection closed

**TCP Use Cases**:
- Web browsing (HTTP/HTTPS)
- Email (SMTP, POP3, IMAP)
- File transfer (FTP, SSH)
- Remote access (SSH, Telnet)
- Database connections

### UDP (User Datagram Protocol)

**Characteristics**:
- Connectionless protocol
- Unreliable data delivery (best-effort)
- No ordering guarantee
- No error recovery
- Low overhead
- Fast transmission

**UDP Header Structure**:
- Source Port (16 bits)
- Destination Port (16 bits)
- Length (16 bits)
- Checksum (16 bits)

**UDP Use Cases**:
- DNS queries
- DHCP
- Video streaming
- Online gaming
- VoIP (Voice over IP)
- Network monitoring (SNMP)
- Time synchronization (NTP)

### TCP vs UDP Comparison

| Feature | TCP | UDP |
|---------|-----|-----|
| Connection | Connection-oriented | Connectionless |
| Reliability | Reliable | Unreliable |
| Ordering | Ordered | Unordered |
| Speed | Slower | Faster |
| Overhead | High | Low |
| Error Checking | Yes | Basic |
| Flow Control | Yes | No |
| Congestion Control | Yes | No |

---

## 9. Linux Networking Commands {#linux-commands}

Essential Linux commands for network configuration, troubleshooting, and monitoring.

### Basic Network Information

**ifconfig**: Configure and display network interfaces
```bash
# Display all network interfaces
ifconfig

# Display specific interface
ifconfig eth0

# Configure IP address
sudo ifconfig eth0 192.168.1.100 netmask 255.255.255.0

# Enable/disable interface
sudo ifconfig eth0 up
sudo ifconfig eth0 down
```

**ip**: Modern replacement for ifconfig
```bash
# Display all interfaces
ip addr show
ip a

# Display specific interface
ip addr show eth0

# Configure IP address
sudo ip addr add 192.168.1.100/24 dev eth0

# Enable/disable interface
sudo ip link set eth0 up
sudo ip link set eth0 down

# Display routing table
ip route show
ip r
```

### Network Connectivity Testing

**ping**: Test network connectivity
```bash
# Ping IP address
ping 192.168.1.1

# Ping hostname
ping google.com

# Ping with specific count
ping -c 4 google.com

# Ping with interval
ping -i 2 google.com

# Ping IPv6
ping6 2001:4860:4860::8888
```

**traceroute**: Trace network path
```bash
# Trace route to destination
traceroute google.com

# Trace route with IP addresses only
traceroute -n google.com

# Trace route with specific protocol
traceroute -I google.com  # ICMP
traceroute -T google.com  # TCP
```

**mtr**: Continuous traceroute
```bash
# Real-time traceroute
mtr google.com

# Run specific number of cycles
mtr -c 10 google.com
```

### DNS Resolution

**nslookup**: DNS lookup utility
```bash
# Forward DNS lookup
nslookup google.com

# Reverse DNS lookup
nslookup 8.8.8.8

# Query specific DNS server
nslookup google.com 8.8.8.8

# Query specific record type
nslookup -type=MX google.com
```

**dig**: Advanced DNS lookup
```bash
# Basic DNS query
dig google.com

# Query specific record type
dig google.com MX
dig google.com AAAA

# Query specific DNS server
dig @8.8.8.8 google.com

# Reverse DNS lookup
dig -x 8.8.8.8

# Trace DNS resolution
dig +trace google.com
```

**host**: Simple DNS lookup
```bash
# Forward lookup
host google.com

# Reverse lookup
host 8.8.8.8

# Query specific record type
host -t MX google.com
```

### Port and Service Management

**netstat**: Network statistics
```bash
# Display all connections
netstat -a

# Display listening ports
netstat -l

# Display TCP connections
netstat -t

# Display UDP connections
netstat -u

# Display with process information
netstat -p

# Display with numeric addresses
netstat -n

# Common combinations
netstat -tlnp  # TCP listening ports with process info
netstat -ulnp  # UDP listening ports with process info
netstat -tuln  # All listening ports
```

**ss**: Modern replacement for netstat
```bash
# Display all connections
ss -a

# Display listening ports
ss -l

# Display TCP connections
ss -t

# Display UDP connections
ss -u

# Display with process information
ss -p

# Display with numeric addresses
ss -n

# Common combinations
ss -tlnp  # TCP listening ports with process info
ss -ulnp  # UDP listening ports with process info
ss -tuln  # All listening ports
```

**lsof**: List open files and network connections
```bash
# Display network connections
lsof -i

# Display connections for specific port
lsof -i :80
lsof -i :22

# Display connections for specific protocol
lsof -i tcp
lsof -i udp

# Display connections for specific host
lsof -i @192.168.1.100
```

### Network Scanning and Security

**nmap**: Network scanning tool
```bash
# Basic host scan
nmap 192.168.1.1

# Scan specific ports
nmap -p 80,443 192.168.1.1

# Scan port range
nmap -p 1-1000 192.168.1.1

# Scan entire subnet
nmap 192.168.1.0/24

# Service detection
nmap -sV 192.168.1.1

# Operating system detection
nmap -O 192.168.1.1

# Aggressive scan
nmap -A 192.168.1.1
```

**telnet**: Test port connectivity
```bash
# Test if port is open
telnet 192.168.1.100 80
telnet google.com 80

# Test SMTP server
telnet mail.example.com 25
```

**nc (netcat)**: Network Swiss Army knife
```bash
# Test port connectivity
nc -z 192.168.1.100 80

# Port scan
nc -z 192.168.1.100 1-1000

# Listen on port
nc -l 8080

# Transfer files
# On receiver: nc -l 8080 > file.txt
# On sender: nc 192.168.1.100 8080 < file.txt
```

### Routing and Gateway Management

**route**: Display and modify routing table
```bash
# Display routing table
route -n

# Add default gateway
sudo route add default gw 192.168.1.1

# Add specific route
sudo route add -net 10.0.0.0/8 gw 192.168.1.1

# Delete route
sudo route del -net 10.0.0.0/8
```

**ip route**: Modern routing management
```bash
# Display routing table
ip route show

# Add default gateway
sudo ip route add default via 192.168.1.1

# Add specific route
sudo ip route add 10.0.0.0/8 via 192.168.1.1

# Delete route
sudo ip route del 10.0.0.0/8
```

### Network Monitoring

**iftop**: Display bandwidth usage
```bash
# Monitor interface traffic
sudo iftop

# Monitor specific interface
sudo iftop -i eth0

# Display port information
sudo iftop -P
```

**nethogs**: Display process network usage
```bash
# Monitor network usage by process
sudo nethogs

# Monitor specific interface
sudo nethogs eth0
```

**tcpdump**: Packet capture and analysis
```bash
# Capture all traffic
sudo tcpdump

# Capture on specific interface
sudo tcpdump -i eth0

# Capture specific protocol
sudo tcpdump tcp
sudo tcpdump udp
sudo tcpdump icmp

# Capture specific port
sudo tcpdump port 80
sudo tcpdump port 22

# Capture and save to file
sudo tcpdump -w capture.pcap

# Read from file
tcpdump -r capture.pcap

# Verbose output
sudo tcpdump -v
sudo tcpdump -vv
sudo tcpdump -vvv
```

### ARP (Address Resolution Protocol)

**arp**: ARP table management
```bash
# Display ARP table
arp -a

# Display ARP table in numeric format
arp -n

# Add static ARP entry
sudo arp -s 192.168.1.100 00:11:22:33:44:55

# Delete ARP entry
sudo arp -d 192.168.1.100
```

**ip neigh**: Modern ARP management
```bash
# Display ARP table
ip neigh show

# Add static ARP entry
sudo ip neigh add 192.168.1.100 lladdr 00:11:22:33:44:55 dev eth0

# Delete ARP entry
sudo ip neigh del 192.168.1.100 dev eth0
```

### Advanced Network Configuration

**ethtool**: Ethernet device configuration
```bash
# Display interface information
ethtool eth0

# Display interface statistics
ethtool -S eth0

# Set interface speed and duplex
sudo ethtool -s eth0 speed 1000 duplex full autoneg off
```

**iwconfig**: Wireless interface configuration
```bash
# Display wireless interfaces
iwconfig

# Set wireless network
sudo iwconfig wlan0 essid "MyNetwork"
sudo iwconfig wlan0 key s:mypassword
```

---

## 10. Practical Examples and Exercises {#practical-examples}

### Exercise 1: Network Discovery

**Objective**: Discover devices on your local network

**Steps**:
1. Find your IP address and subnet:
   ```bash
   ip addr show
   ```

2. Scan your local network:
   ```bash
   nmap -sn 192.168.1.0/24
   ```

3. Get detailed information about discovered hosts:
   ```bash
   nmap -A 192.168.1.1
   ```

### Exercise 2: Port Scanning and Service Identification

**Objective**: Identify running services on a server

**Steps**:
1. Scan common ports:
   ```bash
   nmap -p 21,22,23,25,53,80,110,143,443,993,995 192.168.1.100
   ```

2. Perform service detection:
   ```bash
   nmap -sV -p 1-1000 192.168.1.100
   ```

3. Check listening services locally:
   ```bash
   ss -tlnp
   ```

### Exercise 3: Network Troubleshooting

**Objective**: Diagnose network connectivity issues

**Steps**:
1. Test basic connectivity:
   ```bash
   ping 8.8.8.8
   ```

2. Test DNS resolution:
   ```bash
   nslookup google.com
   dig google.com
   ```

3. Trace network path:
   ```bash
   traceroute google.com
   ```

4. Check routing table:
   ```bash
   ip route show
   ```

### Exercise 4: Subnetting Practice

**Objective**: Calculate subnet information

**Problem**: You have been assigned 192.168.10.0/24 and need to create 8 subnets.

**Solution**:
1. Calculate required subnet bits: 2^3 = 8 subnets (need 3 bits)
2. New subnet mask: /24 + 3 = /27 (255.255.255.224)
3. Hosts per subnet: 2^5 - 2 = 30 hosts
4. Subnet ranges:
   - 192.168.10.0/27 (192.168.10.1-192.168.10.30)
   - 192.168.10.32/27 (192.168.10.33-192.168.10.62)
   - 192.168.10.64/27 (192.168.10.65-192.168.10.94)
   - ... and so on

### Exercise 5: Packet Capture Analysis

**Objective**: Capture and analyze network traffic

**Steps**:
1. Start packet capture:
   ```bash
   sudo tcpdump -i eth0 -w traffic.pcap
   ```

2. Generate some traffic:
   ```bash
   curl http://example.com
   ```

3. Stop capture and analyze:
   ```bash
   tcpdump -r traffic.pcap
   ```

### Exercise 6: Network Performance Testing

**Objective**: Test network performance between two hosts

**Steps**:
1. On server (listener):
   ```bash
   iperf3 -s
   ```

2. On client (sender):
   ```bash
   iperf3 -c server_ip_address
   ```

3. Test UDP performance:
   ```bash
   iperf3 -c server_ip_address -u
   ```

### Common Troubleshooting Scenarios

**Scenario 1**: Cannot reach a website
1. Check local connectivity: `ping 127.0.0.1`
2. Check gateway: `ping 192.168.1.1`
3. Check DNS: `nslookup google.com`
4. Check external connectivity: `ping 8.8.8.8`
5. Check routing: `traceroute google.com`

**Scenario 2**: Service not accessible
1. Check if service is running: `ss -tlnp | grep :80`
2. Check firewall rules: `sudo iptables -L`
3. Test port connectivity: `telnet server_ip 80`
4. Check service logs: `sudo journalctl -u apache2`

**Scenario 3**: Slow network performance
1. Check interface status: `ethtool eth0`
2. Monitor bandwidth usage: `iftop`
3. Check for packet loss: `ping -c 100 8.8.8.8`
4. Analyze network traffic: `tcpdump -i eth0`

### Best Practices for DevOps

1. **Security**: Always close unused ports and services
2. **Monitoring**: Implement network monitoring and alerting
3. **Documentation**: Keep network diagrams and configurations updated
4. **Automation**: Use configuration management tools for network setup
5. **Backup**: Maintain backups of network configurations
6. **Testing**: Regularly test network connectivity and performance
7. **Logging**: Enable and monitor network logs
8. **Segmentation**: Use VLANs and subnets to isolate network traffic

---
