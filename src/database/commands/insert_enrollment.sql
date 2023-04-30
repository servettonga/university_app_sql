INSERT INTO enrollment (course_code, student_id)
SELECT course_code,
    student_id
FROM (
        SELECT :student_id AS student_id,
            :course_code AS course_code
    ) AS input
WHERE NOT EXISTS (
        SELECT *
        FROM enrollment
        WHERE student_id = input.student_id
            AND course_code = input.course_code
    )