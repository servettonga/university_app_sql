UPDATE course
SET code = :new_code,
    name = :new_name
WHERE code = :code;