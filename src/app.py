import os
import time
from abc import ABC, abstractmethod

from src.university import University


class App(ABC):

    def __init__(self):
        self.base = University()
        self.base.connect()
        self.choices: dict[int, str] = {
            1: "Create a new lecturer",
            2: "Create a new student",
            3: "Create a new course",
            4: "Enroll a student to a course",
            5: "Add a new grade",
            6: "Update lecturer",
            7: "Update student",
            8: "Update course",
            9: "Update grade",
            10: "Lecturer information",
            11: "Student information",
            12: "Course information",
            0: "Exit"}
        self.header = """
        +-+-+-+-+-+-+-+-+-+-+-+-+-+-+
        |U|N|I|V|E|R|S|I|T|Y| |A|P|P|
        +-+-+-+-+-+-+-+-+-+-+-+-+-+-+
        """

    @abstractmethod
    def clear(self, n: int = 0):
        time.sleep(n)
        os.system("cls" if os.name == "nt" else "clear")
