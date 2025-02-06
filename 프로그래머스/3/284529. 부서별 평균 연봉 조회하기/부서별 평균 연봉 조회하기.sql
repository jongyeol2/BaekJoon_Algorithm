SELECT he.DEPT_ID,
       hd.DEPT_NAME_EN,
       ROUND(AVG(he.SAL), 0) as AVG_SAL
FROM HR_EMPLOYEES as he
LEFT JOIN HR_DEPARTMENT as hd
     ON he.DEPT_ID = hd.DEPT_ID
GROUP BY 1, 2
ORDER BY 3 DESC
