-- Enterprise Project Analytics Queries

-- 1. Calculate Budget Variance & Financial Risk
SELECT 
    project_name,
    allocated_budget,
    actual_spend,
    (actual_spend - allocated_budget) AS budget_variance,
    CASE 
        WHEN actual_spend > allocated_budget THEN 'High Financial Risk'
        WHEN actual_spend = allocated_budget THEN 'On Budget'
        ELSE 'Under Budget'
    END AS financial_status
FROM enterprise_projects;

-- 2. Identify Delayed & Critical Tasks by Project
SELECT 
    project_id,
    task_name,
    assigned_owner,
    delay_days,
    risk_score
FROM project_tasks
WHERE status != 'Completed' AND risk_score IN ('High', 'Critical')
ORDER BY delay_days DESC;

-- 3. Resource Utilization Summary
SELECT 
    assigned_owner,
    COUNT(task_id) AS total_assigned_tasks,
    SUM(CASE WHEN status = 'In Progress' THEN 1 ELSE 0 END) AS active_tasks
FROM project_tasks
GROUP BY assigned_owner;