import json
import sqlite3
from pathlib import Path

from src.customize import Color


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

    def __run_query(self, raw_sql: str, placeholder: dict = {}) -> None:
        """Run query"""
        raw_sql_path = Path(self.raw_sql_path + raw_sql).read_text()

        self.cursor.execute(raw_sql_path, placeholder)
        self.commit()

    def __check_parameters(self, *args) -> None:
        """Check parameters"""
        for arg in args:
            if str(arg) == '':
                raise Exception(self.text['create']['empty_input'])

    def create_tables(self) -> None:
        """Create tables if not exists"""
        raw_sql_path = Path(self.raw_sql_path + 'create_tables.sql').read_text()
        self.cursor.executescript(raw_sql_path)

    def drop_tables(self) -> None:
        """Drop tables if exists"""
        self.__run_query('drop_tables.sql')

    def create_lecturer(self, title: str, name: str, surname: str) -> None:
        """Create a lecturer"""
        self.__check_parameters(title, name, surname)
        try:
            self.__run_query('insert_lecturer.sql', {'title': title, 'name': name, 'surname': surname})
        except sqlite3.IntegrityError:
            raise Exception(self.text['create']['lecturer']['lecturer_exists'])
        print(Color.info + self.text['create']['lecturer']['successful'])

    def update_lecturer(self, lecturer_id: int, title: str, name: str, surname: str) -> None:
        """Update a lecturer"""
        self.__check_parameters(lecturer_id, title, name, surname)
        self.get_lecturer(lecturer_id=lecturer_id)
        self.__run_query('update_lecturer.sql', {'id': lecturer_id, 'title': title, 'name': name, 'surname': surname})
        print(Color.info + self.text['update']['lecturer']['successful'])

    def create_course(self, course_code: str, course_name: str) -> None:
        """Create a course"""
        self.__check_parameters(course_code, course_name)
        try:
            self.__run_query('insert_course.sql', {'code': course_code, 'name': course_name})
        except sqlite3.IntegrityError:
            raise Exception(self.text['create']['course']['course_exists'])

    def update_course(self, course_code: str, new_code: str, new_name: str) -> None:
        """Update a course"""
        self.__check_parameters(course_code, new_code, new_name)
        self.get_course(course_code=course_code)
        try:
            self.__run_query('update_course.sql', {'code': course_code, 'new_code': new_code, 'new_name': new_name})
            self.__run_query('update_enrollment_course.sql', {'course_code': course_code, 'new_code': new_code})
        except sqlite3.IntegrityError:
            raise Exception(self.text['update']['course']['course_exists'])
        print(Color.info + self.text['update']['course']['successful'])

    def course_lecturer(self, course_code: str, lecturer_id: int) -> None:
        """Assign a lecturer to a course"""
        self.__check_parameters(course_code, lecturer_id)
        self.get_course(course_code=course_code)
        self.get_lecturer(lecturer_id=lecturer_id)
        if self.is_lecturer_assigned(course_code=course_code):
            raise Exception(self.text['update']['assign']['already_assigned'])
        self.__run_query('assign_lecturer.sql', {'course_code': course_code, 'lecturer_id': lecturer_id})
        print(Color.info + self.text['update']['assign']['successful'])

    def create_student(self, name: str, surname: str, id: int) -> None:
        """Create a student"""
        self.__check_parameters(name, surname, id)
        try:
            self.__run_query('insert_student.sql', {'name': name, 'surname': surname, 'id': id})
        except sqlite3.IntegrityError:
            raise Exception(self.text['create']['student']['student_exists'])
        print(Color.info + self.text['create']['student']['successful'])

    def update_student(self, id: int, new_id: int, name: str, surname: str) -> None:
        """Update a student"""
        self.__check_parameters(new_id, name, surname, id)
        self.get_student(student_id=id)
        try:
            self.__run_query('update_student.sql', {'id': id, 'new_id': new_id, 'name': name, 'surname': surname})
            self.__run_query('update_enrollment_student.sql', {'id': id, 'new_id': new_id})
        except sqlite3.IntegrityError:
            raise Exception(self.text['update']['student']['student_exists'])
        print(Color.info + self.text['update']['student']['successful'])

    def enroll_student(self, student_id: int, course_code: str) -> None:
        """Enroll a student to a course"""
        if not self.is_enrolled(student_id, course_code):
            self.__run_query('insert_enrollment.sql', {'student_id': student_id, 'course_code': course_code})
            print(Color.info + self.text['update']['enroll']['successful'])
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
        self.__run_query('insert_grade.sql', {'student_id': student_id, 'course_code': course_code, 'grade': grade})
        if self.get_grade(student_id, course_code) == grade:
            print(Color.info + self.text['create']['grade']['successful'])

    def update_grade(self, student_id: int, course_code: str, grade: float) -> None:
        """Update grade from a student"""
        self.get_student(student_id=student_id)
        self.get_course(course_code=course_code)
        if not self.is_enrolled(student_id, course_code):
            raise Exception(self.text['create']['grade']['not_enrolled'])
        self.__run_query('update_grade.sql', {'student_id': student_id, 'course_code': course_code, 'grade': grade})
        if self.get_grade(student_id, course_code) == grade:
            print(Color.info + self.text['update']['grade']['successful'])

    def delete_grade(self, student_id: int, course_code: str) -> None:
        """Delete grade from a student"""
        self.get_student(student_id=student_id)
        self.get_course(course_code=course_code)
        self.get_grade(student_id, course_code)
        self.__run_query('delete_grade.sql', {'student_id': student_id, 'course_code': course_code})

    def get_lecturer(self, lecturer_id: int) -> list:
        """Get lecturer by id"""
        self.__run_query('select_lecturer.sql', {'id': lecturer_id})
        if not self.cursor.fetchall():
            raise Exception(self.text['get']['lecturer_not_found'])
        return self.cursor.fetchone()

    def get_lecturers(self) -> list:
        """Get all lecturers"""
        self.__run_query('select_lecturers.sql')
        result = self.cursor.fetchall()
        if not result:
            raise Exception(self.text['get']['lecturers_not_found'])
        return result

    def get_lecturer_by_name(self, name: str, surname: str) -> list:
        """Get lecturer by name"""
        self.__run_query('select_lecturer_by_name.sql', {'name': name, 'surname': surname})
        result = self.cursor.fetchall()
        if not result:
            raise Exception(self.text['get']['lecturer_not_found'])
        return result

    def get_lecturer_courses(self, lecturer_id: int) -> list:
        """Get lecturer courses"""
        self.get_lecturer(lecturer_id=lecturer_id)
        self.__run_query('select_lecturer_courses.sql', {'lecturer_id': lecturer_id})
        return self.cursor.fetchall()

    def is_lecturer_assigned(self, course_code: str) -> bool:
        """Get lecturer by course"""
        self.__run_query('select_lecturer_by_course.sql', {'course_code': course_code})
        result = self.cursor.fetchone()
        if result[0] is not None:
            return True
        return False

    def get_course(self, course_code: str) -> list:
        """Get course by code"""
        self.__run_query('select_course.sql', {'course_code': course_code})
        result = self.cursor.fetchall()
        if not result:
            raise Exception(self.text['get']['course_not_found'])
        return result

    def get_courses(self) -> list:
        """Get all courses"""
        self.__run_query('select_courses.sql')
        result = self.cursor.fetchall()
        if not result:
            raise Exception(self.text['get']['courses_not_found'])
        return result

    def get_courses_by_lecturer(self, lecturer_id: int) -> list:
        """Get all courses by lecturer"""
        self.get_lecturer(lecturer_id=lecturer_id)
        self.__run_query('select_courses_by_lecturer.sql', {'lecturer_id': lecturer_id})
        result = self.cursor.fetchall()
        if not result:
            raise Exception(self.text['get']['courses_not_found'])
        return result

    def get_student(self, student_id: int) -> list:
        """Get student by id"""
        self.__run_query('select_student.sql', {'id': student_id})
        result = self.cursor.fetchall()
        if not result:
            raise Exception(self.text['get']['student_not_found'])
        return result

    def get_students(self) -> list:
        """Get all students"""
        self.__run_query('select_students.sql')
        result = self.cursor.fetchall()
        if not result:
            raise Exception(self.text['get']['students_not_found'])
        return result

    def get_student_enrollments(self, student_id: int) -> list:
        """Get student enrollments"""
        self.get_student(student_id=student_id)
        self.__run_query('select_student_enrollments.sql', {'id': student_id})
        return self.cursor.fetchall()

    def is_enrolled(self, id, code) -> bool:
        """Get student's enrollments"""
        self.get_student(student_id=id)
        self.get_course(course_code=code)
        self.__run_query('select_enrolled_student.sql', {'student_id': id, 'course_code': code})
        return self.cursor.fetchall()

    def get_students_by_course(self, course_code: str) -> list:
        """Get all students by course"""
        self.get_course(course_code=course_code)
        self.__run_query('select_students_by_course.sql', {'course_code': course_code})
        return self.cursor.fetchall()

    def get_grade(self, student_id: int, course_code: str) -> list:
        """Get grade by student and course"""
        self.get_student(student_id=student_id)
        self.get_course(course_code=course_code)
        self.__run_query('select_grade.sql', {'student_id': student_id, 'course_code': course_code})
        return self.cursor.fetchone()[0]

    def get_student_grades(self, student_id: int) -> list:
        """Get all grades by student"""
        self.get_student(student_id=student_id)
        self.__run_query('select_student_grades.sql', {'student_id': student_id})
        return self.cursor.fetchall()

    def get_course_grades(self, course_code: str) -> list:
        """Get all grades by course"""
        self.get_course(course_code=course_code)
        self.__run_query('select_course_grades.sql', {'course_code': course_code})
        return self.cursor.fetchall()
