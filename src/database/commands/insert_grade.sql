UPDATE enrollment
SET grade = :grade
WHERE student_id = :student_id
    AND course_code = :course_code
    AND grade IS NULL;