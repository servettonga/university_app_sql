CREATE TABLE IF NOT EXISTS course (
    code CHAR(255) PRIMARY KEY UNIQUE,
    name VARCHAR(255) NOT NULL,
    lecturer INT,
    FOREIGN KEY (lecturer) REFERENCES lecturer(id)
);