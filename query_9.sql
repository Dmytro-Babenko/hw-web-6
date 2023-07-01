SELECT DISTINCT s.title 
FROM subjects s 
JOIN marks m 
ON m.subject_id = s.id 
WHERE m.student_id = ?;