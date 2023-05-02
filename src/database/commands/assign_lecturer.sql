UPDATE course
SET lecturer = :lecturer_id
WHERE code = :course_code
    AND lecturer IS NULL;