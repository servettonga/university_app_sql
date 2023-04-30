SELECT course.code,
    course.name,
    lecturer.name,
    lecturer.surname
FROM course
    INNER JOIN lecturer ON course.lecturer = lecturer.id
ORDER BY code;