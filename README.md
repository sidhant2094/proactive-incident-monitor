# Proactive Incident Monitor

A Docker-based microservices project that simulates a proactive incident monitoring and self-healing platform inspired by real-world enterprise production environments.

Instead of waiting for customers to report issues, the objective is to continuously monitor services, detect failures early, execute predefined remediation playbooks, and notify engineers before incidents become customer-facing.

---

## 📌 Project Goal

Traditional support flow:

```
Issue
    ↓
Customer Notices
    ↓
Ticket Raised
    ↓
Engineer Investigates
    ↓
Issue Fixed
```

Proactive flow (this project):

```
Issue
    ↓
Monitoring Engine Detects
    ↓
Auto Remediation Attempt
    ↓
Notify Engineer (if required)
    ↓
Customer Never Notices
```

---

# 🏗️ Current Architecture

```
                    Docker Network

        ┌──────────────────────────────────┐
        │                                  │
        │       OAM Service                │
        │            │                     │
        │   HTTP Requests                 │
        │            ▼                     │
        │       BAC Service               │
        │                                  │
        └──────────────────────────────────┘
```

Current implementation includes:

- Docker Compose orchestration
- Microservice communication
- Health APIs
- Metrics APIs
- Structured logging
- Environment-based configuration
- Runtime metrics
- Resource limits

---

# 📂 Project Structure

```
proactive-incident-monitor/

│
├── docker-compose.yml
├── README.md
├── .gitignore
│
├── oam/
│   ├── app.py
│   ├── config.py
│   ├── state.py
│   ├── Dockerfile
│   ├── requirements.txt
│   └── .env
│
└── bac/
    ├── app.py
    ├── config.py
    ├── state.py
    ├── Dockerfile
    ├── requirements.txt
    └── .env
```

---

# 🛠️ Technologies

- Python
- Flask
- Docker
- Docker Compose
- REST APIs

---

# 🚀 Running the Project

Clone the repository

```bash
git clone https://github.com/<your-username>/proactive-incident-monitor.git
```

Go into the project

```bash
cd proactive-incident-monitor
```

Build and start the services

```bash
docker compose up --build
```

---

# 📡 Available Endpoints

## OAM

| Endpoint | Description |
|----------|-------------|
| `/` | Service information |
| `/health` | Health status |
| `/metrics` | Runtime metrics |
| `/call-bac` | Calls BAC service |

---

## BAC

| Endpoint | Description |
|----------|-------------|
| `/` | Service information |
| `/health` | Health status |
| `/metrics` | Runtime metrics |
| `/status` | BAC status endpoint |

---

# 🗺️ Roadmap

## Phase 1 ✅

- [x] Dockerized microservices
- [x] OAM & BAC communication
- [x] Docker networking
- [x] Runtime metrics
- [x] Health endpoints
- [x] Structured logging

---

## Phase 2 🚧

- [x] Monitoring Engine
- [x] Continuous Health Checks
- [ ] Service Discovery

---

## Phase 3

- [ ] Incident Detection
- [ ] Failure Classification
- [ ] Alert Generation

---

## Phase 4

- [ ] Automated Remediation
- [ ] Playbook Engine
- [ ] Retry Mechanisms

---

## Phase 5

- [ ] Email Notifications
- [ ] Teams/Slack Integration

---

## Phase 6

- [ ] Monitoring Dashboard
- [ ] Service Health Visualization
- [ ] Incident Timeline

---

## Future Scope

- Prometheus Integration
- Grafana Dashboards
- Kubernetes Deployment
- Predictive Incident Detection
- AI-assisted Root Cause Analysis

---

# 📖 Learning Objectives

This project demonstrates:

- Microservices
- Containerization
- Docker Networking
- Service Discovery
- REST Communication
- Health Monitoring
- Runtime Metrics
- Distributed System Fundamentals

---

## Author

**Sidhant Malik**

Built as a hands-on exploration of proactive incident monitoring and self-healing systems.
