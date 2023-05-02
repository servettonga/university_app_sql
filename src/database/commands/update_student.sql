UPDATE student
SET id = :new_id,
    name = :name,
    surname = :surname
WHERE id = id;