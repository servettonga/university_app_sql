SELECT student.id,
    student.name,
    student.surname,
    enrollment.grade
FROM enrollment
    JOIN student ON enrollment.student_id = student.id
WHERE enrollment.course_code = :course_code;