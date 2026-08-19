# 🔄 Apache Airflow for Data Engineering

> Learning Apache Airflow for workflow orchestration and automated Data Engineering pipelines.

## 🎯 Objective

Learn how to schedule, monitor, and manage Data Engineering workflows using Airflow.

## 📚 Day 1 — Airflow Fundamentals

- Apache Airflow
- DAGs
- Tasks
- Operators
- Dependencies
- Scheduler
- Executor
- Webserver
- Airflow UI
- PythonOperator

## 🔄 Basic Workflow

```text
DAG
 ↓
Extract
 ↓
Transform
 ↓
Load




## 📚 Day 2 — Operators, Tasks & Dependencies

### Topics Covered

- DAG vs Task
- Operators
- PythonOperator
- BashOperator
- Task Dependencies
- Sequential Execution
- `>>` dependency operator
- `task_id`

### Operators

Operators define what a task should do.

Examples:

- `PythonOperator` — executes Python functions
- `BashOperator` — executes shell commands

### Task Dependency

```text
Extract
   ↓
Transform
   ↓
Validate
   ↓
Finish

## 📚 Day 3 — Scheduling, Retries & Dependencies

### Topics Covered

- DAG Scheduling
- `schedule`
- `start_date`
- `catchup`
- Task Retries
- Retry Delay
- Task Dependencies
- Upstream & Downstream Tasks

### Scheduling

Airflow Scheduler determines when DAGs should run.

Example:

```text
@daily
   ↓
DAG Run
   ↓
Extract → Transform → Load

## 📚 Day 5 — Airflow + Docker

### Topics Covered

- Docker Containers
- Docker Images
- Docker Compose
- Airflow Containerization
- Airflow Webserver
- Airflow Scheduler
- DAGs inside Containers

### Why Docker?

Docker provides a consistent environment for running Airflow and its dependencies.

### Architecture

```text
Docker Compose
      ↓
Airflow Services
      ↓
Scheduler + Webserver
      ↓
DAG
      ↓
Data Pipeline