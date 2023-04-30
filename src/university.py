import sqlite3
from abc import ABC, abstractmethod
from pathlib import Path


class University(ABC):
    """University app class"""

    def __init__(self) -> None:
        self.database = 'database/university.db'
        self.raw_sql_path = 'src/database/commands/'

    def connect(self) -> None:
        """Connect to database"""
        self.connection = sqlite3.connect(self.database)
        self.cursor = self.connection.cursor()

    @abstractmethod
    def read_sql_query(sql_path: Path) -> str:
        """Read sql query"""
        return Path(sql_path).read_text()

    def run_query(self, raw_sql: str, placeholder: dict) -> None:
        """Run query"""
        self.connect()
        if placeholder:
            self.cursor.execute(self.raw_sql_path + raw_sql, placeholder)
        else:
            self.cursor.execute(self.raw_sql_path + raw_sql)
        self.connection.commit()
        self.connection.close()

    def create_tables(self) -> None:
        """Create tables if not exists"""
        self.run_query('create_tables.sql')

    def drop_tables(self) -> None:
        """Drop tables if exists"""
        self.run_query('drop_tables.sql')

    def create_lecturer(self, title: str, name: str, surname: str) -> None:
        """Create a lecturer"""
        self.run_query('insert_lecturer.sql', {'title': title, 'name': name, 'surname': surname})

    def create_course(self, course_code: str, course_name: str) -> None:
        """Create a course"""
        self.run_query('insert_course.sql', {'course_code': course_code, 'course_name': course_name})

    def course_lecturer(self, course_code: str, lecturer_id: int) -> None:
        """Assign a lecturer to a course"""
        self.run_query('update_course_lecturer.sql', {'course_code': course_code, 'lecturer_id': lecturer_id})

    def create_student(self, name: str, surname: str, id: int) -> None:
        """Create a student"""
        self.run_query('insert_student.sql', {'name': name, 'surname': surname, 'id': id})

    def enroll_student(self, student_id: int, course_code: str) -> None:
        """Enroll a student to a course"""
        self.run_query('insert_enrollment.sql', {'student_id': student_id, 'course_code': course_code})

    def add_grade(self, student_id: int, course_code: str, grade: float) -> None:
        """Add grade to a student"""
        self.run_query('insert_grade.sql', {'student_id': student_id, 'course_code': course_code, 'grade': grade})

    def delete_grade(self, student_id: int, course_code: str) -> None:
        """Delete grade from a student"""
        self.run_query('delete_grade.sql', {'student_id': student_id, 'course_code': course_code})

    def update_grade(self, student_id: int, course_code: str, grade: float) -> None:
        """Update grade from a student"""
        self.run_query('update_grade.sql', {'student_id': student_id, 'course_code': course_code, 'grade': grade})

    def get_lecturer(self, lecturer_id: int) -> list:
        """Get lecturer by id"""
        self.run_query('select_lecturer.sql', {'lecturer_id': lecturer_id})
        return self.cursor.fetchall()

    def get_lecturers(self) -> list:
        """Get all lecturers"""
        self.run_query('select_lecturers.sql')
        return self.cursor.fetchall()

    def get_course(self, course_code: str) -> list:
        """Get course by code"""
        self.run_query('select_course.sql', {'course_code': course_code})
        return self.cursor.fetchall()

    def get_courses(self) -> list:
        """Get all courses"""
        self.run_query('select_courses.sql')
        return self.cursor.fetchall()

    def get_student(self, student_id: int) -> list:
        """Get student by id"""
        self.run_query('select_student.sql', {'student_id': student_id})
        return self.cursor.fetchall()

    def get_students(self) -> list:
        """Get all students"""
        self.run_query('select_students.sql')
        return self.cursor.fetchall()

    def get_students_by_course(self, course_code: str) -> list:
        """Get all students by course"""
        self.run_query('select_students_by_course.sql', {'course_code': course_code})
        return self.cursor.fetchall()
