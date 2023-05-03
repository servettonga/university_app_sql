SELECT *
FROM enrollment
WHERE student_id = :id
ORDER BY course_code;