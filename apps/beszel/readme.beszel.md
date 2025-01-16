# Beszel

## What is Beszel?

- **Lightweight** 
  - Smaller & less resource hungry
- **Simple**
  - Easy setup, No network dependency
- **Stats & Alerts**
  - CPU, Memory, Network usage history per container
  - CPU, Memory, Disk, Netork, Bandwidth, Temperature, System Status alerts
- **Multi User**
  - RBAC, User Management, User Profiles
- **Oauth**
  - Mulitple Oauth Providers
- **Automatic Backup**
  - Disk or S3 Save and Restore
- **REST API**
  - Use with Custom scripts or Apps

## Setup

- **Hub**
  - Web App Dashboard built on Pocketbase
- **Agent**
  - SSH Server running on each system

## Installation

1. Start the hub (docker-compose.beszel.yml)
2. Default http://localhost:8090 - Create an admin user
3. *Click* 'Add System' - name & host of system to be monitored
4. *Click* 'Copy docker compose' - Copy Agent's docker-compose.yml