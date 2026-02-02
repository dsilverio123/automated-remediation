
# automated-remediation

A local lab demonstrating **Ansible-based application remediation** across multiple Docker environments to simulate real-world production support scenarios involving bad version rollouts and safe recovery.

This project focuses on **operational remediation**, not CI/CD, and mirrors how Application Support and SRE teams safely respond to incidents in live environments.

---

## Project Overview

This lab simulates three application instances running as Docker containers:

- **app01** → healthy version (`1.2`)
<img width="512" height="330" alt="image" src="https://github.com/user-attachments/assets/beead5b6-93d7-4e41-8663-8ca7b7ac9f15" />

- **app02** → unhealthy version (`1.3`)
<img width="522" height="336" alt="image" src="https://github.com/user-attachments/assets/26fdb0c9-28f0-48bc-b6a6-cf12f7547cdd" />

- **app03** → unhealthy version (`1.3`)
<img width="576" height="291" alt="image" src="https://github.com/user-attachments/assets/b6144eed-dd2d-4f73-8f55-fac81da68b90" />

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

DockerFile Commands

Build Docker Image:
```
docker build -t app:1.2 .
```
Build Containers:

```
docker run -d --name app01 -e APP_VERSION=1.2 -p 8081:8080 app:1.2

docker run -d --name app02 -e APP_VERSION=1.3 -p 8082:8080 app:1.2

docker run -d --name app03 -e APP_VERSION=1.3 -p 8083:8080 app:1.2
```
---

## Ansible Inventory

```ini
[app_devices]
app01
app02
app03

```

##Remediation Logic

The playbook:

1. Inspects container environment variables

2. Determines if a bad version is running

3. Prints remediation decisions per host

4. Stops and removes unhealthy containers

5. Recreates them using the healthy version

6. Healthy containers are never modified.

##Ansible Commands

Dry Run Validation

```
ansible-playbook -i inventory.ini remediate.yml --check
```

After dry run succeeds and you see the erroring devices, run the following:

```
ansible-playbook -i inventory.ini remediate.yml
```


