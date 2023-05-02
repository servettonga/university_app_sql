import json
import os
import time
from turtle import st

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

    def clear(self, n: int = 0) -> None:
        time.sleep(n)
        os.system("cls" if os.name == "nt" else "clear")

    def close(self) -> None:
        self.base.close()
        exit(0)

    def greet(self) -> None:
        self.clear()
        print(self.text['greeting'])
        # for key, value in self.choices.items():
        #     print(f"{key}. {value}")
        for title in self.choices:
            print(title + " ---------------------------")
            for choice in self.choices[title]:
                print(f"{choice}. {self.choices[title][choice]}")
        print("\n0. Exit")
        try:
            self.cohice(int(input(self.text['input']['choice'])))
            self.commit_changes()
        except ValueError:
            print(self.text['input']['invalid'])
        self.clear(2)

    def cohice(self, choice: int) -> None:
        self.clear()
        match choice:
            case 1:
                self.create_lecturer()
            case 2:
                self.create_course()
            case 3:
                self.assign_lecturer()
            case 4:
                self.create_student()
            case 5:
                self.enroll_student()
            case 6:
                self.add_grade()
            case 7:
                self.update_student()
            case 8:
                self.update_course()
            case 9:
                self.update_grade()
            case 10:
                self.print_lecturer()
            case 11:
                self.print_student()
            case 12:
                self.print_course()
            case 0:
                self.close()
                exit(0)
            case _:
                print("Invalid choice!")

    def commit_changes(self) -> None:
        self.base.commit()

    def create_lecturer(self) -> None:
        print(self.text['create']['lecturer']['title'])
        title: str = input(self.text['data']['title']).capitalize()
        name: str = input(self.text['data']['name']).capitalize()
        surname: str = input(self.text['data']['surname']).capitalize()
        try:
            self.base.create_lecturer(title=title, name=name, surname=surname)
        except Exception as e:
            print(e)
            return

    def create_course(self) -> None:
        print(self.text['create']['course']['title'])
        code: str = input(self.text['data']['course_code']).upper()
        name: str = input(self.text['data']['course_name']).capitalize()
        try:
            self.base.create_course(course_code=code, course_name=name)
        except Exception as e:
            print(e)
            return
        print(self.text['create']['course']['successful'])

    def assign_lecturer(self) -> None:
        print(self.text['assign']['title'])
        course_code: str = input(self.text['data']['course_code']).upper()
        lecturer_id: int = int(input(self.text["data"]["lecturer_id"]))
        try:
            self.base.get_lecturer(lecturer_id=lecturer_id)
            self.base.get_course(course_code=course_code)
            self.base.course_lecturer(course_code=course_code, lecturer_id=lecturer_id)
        except Exception as e:
            print(e)
            return
        print(self.text['assign']['successful'])

    def create_student(self) -> None:
        print(self.text['create']['student']['title'])
        id: int = int(input(self.text['data']['student_id']))
        name: str = input(self.text['data']['name']).capitalize()
        surname: str = input(self.text['data']['surname']).capitalize()
        try:
            self.base.create_student(name=name, surname=surname, id=id)
        except Exception as e:
            print(e)
            return

    def enroll_student(self) -> None:
        print(self.text['enroll']['title'])
        student_id: int = int(input(self.text['data']['student_id']))
        course_code: str = input(self.text['data']['course_code']).upper()
        try:
            self.base.enroll_student(student_id=student_id, course_code=course_code)
        except Exception as e:
            print(e)
            return

    def add_grade(self) -> None:
        print(self.text['create']['grade']['title'])
        student_id: int = int(input(self.text['data']['student_id']))
        course_code: str = input(self.text['data']['course_code']).upper()
        grade_input: float = float(input(self.text['data']['grade']))
        try:
            self.base.add_grade(student_id=student_id, course_code=course_code, grade=grade_input)
        except Exception as e:
            print(e)
            return
