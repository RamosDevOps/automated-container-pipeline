# Automated Container Pipeline 🚀

A fully automated, production-ready CI/CD pipeline that builds, tests, and deploys a containerized Python Flask API using Docker, GitHub Actions, and free cloud hosting on Render.

## 🔗 Project Links
* **Live Web Service:** [https://automated-container-pipeline.onrender.com](https://automated-container-pipeline.onrender.com)
* **Docker Hub Repository:** [https://hub.docker.com/r/ramosjm080/automated-container-pipeline](https://hub.docker.com/r/ramosjm080/automated-container-pipeline)

---

## 📋 Project Overview
This project demonstrates a complete Continuous Integration and Continuous Deployment (CI/CD) lifecycle for a modern cloud-native web application. 

Instead of manually deploying code updates, this pipeline automates the entire process from local development to production. Every code commit pushed to the `main` branch undergoes automated testing, containerization, and immutable deployment, ensuring zero downtime and high reliability.

---

## 🔄 The Automated Workflow

```text
  [ Developer ] 
        │
     git push
        ▼
 ┌──────────────┐
 │    GitHub    │ ───► Triggers GitHub Actions Runner
 └──────────────┘
        │
        ▼
 ┌──────────────┐
 │  Unit Tests  │ ───► Runs "pytest" (Fails deployment if tests fail)
 └──────────────┘
        │
        ▼
 ┌──────────────┐
 │ Docker Build │ ───► Packages app & dependencies into a Linux image
 └──────────────┘
        │
        ▼
 ┌──────────────┐
 │  Docker Hub  │ ───► Pushes image to "ramosjm080/automated-container-pipeline"
 └──────────────┘
        │
        ▼
 ┌──────────────┐
 │  Cloud Host  │ ───► Pulls new image & deploys live (Render)
 └──────────────┘