-- Write your MySQL query statement below
SELECT 
    event_day AS day, 
    emp_id, 
    SUM(out_time-in_time) AS total_time
FROM 
    Employees
GROUP BY event_day, emp_id  

--QED
--Problem 1741 (Easy of Find Total Time Spent By Each Employee) - Jason Balayev (MySQL)