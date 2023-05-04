DROP TABLE IF EXISTS lecturer;
DROP TABLE IF EXISTS course;
DROP TABLE IF EXISTS student;
DROP TABLE IF EXISTS enrollment;
CREATE TABLE lecturer (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    title VARCHAR(255),
    name VARCHAR(255) NOT NULL,
    surname VARCHAR(255) NOT NULL
);
CREATE TABLE course (
    code CHAR(255) PRIMARY KEY UNIQUE,
    name VARCHAR(255) NOT NULL,
    lecturer INT,
    FOREIGN KEY (lecturer) REFERENCES lecturer(id)
);
CREATE TABLE student (
    id INTEGER PRIMARY KEY UNIQUE,
    name VARCHAR(255) NOT NULL,
    surname VARCHAR(255) NOT NULL
);
CREATE TABLE enrollment (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    course_code CHAR(255) NOT NULL,
    student_id INT NOT NULL,
    grade FLOAT,
    FOREIGN KEY (course_code) REFERENCES course(code),
    FOREIGN KEY (student_id) REFERENCES student(id)
);
INSERT INTO lecturer (title, name, surname)
VALUES ('Dr.', 'John', 'Smith'),
    ('Prof.', 'Jane', 'Doe'),
    ('Dr.', 'Michael', 'Johnson'),
    ('Prof.', 'Sarah', 'Lee'),
    ('Dr.', 'William', 'Williams'),
    ('Prof.', 'Ava', 'Jones');
INSERT INTO course (code, name, lecturer)
VALUES ('CS101', 'Introduction to CS', 1),
    ('CS102', 'Data Structures and Algos', 2),
    ('CS103', 'Computer Networks', 3),
    ('CS104', 'Operating Systems', 4),
    ('CS105', 'Artificial Intelligence', 5),
    ('CS106', 'EMPTY COURSE', NULL);
INSERT INTO student (id, name, surname)
VALUES ('20230001', 'Mike', 'Doe'),
    ('20230002', 'Samantha', 'Doe'),
    ('20230003', 'David', 'Smith'),
    ('20230004', 'Emily', 'Smith'),
    ('20230005', 'William', 'Johnson'),
    ('20230006', 'Ava', 'Johnson'),
    ('20230007', 'Ethan', 'Williams'),
    ('20230008', 'Olivia', 'Williams'),
    ('20230010', 'Sophia', 'Brown'),
    ('20230011', 'Justin', 'Martinez'),
    ('20230012', 'Julie', 'Martinez'),
    ('20230013', 'Tommy', 'Davis'),
    ('20230014', 'Ben', 'Davis'),
    ('20230015', 'Jared', "O'Connor"),
    ('20230016', "Jenna", "O'Connor"),
    ("20230017", "Albert", "Nguyen"),
    ("20230018", "Jasmine", "Nguyen");
INSERT INTO enrollment (student_id, course_code, grade)
VALUES ('20230001', 'CS101', 4.5),
    ('20230001', 'CS102', 3.2),
    ('20230001', 'CS103', 2.7),
    ('20230001', 'CS104', 4.0),
    ('20230002', 'CS101', NULL),
    ('20230002', 'CS102', 4.2),
    ('20230002', 'CS103', 3.7),
    ('20230002', 'CS104', 4.5),
    ('20230002', 'CS105', 4.0),
    ('20230003', 'CS101', 2.5),
    ('20230003', 'CS102', 3.2),
    ('20230003', 'CS103', 3.7),
    ('20230003', 'CS104', 3.0),
    ('20230003', 'CS105', 2.8),
    ('20230004', 'CS101', 4.0),
    ('20230004', 'CS102', 4.5),
    ('20230004', 'CS103', 4.7),
    ('20230004', 'CS104', 4.0),
    ('20230004', 'CS105', 4.5),
    ('20230005', 'CS101', 3.5),
    ('20230005', 'CS102', 3.2),
    ('20230005', 'CS103', 2.7),
    ('20230005', 'CS104', 3.0),
    ('20230005', 'CS105', 3.8),
    ('20230006', 'CS101', '4.5'),
    ('20230006', 'CS102', '4.2'),
    ('20230006', 'CS103', '3.7'),
    ('20230006', 'CS104', '4.5'),
    ('20230006', 'CS105', '4'),
    ('20230007', 'CS101', '2.5'),
    ('20230007', 'CS102', '3.2'),
    ('20230007', 'CS103', '3.7'),
    ('20230007', 'CS104', '3'),
    ('20230007', 'CS105', '2.8'),
    ('20230008', 'CS101', '4'),
    ('20230008', 'CS102', '4.5'),
    ('20230008', 'CS103', '4.7'),
    ('20230008', 'CS104', '4'),
    ('20230008', 'CS105', '4.5'),
    ('20230009', 'CS101', '3.5'),
    ('20230009', 'CS102', '3.2'),
    ('20230009', 'CS103', '2.7'),
    ('20230009', 'CS104', '3'),
    ('20230009', 'CS105', '3.8'),
    ('20230010', 'CS101', '4'),
    ('20230010', 'CS102', '4.5'),
    ('20230010', 'CS103', '4.7'),
    ('20230010', 'CS104', '4'),
    ('20230010', 'CS105', '4.5'),
    ('20230011', 'CS101', '3.5'),
    ('20230011', 'CS102', '3.2'),
    ('20230011', 'CS103', '2.7'),
    ('20230011', 'CS104', '3'),
    ('20230011', 'CS105', '3.8'),
    ('20230012', 'CS101', '4.5'),
    ('20230012', 'CS102', '4.2'),
    ('20230012', 'CS103', '3.7'),
    ('20230012', 'CS104', '4.5'),
    ('20230012', 'CS105', '4'),
    ('20230013', 'CS101', 2.5),
    ('20230013', 'CS102', 3.2),
    ('20230013', 'CS103', 3.7),
    ('20230013', 'CS104', 3.0),
    ('20230013', 'CS105', 2.8),
    ('20230014', 'CS101', 3.5),
    ('20230014', 'CS102', 3.2),
    ('20230014', 'CS103', 2.7),
    ('20230014', 'CS104', 3.0),
    ('20230014', 'CS105', 3.8),
    ('20230015', 'CS101', 4.5),
    ('20230015', 'CS102', 4.2),
    ('20230015', 'CS103', 3.7),
    ('20230015', 'CS104', 4.5),
    ('20230015', 'CS105', 4.0),
    ('20230016', 'CS101', 2.5),
    ('20230016', 'CS102', 3.2),
    ('20230016', 'CS103', 3.7),
    ('20230016', 'CS104', 3.0),
    ('20230016', 'CS105', 2.8),
    ('20230017', 'CS101', 4.0),
    ('20230017', 'CS102', 4.5),
    ('20230017', 'CS103', 4.7),
    ('20230017', 'CS104', 4.0),
    ('20230017', 'CS105', 4.5);