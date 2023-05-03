SELECT *
FROM lecturer
WHERE lecturer.name = :name
    OR lecturer.surname = :surname;