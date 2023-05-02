import json
import sqlite3
from pathlib import Path


class University():
    """University app class"""

    def __init__(self, database, raw_sql_path) -> None:
        self.database = database
        self.raw_sql_path = raw_sql_path
        with open('src/text.json', 'r') as text:
            self.text = json.load(text)

    def connect(self) -> None:
        """Connect to database"""
        self.connection = sqlite3.connect(self.database)
        self.cursor = self.connection.cursor()

    def close(self) -> None:
        """Close connection"""
        self.connection.close()

    def commit(self) -> None:
        """Commit changes"""
        self.connection.commit()

    def _run_query(self, raw_sql: str, placeholder: dict = None) -> None:
        """Run query"""
        raw_sql_path = Path(self.raw_sql_path + raw_sql).read_text()
        if placeholder is not None:
            self.cursor.execute(raw_sql_path, placeholder)
        else:
            self.cursor.executescript(raw_sql_path)
        self.commit()

    def _check_parameters(self, *args) -> None:
        """Check parameters"""
        for arg in args:
            if str(arg) == '':
                raise Exception(self.text['create']['empty_input'])

    def create_tables(self) -> None:
        """Create tables if not exists"""
        self._run_query('create_tables.sql')

    def drop_tables(self) -> None:
        """Drop tables if exists"""
        self._run_query('drop_tables.sql')

    def create_lecturer(self, title: str, name: str, surname: str) -> None:
        """Create a lecturer"""
        self._check_parameters(title, name, surname)
        try:
            self._run_query('insert_lecturer.sql', {'title': title, 'name': name, 'surname': surname})
        except sqlite3.IntegrityError:
            raise Exception(self.text['create']['lecturer']['lecturer_exists'])
        print(self.text['create']['lecturer']['successful'])

    def create_course(self, course_code: str, course_name: str) -> None:
        """Create a course"""
        self._check_parameters(course_code, course_name)
        try:
            self._run_query('insert_course.sql', {'code': course_code, 'name': course_name})
        except sqlite3.IntegrityError:
            raise Exception(self.text['create']['course']['course_exists'])

    def course_lecturer(self, course_code: str, lecturer_id: int) -> None:
        """Assign a lecturer to a course"""
        self._check_parameters(course_code, lecturer_id)
        self.get_course(course_code=course_code)
        self.get_lecturer(lecturer_id=lecturer_id)
        if self.is_lecturer_assigned(course_code=course_code):
            raise Exception(self.text['update']['assign']['already_assigned'])
        self._run_query('assign_lecturer.sql', {'course_code': course_code, 'lecturer_id': lecturer_id})
        print(self.text['update']['assign']['successful'])

    def create_student(self, name: str, surname: str, id: int) -> None:
        """Create a student"""
        self._check_parameters(name, surname, id)
        try:
            self._run_query('insert_student.sql', {'name': name, 'surname': surname, 'id': id})
        except sqlite3.IntegrityError:
            raise Exception(self.text['create']['student']['student_exists'])
        print(self.text['create']['student']['successful'])

    def enroll_student(self, student_id: int, course_code: str) -> None:
        """Enroll a student to a course"""
        if not self.is_enrolled(student_id, course_code):
            self._run_query('insert_enrollment.sql', {'student_id': student_id, 'course_code': course_code})
            print(self.text['update']['enroll']['successful'])
        else:
            raise Exception(self.textp['update']['enroll']['already_enrolled'])

    def add_grade(self, student_id: int, course_code: str, grade: float) -> None:
        """Add grade to a student"""
        self.get_student(student_id=student_id)
        self.get_course(course_code=course_code)
        if not self.is_enrolled(student_id, course_code):
            raise Exception(self.text['create']['grade']['not_enrolled'])
        if self.get_grade(student_id, course_code):
            raise Exception(self.text['create']['grade']['alread_graded'])
        self._run_query('insert_grade.sql', {'student_id': student_id, 'course_code': course_code, 'grade': grade})
        print(self.text['create']['grade']['successful'])

    def delete_grade(self, student_id: int, course_code: str) -> None:
        """Delete grade from a student"""
        self.get_student(student_id=student_id)
        self.get_course(course_code=course_code)
        self.get_grade(student_id, course_code)
        self._run_query('delete_grade.sql', {'student_id': student_id, 'course_code': course_code})

    def update_grade(self, student_id: int, course_code: str, grade: float) -> None:
        """Update grade from a student"""
        self.get_student(student_id=student_id)
        self.get_course(course_code=course_code)
        if not self.is_enrolled(student_id, course_code):
            raise Exception(self.text['create']['grade']['not_enrolled'])
        self._run_query('update_grade.sql', {'student_id': student_id, 'course_code': course_code, 'grade': grade})

    def get_lecturer(self, lecturer_id: int) -> list:
        """Get lecturer by id"""
        self._run_query('select_lecturer.sql', {'id': lecturer_id})
        if not self.cursor.fetchall():
            raise Exception(self.text['get']['lecturer_not_found'])
        return self.cursor.fetchone()

    def is_lecturer_assigned(self, course_code: str) -> bool:
        """Get lecturer by course"""
        self._run_query('select_lecturer_by_course.sql', {'course_code': course_code})
        if self.cursor.fetchall():
            return True
        return False

    def get_lecturers(self) -> list:
        """Get all lecturers"""
        self._run_query('select_lecturers.sql')
        if not self.cursor.fetchall():
            raise Exception(self.text['get']['lecturers_not_found'])
        return self.cursor.fetchall()

    def get_course(self, course_code: str) -> list:
        """Get course by code"""
        self._run_query('select_course.sql', {'course_code': course_code})
        if not self.cursor.fetchall():
            raise Exception(self.text['get']['course_not_found'])
        return self.cursor.fetchall()

    def get_courses(self) -> list:
        """Get all courses"""
        self._run_query('select_courses.sql')
        if not self.cursor.fetchall():
            raise Exception(self.text['get']['courses_not_found'])
        return self.cursor.fetchall()

    def get_student(self, student_id: int) -> list:
        """Get student by id"""
        self._run_query('select_student.sql', {'id': student_id})
        if not self.cursor.fetchall():
            raise Exception(self.text['get']['student_not_found'])
        return self.cursor.fetchall()

    def get_students(self) -> list:
        """Get all students"""
        self._run_query('select_students.sql')
        if not self.cursor.fetchall():
            raise Exception(self.text['get']['students_not_found'])
        return self.cursor.fetchall()

    def is_enrolled(self, id, code) -> bool:
        """Get student's enrollments"""
        self.get_student(student_id=id)
        self.get_course(course_code=code)
        self._run_query('select_enrolled_student.sql', {'student_id': id, 'course_code': code})
        return self.cursor.fetchall()

    def get_students_by_course(self, course_code: str) -> list:
        """Get all students by course"""
        self.get_course(course_code=course_code)
        self._run_query('select_students_by_course.sql', {'course_code': course_code})
        return self.cursor.fetchall()

    def get_grade(self, student_id: int, course_code: str) -> list:
        """Get grade by student and course"""
        self.get_student(student_id=student_id)
        self.get_course(course_code=course_code)
        self._run_query('select_grade.sql', {'student_id': student_id, 'course_code': course_code})
        return self.cursor.fetchone()[0]

    def get_student_grades(self, student_id: int) -> list:
        """Get all grades by student"""
        self.get_student(student_id=student_id)
        self._run_query('select_student_grades.sql', {'student_id': student_id})
        return self.cursor.fetchall()

    def get_course_grades(self, course_code: str) -> list:
        """Get all grades by course"""
        self.get_course(course_code=course_code)
        self._run_query('select_course_grades.sql', {'course_code': course_code})
        return self.cursor.fetchall()
