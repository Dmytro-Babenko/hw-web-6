SELECT fullname, mark FROM students s 
JOIN marks m ON m.student_id = s.id
WHERE s.group_id = ? AND m.subject_id = ?;