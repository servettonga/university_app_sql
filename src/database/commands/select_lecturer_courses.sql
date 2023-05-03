SELECT course.code,
    course.name
FROM course
WHERE lecturer = :lecturer_id;