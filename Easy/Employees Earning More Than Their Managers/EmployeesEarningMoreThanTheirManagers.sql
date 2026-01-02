-- Write your MySQL query statement below
SELECT e1.name as Employee
FROM Employee as e1
JOIN Employee e2 on e1.managerId=e2.id
WHERE e1.salary>e2.salary

--QED
--Problem 181 (Easy of Employees Earning More Than Their Managers) - Jason Balayev (MySQL)