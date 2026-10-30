# 📊 Enterprise Project Delivery & Budget Health Dashboard

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28%2B-FF4B4B)
![PostgreSQL / SQL](https://img.shields.io/badge/SQL-Analytics-003B5C)
![License](https://img.shields.io/badge/License-MIT-green)

An end-to-end Enterprise Project Management (EPM) framework designed to bridge business requirement analysis, database querying, and real-time visualization. This project tracks project health, identifies budget variances, and flags delivery bottleneck risks across active enterprise software deployments.

---

## 📌 Executive Summary & Business Need

Enterprise delivery teams frequently encounter **budget slippage** and **timeline overruns** due to decentralized tracking systems and fragmented status updates. 

This repository provides an integrated solution:
1. **Business Requirement Specification (BRD):** Standardized documentation outlining operational KPIs and functional scopes.
2. **Data-Driven Analytics (SQL):** Structured queries to calculate financial variances, delay risks, and resource utilization.
3. **Interactive Visual Dashboard (Streamlit):** A decision-support interface for Project Managers and Business Analysts to mitigate risks proactively.

---

## 🛠️ Key Project Deliverables

| File | Type | Description |
| :--- | :--- | :--- |
| `BRD_Enterprise_Tracker.md` | Business Analysis | Comprehensive document defining problem statement, stakeholder roles, and functional workflows. |
| `analytics_queries.sql` | SQL Database Scripts | Analytical queries for financial health status, delayed task flagging, and workload distribution. |
| `app.py` | Python Application | Interactive Streamlit Web App featuring metric cards, variance bar charts, and risk pie distributions. |

---

## 📈 Core Metrics & Features

* **Financial Health Monitoring:** Real-time tracking of Allocated Budget vs. Actual Spend to calculate Net Variance.
* **Bottleneck Identification:** Flagging tasks with `High` or `Critical` risk levels and track delay durations.
* **Interactive Data Filtering:** Dynamic breakdown of project statuses and active delivery counts.

---

## 🚀 Quickstart Guide (Local Setup)

To run the dashboard locally on your machine, follow these simple steps:

### 1. Prerequisites
Ensure you have **Python 3.10+** installed on your system.

### 2. Clone the Repository
```bash
git clone [https://github.com/YOUR_USERNAME/Enterprise-Project-Management-Dashboard.git](https://github.com/YOUR_USERNAME/Enterprise-Project-Management-Dashboard.git)
cd Enterprise-Project-Management-Dashboard

pip install streamlit pandas plotly


streamlit run app.py

[ Enterprise Project Data ] ➔ [ SQL Risk & Budget Aggregation ] ➔ [ Streamlit Interactive UI ]


