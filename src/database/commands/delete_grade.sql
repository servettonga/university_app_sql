UPDATE enrollment
SET grade = NULL
WHERE course_code = :course_code
    AND student_id = :student_id
    AND grade IS NOT NULL;