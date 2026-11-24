# DevOps Assignment Report — Todo API

> Complete every bracketed field. Insert your own screenshots and actual command output. Do not claim a command passed unless you ran it.

## Title Page
- Student name: [Your name]
- Register number: [Your register number]
- Course: DevOps
- Course code: 25CIAEC59 / 25CYAEC59
- Project: Todo API — CI/CD Pipeline and Kubernetes Deployment
- Repository: https://github.com/akash0192005-cpu/todo-devops-pipeline

## Certificate
[Insert the certificate page/template supplied by your institution. Obtain the required signature; do not treat this placeholder as a certificate.]

## Abstract
This project implements a small Todo REST API using Python and Flask. The API stores tasks in memory and exposes endpoints to list tasks, create a task, and report service health. The source is managed in GitHub. Jenkins is configured as a pipeline to poll source control, install dependencies, run unit tests, package the application, and archive the package. GitHub Actions provides an additional push and pull-request CI workflow. Ansible provisions a Linux host using a reusable role and handler. Docker packages the API, and Kubernetes deploys it behind a Service with three initial replicas. The Kubernetes configuration uses a ConfigMap and health probes.

## 1. Introduction
[Explain the objective: demonstrate the flow from source control through continuous integration, configuration management, containerization, deployment, and scaling. Add a short description of the Todo API.]

## 2. Component 1 — Git, Build and Continuous Integration

### 2.1 Development Environment
- Language/runtime: Python 3.12
- Framework: Flask
- Tests: pytest
- Source control: Git and GitHub
- CI: Jenkins and GitHub Actions

[Record the OS and exact tool versions used.]

### 2.2 Application and API
- `GET /todos`: returns the in-memory task list.
- `POST /todos`: creates a task from JSON containing a non-empty `title`.
- `GET /health`: returns service health.

Example:
```bash
curl http://localhost:5000/health
curl -X POST http://localhost:5000/todos -H 'Content-Type: application/json' -d '{"title":"Complete assignment"}'
curl http://localhost:5000/todos
```

[Insert actual response screenshots from your own run.]

### 2.3 Git Branching and Merge
The implementation was developed on `feature/todo-api-devops` and merged into `main` through pull request #1.

[Insert screenshot of GitHub branches and the merged pull request/commit history.]

### 2.4 Jenkins Pipeline
The repository contains a Jenkinsfile with SCM polling, dependency installation, a pytest stage that writes JUnit XML, and an archived build tarball named with the Jenkins build number.

Jenkins job configuration:
- Repository URL: https://github.com/akash0192005-cpu/todo-devops-pipeline
- Branch: `main`
- Pipeline definition: Pipeline script from SCM
- Script path: `Jenkinsfile`
- The Jenkinsfile polls SCM every two minutes. A GitHub webhook can be configured instead.

[Insert screenshots of job SCM configuration, trigger configuration, successful console output, and archived artifact. These must come from your Jenkins instance.]

### 2.5 CI Enhancement
The chosen enhancement is GitHub Actions alongside Jenkins. The workflow runs pytest and builds a Docker image on pushes to `main` and feature branches and on pull requests targeting `main`.

[Insert a screenshot/link to a completed successful Actions run. Record the run URL and result.]

## 3. Component 2 — Ansible, Docker and Kubernetes

### 3.1 Ansible Configuration Management
The Ansible inventory targets localhost by default for a local Linux/WSL demonstration. The `todo_api` role installs Python, creates a service account and application directory, copies the source, installs Flask in a virtual environment, and configures a systemd service. A handler restarts the service when its configuration or source changes.

Run from the repository root on a Linux/WSL host with Ansible and sudo access:
```bash
ansible-playbook -i ansible/inventory.ini ansible/site.yml --ask-become-pass
```
[Record the target host, command output and whether the playbook completed successfully. Insert screenshot.]

### 3.2 Docker
Build and run:
```bash
docker build -t todo-api:local .
docker run --rm -p 5000:5000 todo-api:local
```
In another terminal, test `curl http://localhost:5000/health`.

[Insert terminal screenshot showing successful image build, running container and API response.]

### 3.3 Kubernetes Deployment and Service
For Minikube:
```bash
minikube start
docker build -t todo-api:local .
minikube image load todo-api:local
kubectl apply -f k8s/
kubectl rollout status deployment/todo-api
kubectl get pods
kubectl get svc
```
The Deployment starts with three replicas. The Service exposes port 5000 through NodePort 30050. The Deployment uses a ConfigMap for the port and liveness/readiness probes on `/health`.

[Insert screenshots of the applied manifests, three running pods, Service, and a successful API request through the cluster.]

### 3.4 Scaling Demonstration
```bash
kubectl scale deployment/todo-api --replicas=5
kubectl get pods
kubectl scale deployment/todo-api --replicas=3
kubectl get pods
```
[Insert actual screenshots showing five ready pods and then three ready pods.]

### 3.5 Deployment Enhancement
The selected deployment enhancements are a ConfigMap for the application port and liveness/readiness probes against `/health`. The ConfigMap separates configuration from the container image. The probes let Kubernetes check whether the service is ready to receive traffic and whether it should be restarted.

[Insert screenshot of the applied ConfigMap and Deployment probe configuration, plus pod readiness evidence.]

## 4. Results
[Summarize only verified results. Include a table of each command/tool, observed result, date, and evidence screenshot filename.]

## 5. Conclusion
[Describe what you learned about Git branching, CI automation, configuration management, containerization, Kubernetes deployment and scaling. Mention any remaining limitations honestly.]

## 6. References
1. Assignment brief: DevOps course assignment, course code 25CIAEC59 / 25CYAEC59.
2. Flask documentation: https://flask.palletsprojects.com/
3. pytest documentation: https://docs.pytest.org/
4. Jenkins Pipeline documentation: https://www.jenkins.io/doc/book/pipeline/
5. Ansible documentation: https://docs.ansible.com/
6. Docker documentation: https://docs.docker.com/
7. Kubernetes documentation: https://kubernetes.io/docs/

## Submission Checklist
- [ ] Replace all placeholders and add title/certificate pages in the institution's required format.
- [ ] Run the API and record real curl output.
- [ ] Run pytest and capture the result.
- [ ] Configure Jenkins SCM and trigger; confirm a push triggers a build and archive.
- [ ] Confirm a successful GitHub Actions run.
- [ ] Run the Ansible playbook successfully on a Linux/WSL host.
- [ ] Build and run the Docker image successfully.
- [ ] Deploy to Kubernetes; verify Service and API response.
- [ ] Capture scaling evidence at five replicas and then three.
- [ ] Add the course coordinator as a repository collaborator.
- [ ] Put this report and the source-code folder in the final submission.
