SELECT enrollment.grade
FROM enrollment
WHERE course_code = :course_code
    AND student_id = :student_id;