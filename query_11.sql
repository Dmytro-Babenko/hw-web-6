SELECT AVG(m.mark) AS avg_mark
FROM subjects s 
JOIN marks m 
ON m.subject_id = s.id 
JOIN lecturers l 
ON s.lecturer_id = l.id 
WHERE l.id = ? AND m.student_id = ?