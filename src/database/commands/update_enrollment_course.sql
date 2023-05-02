UPDATE enrollment
SET course_code = :new_code
WHERE course_code = :course_code;