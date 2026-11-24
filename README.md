# Todo DevOps Pipeline

A starter project scaffolded from the uploaded DevOps assignment brief.

## Application
A small Python Flask Todo API with in-memory storage:
- `GET /todos` — list todos
- `POST /todos` — create a todo
- `GET /health` — health check

## Project layout
```
app/                  Flask application
tests/                pytest tests
ansible/              inventory, playbook and role
k8s/                  Kubernetes Deployment, Service and ConfigMap
.github/workflows/    GitHub Actions CI
Dockerfile            Container image
Jenkinsfile           Jenkins pipeline
requirements.txt      Python dependencies
repo_link.txt         Repository URL
```

## Run locally
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\\Scripts\\activate
pip install -r requirements.txt
python -m app
```
The API listens on port 5000.

## Test
```bash
pip install -r requirements.txt
pytest -q
```

## Docker
```bash
docker build -t todo-devops-pipeline:local .
docker run --rm -p 5000:5000 todo-devops-pipeline:local
```

## Kubernetes
Review the manifests in `k8s/`, then apply them:
```bash
kubectl apply -f k8s/
kubectl get pods,svc
kubectl scale deployment/todo-api --replicas=5
kubectl scale deployment/todo-api --replicas=3
```

## Ansible
The role and playbook in `ansible/` are a starting point. Update the inventory to point to a Linux host with SSH access before running:
```bash
ansible-playbook -i ansible/inventory.ini ansible/site.yml
```

## Important
This repository contains a starter implementation generated from the assignment specification. It has not been run against your Jenkins server, Ansible host, Docker daemon or Kubernetes cluster. Complete those environment-specific steps and capture the required screenshots before submission.
