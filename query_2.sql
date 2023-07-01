SELECT st.id, st.fullname, AVG(m.mark) AS avg_m 
FROM students st
JOIN marks m ON m.student_id = st.id
WHERE m.subject_id = ?
GROUP BY st.id
ORDER BY avg_m DESC
LIMIT 1;
