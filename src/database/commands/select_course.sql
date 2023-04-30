SELECT course.code,
    course.name,
    lecturer.title,
    lecturer.name,
    lecturer.surname
FROM course
    INNER JOIN lecturer ON course.lecturer = lecturer.id
WHERE code = :code;