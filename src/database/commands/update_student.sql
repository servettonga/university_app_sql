UPDATE student
SET id = CASE
        WHEN :id = :new_id THEN id
        ELSE :new_id
    END,
    name = :name,
    surname = :surname
WHERE id = :id;