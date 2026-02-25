☁️ CloudResume – DevOps Edition

This is my enhanced version of the Cloud Resume Challenge, built with a modern cloud-native architecture and deployed with terraform.

This repository represents the development (Dev) environment, focused on containerization, Kubernetes orchestration, CI/CD pipeline, automation and scalability testing.


🚀 Project Overview

This project evolves the traditional Cloud Resume Challenge into a production-style system using:

Serverless backend (AWS Lambda + API Gateway)

DynamoDB visitor counter

CI/CD with GitHub Actions

Docker containerization

Kubernetes deployment (Minikube for local cluster)

Future production-ready networking with Ingress


🏗 Architecture (Dev Version)
Frontend → API → Visitor Service → DynamoDB
                    ↓
                Docker
                    ↓
               Kubernetes
               
🔧 Technologies Used

AWS Lambda

Amazon API Gateway

Amazon DynamoDB

Docker

Kubernetes (Minikube)

GitHub Actions (CI/CD)

Python (FastAPI)


⚙️ Features Implemented
✅ CI/CD Pipeline

Automatic build and test on push

GitHub Actions deployment workflow

Infrastructure-as-code driven updates

✅ Containerization

Backend packaged in Docker

Reproducible local and cluster environments

✅ Kubernetes Deployment

Deployment + Service YAML definitions

Scalable pod configuration

Secrets management for AWS credentials

✅ Stress Testing

Load test visitor API

Measure response time under load

Observe scaling behavior

✅ Auto Scaling

Horizontal Pod Autoscaler (HPA)

Automatically duplicate pods under CPU load

Scale down when idle

✅ Failure Recovery

Kill pods manually

Observe Kubernetes self-healing

Report restart and rescheduling behavior

✅ Monitoring & Reporting

Track:

Pod replication

Restart counts

Scaling events

Document behavior under stress


📊 Why This Version?

This project demonstrates:

Understanding of cloud-native architecture

Container orchestration

CI/CD automation

Infrastructure scalability

Production-grade deployment patterns
