UPDATE enrollment
SET grade = :grade
WHERE course_code = :course_code
    AND student_id = :student_id
    AND grade IS NULL;