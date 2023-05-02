UPDATE enrollment
SET student_id = :new_id
WHERE student_id = :id;