SELECT course.code,
    course.name,
    lecturer.title,
    lecturer.name,
    lecturer.surname
FROM course
    LEFT JOIN lecturer ON course.lecturer = lecturer.id
WHERE code = :course_code;