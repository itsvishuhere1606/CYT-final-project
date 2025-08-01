# CYT160 Final Project – End-to-End IoT Security Pipeline

## Overview
This project simulates an IoT security pipeline with:
- Python-based temperature sensor
- MQTT/Elastic Cloud ingestion
- Suricata IDS threat detection
- Real-time visualization in Kibana

## Setup Instructions

### 1. Clone or download project files to your VM/Pi.

### 2. Python Sensor Setup

#### a) Create a virtual environment and install dependencies
```bash
sudo apt update
sudo apt install python3-venv python3-full -y
python3 -m venv ~/tempsim
source ~/tempsim/bin/activate
pip install requests
```

#### b) Save `tempsensor.py` as shown below.

### 3. Configure the Python Sensor

- Update your Elastic Cloud URL, username, and password in the script.

### 4. (Optional) Make sensor auto-start at boot
Create `/etc/systemd/system/tempsensor.service`:
```
[Unit]
Description=Simulated Temperature Sensor Service
After=network.target

[Service]
Type=simple
User=YOURUSERNAME
WorkingDirectory=/home/YOURUSERNAME
ExecStart=/home/YOURUSERNAME/tempsim/bin/python /home/YOURUSERNAME/tempsensor.py
Environment=PYTHONUNBUFFERED=1
Restart=on-failure

[Install]
WantedBy=multi-user.target
```
Then:
```bash
sudo systemctl daemon-reload
sudo systemctl enable tempsensor.service
sudo systemctl start tempsensor.service
```

### 5. View Sensor Data in Kibana

- Go to Discover: Data view = `temperature-sensor*`
- Build a Lens visualization: X-axis = `@timestamp`, Y-axis = `temperature`

### 6. Simulate Attacks for Suricata

- Use `nmap`, `hping3`, or `scapy` to simulate scans/DoS/malformed packets.
- Alerts will appear in Kibana dashboard (data view = `filebeat-*`).

### 7. Dashboard Visualization

- Add panels: Temperature over time, Top alert signatures, Top source IPs, Alerts over time, Raw alerts table.

## Contact
Group 1
**Student:** Vishesh,Navneet Kaur, Anurag Jabegu, Darien James
**Course:** CYT160  
**Date:** July 2025
