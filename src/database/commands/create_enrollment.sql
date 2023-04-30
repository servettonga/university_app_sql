CREATE TABLE IF NOT EXISTS enrollment (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    course_code CHAR(255) NOT NULL,
    student_id INT NOT NULL,
    grade FLOAT,
    FOREIGN KEY (course_code) REFERENCES course(code),
    FOREIGN KEY (student_id) REFERENCES student(id)
);