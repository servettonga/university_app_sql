import json
import os
import time

from src.customize import Color
from src.university import University


class App():

    def __init__(self) -> None:
        with open('src/config.json', 'r') as config_file:
            self.config = json.load(config_file)
        self.database = self.config['database']
        self.raw_sql_path = self.config['sql_commands']

        self.base = University(self.database, self.raw_sql_path)
        self.base.connect()
        self.base.create_tables()

        with open('src/text.json', 'r') as text:
            self.text = json.load(text)
        self.choices: dict = self.text['choices']

    def __clear(self, n: int = 0) -> None:
        time.sleep(n)
        os.system("cls" if os.name == "nt" else "clear")

    def close(self) -> None:
        self.base.close()
        exit(0)

    def __commit_changes(self) -> None:
        self.base.commit()

    # Menu
    # --------------------------------------------------------------------------
    def run(self) -> None:
        """Print options"""
        self.__clear()
        print(Color.primary + self.text['greeting'])
        for title in self.choices:
            print(Color.primary + f"{title} ---------------------------")
            for choice in self.choices[title]:
                print(Color.seconday + f"{choice}. {self.choices[title][choice]}")
        print("\n0. Exit")
        try:
            self.__cohice(int(input(Color.primary + self.text['input']['choice'])))
            self.__commit_changes()
        except ValueError:
            print(Color.warning + self.text['input']['invalid'])
        self.__clear(2)

    def __cohice(self, choice: int) -> None:
        """List of methods to be used by user"""
        self.__clear()
        match choice:
            case 1:
                self.create_lecturer()
            case 2:
                self.create_course()
            case 3:
                self.create_student()
            case 4:
                self.assign_lecturer()
            case 5:
                self.enroll_student()
            case 6:
                self.add_grade()
            case 7:
                self.update_lecturer()
            case 8:
                self.update_course()
            case 9:
                self.update_student()
            case 10:
                self.update_grade()
            case 11:
                self.find_lecturer()
            case 12:
                self.print_all_lecturers()
            case 13:
                self.print_course_information()
            case 14:
                self.print_all_courses()
            case 15:
                self.find_student_by_id()
            case 16:
                self.print_all_students()
            case 0:
                self.close()
                exit(0)
            case _:
                print("Invalid choice!")

    def __continue(self) -> None:
        input(Color.info + self.text['input']['continue'])

    # Create
    # --------------------------------------------------------------------------
    def create_lecturer(self) -> None:
        print(Color.primary + self.text['create']['lecturer']['title'])
        title: str = input(Color.seconday + self.text['data']['title']).capitalize()
        name: str = input(self.text['data']['name']).capitalize()
        surname: str = input(self.text['data']['surname']).capitalize()
        try:
            self.base.create_lecturer(title=title, name=name, surname=surname)
        except Exception as e:
            print(Color.warning + str(e))
            return

    def create_course(self) -> None:
        print(Color.primary + self.text['create']['course']['title'])
        code: str = input(Color.seconday + self.text['data']['course_code']).upper()
        name: str = input(self.text['data']['course_name']).capitalize()
        try:
            self.base.create_course(course_code=code, course_name=name)
        except Exception as e:
            print(Color.warning + str(e))
            return
        print(self.text['create']['course']['successful'])

    def create_student(self) -> None:
        print(Color.primary + self.text['create']['student']['title'])
        id: int = int(input(Color.seconday + self.text['data']['student_id']))
        name: str = input(self.text['data']['name']).capitalize()
        surname: str = input(self.text['data']['surname']).capitalize()
        try:
            self.base.create_student(name=name, surname=surname, id=id)
        except Exception as e:
            print(Color.warning + str(e))
            return

    def add_grade(self) -> None:
        print(Color.primary + self.text['create']['grade']['title'])
        student_id: int = int(input(Color.seconday + self.text['data']['student_id']))
        course_code: str = input(self.text['data']['course_code']).upper()
        grade_input: float = float(input(self.text['data']['grade']))
        try:
            self.base.add_grade(student_id=student_id, course_code=course_code, grade=grade_input)
        except Exception as e:
            print(Color.warning + str(e))
            return

    # Update
    # --------------------------------------------------------------------------
    def assign_lecturer(self) -> None:
        print(Color.primary + self.text['update']['assign']['title'])
        course_code: str = input(Color.seconday + self.text['data']['course_code']).upper()
        lecturer_id: int = int(input(self.text['data']['lecturer_id']))
        try:
            self.base.get_lecturer(lecturer_id=lecturer_id)
            self.base.get_course(course_code=course_code)
            self.base.course_lecturer(course_code=course_code, lecturer_id=lecturer_id)
        except Exception as e:
            print(Color.warning + str(e))
            return

    def enroll_student(self) -> None:
        print(Color.primary + self.text['update']['enroll']['title'])
        student_id: int = int(input(Color.seconday + self.text['data']['student_id']))
        course_code: str = input(self.text['data']['course_code']).upper()
        try:
            self.base.enroll_student(student_id=student_id, course_code=course_code)
        except Exception as e:
            print(Color.warning + str(e))
            return

    def update_lecturer(self) -> None:
        print(Color.primary + self.text['update']['lecturer']['title'])
        lecturer_id: int = int(input(Color.seconday + self.text['data']['lecturer_id']))
        title: str = input(self.text['data']['title']).capitalize()
        name: str = input(self.text['data']['name']).capitalize()
        surname: str = input(self.text['data']['surname']).capitalize()
        try:
            self.base.update_lecturer(lecturer_id=lecturer_id, title=title, name=name, surname=surname)
        except Exception as e:
            print(Color.warning + str(e))
            return

    def update_course(self) -> None:
        print(Color.primary + self.text['update']['course']['title'])
        print(Color.primary + self.text['update']['course']['old_code'])
        old_code: str = input(Color.seconday + self.text['data']['course_code']).upper()
        print(Color.primary + self.text['update']['course']['new_code'])
        course_code: str = input(Color.seconday + self.text['data']['course_code']).upper()
        name: str = input(self.text['data']['course_name']).capitalize()
        try:
            self.base.update_course(course_code=old_code, new_code=course_code, new_name=name)
        except Exception as e:
            print(Color.warning + str(e))
            return

    def update_student(self) -> None:
        print(Color.primary + self.text['update']['student']['title'])
        print(Color.primary + self.text['update']['student']['old_id'])
        id: int = int(input(Color.seconday + self.text['data']['student_id']))
        print(Color.primary + self.text['update']['student']['new_id'])
        new_id: int = int(input(Color.seconday + self.text['data']['student_id']))
        name: str = input(self.text['data']['name']).capitalize()
        surname: str = input(self.text['data']['surname']).capitalize()
        try:
            self.base.update_student(id=id, new_id=new_id, name=name, surname=surname)
        except Exception as e:
            print(Color.warning + str(e))
            return

    def update_grade(self) -> None:
        print(Color.primary + self.text['update']['grade']['title'])
        student_id: int = int(input(Color.seconday + self.text['data']['student_id']))
        course_code: str = input(self.text['data']['course_code']).upper()
        grade_input: float = float(input(self.text['data']['grade']))
        try:
            self.base.update_grade(student_id=student_id, course_code=course_code, grade=grade_input)
        except Exception as e:
            print(Color.warning + str(e))
            return

    # Print
    # --------------------------------------------------------------------------
    def find_lecturer(self) -> None:
        print(Color.primary + self.text['print']['lecturer'])
        name: str = input(Color.seconday + self.text['data']['name']).capitalize()
        surname: str = input(self.text['data']['surname']).capitalize()
        try:
            print(Color.primary + self.text['print']['result'])
            for row in self.base.get_lecturer_by_name(name=name, surname=surname):
                print(Color.seconday + f"\nID: {row[0]}\nTitle: {row[1]}\nName: {row[2]}\nSurname: {row[3]}\nCourses:")
                courses = self.base.get_lecturer_courses(lecturer_id=row[0])
                if courses is not None:
                    for course in courses:
                        print(Color.seconday + f"Code: {course[0]} Name: {course[1]}")
                else:
                    print(Color.seconday + self.text['print']['not_assigned'])
            self.__continue()
        except Exception as e:
            print(Color.warning + str(e))
            return

    def print_all_lecturers(self) -> None:
        print(Color.primary + self.text['print']['lecturers'])
        try:
            print(Color.primary + self.text['print']['result'])
            for row in self.base.get_lecturers():
                print(Color.seconday + f"ID: {row[0]}\nTitle: {row[1]}\nName: {row[2]}\nSurname: {row[3]}\n")
            self.__continue()
        except Exception as e:
            print(Color.warning + str(e))
            return

    def print_course_information(self) -> None:
        print(Color.primary + self.text['print']['course'])
        course_code: str = input(Color.seconday + self.text['data']['course_code']).upper()
        try:
            print(Color.primary + self.text['print']['result'])
            for row in self.base.get_course(course_code=course_code):
                print(Color.seconday + f"Course Code: {row[0]}\nCourse Name: {row[1]}")
                if row[2] is not None:
                    print(Color.seconday + f"Lecturer: {row[2]} {row[3]} {row[4]}")
                else:
                    print(Color.seconday + self.text['print']['without_lecturer'])
                print(Color.seconday + self.text['print']['enrolled_students'])
                for row in self.base.get_course_grades(course_code=course_code):
                    print(Color.seconday + f"Student ID: {row[0]} Grade: {row[3] or 'n/a'}")
            self.__continue()
        except Exception as e:
            print(Color.warning + str(e))
            return

    def print_all_courses(self) -> None:
        print(Color.primary + self.text['print']['courses'])
        try:
            print(Color.primary + self.text['print']['result'])
            for row in self.base.get_courses():
                print(Color.seconday + f"\nCourse Code: {row[0]}\nCourse Name: {row[1]}")
                if row[2] is not None:
                    print(Color.seconday + f"Lecturer: {row[2]} {row[3]} {row[4]}")
                else:
                    print(Color.seconday + self.text['print']['without_lecturer'])
            self.__continue()
        except Exception as e:
            print(Color.warning + str(e))
            return

    def find_student_by_id(self) -> None:
        print(Color.primary + self.text['print']['student'])
        id: int = int(input(Color.seconday + self.text['data']['student_id']))
        try:
            print(Color.primary + self.text['print']['result'])
            for row in self.base.get_student(student_id=id):
                print(Color.seconday + f"ID: {row[0]}\nName: {row[1]}\nSurname: {row[2]}\n\nEnrolled Courses:")
                courses = self.base.get_student_enrollments(student_id=row[0])
                if len(courses) == 0:
                    print(Color.seconday + self.text['print']['not_enrolled'])
                for course in courses:
                    print(Color.seconday + f"Code: {course[1]} Grade: {course[3]}")
            self.__continue()
        except Exception as e:
            print(Color.warning + str(e))
            return

    def print_all_students(self) -> None:
        print(Color.primary + self.text['print']['students'])
        try:
            print(Color.primary + self.text['print']['result'])
            for row in self.base.get_students():
                print(Color.seconday + f"ID: {row[0]}\nName: {row[1]}\nSurname: {row[2]}\n")
            self.__continue()
        except Exception as e:
            print(Color.warning + str(e))
            return
