SELECT AVG(mark) FROM marks m
WHERE subject_id IN (
SELECT s.id FROM subjects s
WHERE s.lecturer_id = ?
)