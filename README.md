
# automated-remediation

A local lab demonstrating **Ansible-based application remediation** across multiple Docker environments to simulate real-world production support scenarios involving bad version rollouts and safe recovery.

This project focuses on **operational remediation**, not CI/CD, and mirrors how Application Support and SRE teams safely respond to incidents in live environments.

---

## Project Overview

This lab simulates three application instances running as Docker containers:

- **app01** → healthy version (`1.2`)
- **app02** → unhealthy version (`1.3`)
- **app03** → unhealthy version (`1.3`)

Each application exposes:
- A simple web GUI
- `/health` endpoint
- `/version` endpoint

Version `1.3` intentionally returns an unhealthy state to simulate a production regression.

Ansible is used to:
- Inspect the running state of each service
- Identify unhealthy versions
- Perform **targeted remediation**
- Leave healthy services untouched

---

## Why This Project Exists

This project demonstrates how **Application Support automation** differs from CI/CD:

- Focuses on **incident response**
- Uses checks before actions
- Limits blast radius
- Supports dry runs before execution
- Prioritizes service stability over speed

This reflects how production support teams operate in real environments.

---

## Environment

- Windows + WSL (Ubuntu)
- Docker
- Ansible
- Python 3.11+

| Container | Port | Version |
|---------|------|--------|
| app01 | 8081 | 1.2 |
| app02 | 8082 | 1.3 |
| app03 | 8083 | 1.3 |

---

## Ansible Inventory

```ini
[app_devices]
app01
app02
app03



