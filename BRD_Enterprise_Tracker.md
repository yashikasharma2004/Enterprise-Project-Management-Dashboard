# Business Requirement Document (BRD)
## Project: Enterprise Project Delivery & Budget Health System

### 1. Business Problem Statement
Enterprise projects in CPG & SaaS often experience timeline slippages and budget drift due to scattered project management tracking and lack of centralized KPI dashboards.

### 2. Business Objectives
- Centralize multi-project performance metrics into a single source of truth.
- Flag budget overruns early with automated risk categorization.
- Optimize team resource allocation across ongoing enterprise delivery sprints.

### 3. Key Stakeholders & Roles
- **Enterprise Project Manager (EPM):** Tracks velocity, milestones, and delays.
- **Business Analyst:** Analyzes requirement coverage, project risks, and financial health.
- **Operations & Finance Lead:** Monitors budget vs. actual spend variances.

### 4. Functional Requirements
- **FR-1:** System must visualize budget variance per project in real-time.
- **FR-2:** System must highlight tasks marked with High or Critical risk scores.
- **FR-3:** System must display total active projects and overall financial impact.

### 5. Data & Process Flow
[Project Operational Data] -> [SQL Risk & Budget Aggregations] -> [Streamlit Real-Time Dashboard UI]