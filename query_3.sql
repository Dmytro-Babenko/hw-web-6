SELECT g.id, g.title, avg_m FROM
(SELECT st.group_id, AVG(m.mark) AS avg_m 
FROM students st
JOIN marks m ON m.student_id = st.id
WHERE m.subject_id = 2
GROUP BY st.group_id 
ORDER BY avg_m DESC)
JOIN groups g ON group_id = g.id;