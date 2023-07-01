SELECT st.fullname, m.mark 
FROM students st 
JOIN marks m 
ON m.student_id  = st.id  
WHERE st.group_id = ? AND m.subject_id = ?
ORDER BY m.m_date DESC 
LIMIT 1