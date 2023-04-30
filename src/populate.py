from sqlalchemy import create_engine, update
from sqlalchemy.orm import sessionmaker

from database.model import Course, Lecturer, Student

engine = create_engine("sqlite:///database/university.db", echo=True)
Session = sessionmaker(bind=engine)
session = Session()

Lecturer.__table__.drop(bind=engine)
Course.__table__.drop(bind=engine)
Student.__table__.drop(bind=engine)
# Grade.__table__.drop(bind=engine)

Lecturer.__table__.create(bind=engine, checkfirst=True)
Course.__table__.create(bind=engine, checkfirst=True)
Student.__table__.create(bind=engine, checkfirst=True)
# Grade.__table__.create(bind=engine, checkfirst=True)

lecturers = [
    {'Title': 'Dr.', 'Name': 'John', 'Surname': 'Smith'},
    {'Title': 'Prof.', 'Name': 'Jane', 'Surname': 'Doe'},
    {'Title': 'Dr.', 'Name': 'Michael', 'Surname': 'Johnson'},
    {'Title': 'Prof.', 'Name': 'Sarah', 'Surname': 'Lee'}
]

courses_dict = [
    {'CourseCode': 'CS101', 'CourseName': 'Introduction to CS'},
    {'CourseCode': 'CS102', 'CourseName': 'Data Structures and Algos'},
    {'CourseCode': 'CS103', 'CourseName': 'Computer Networks'},
    {'CourseCode': 'CS104', 'CourseName': 'Operating Systems'},
    {'CourseCode': 'CS105', 'CourseName': 'Artificial Intelligence'}
]

students = [
    {'StudentID': 1, 'Name': 'John', 'Surname': 'Doe'},
    {'StudentID': 2, 'Name': 'Jane', 'Surname': 'Smith'},
    {'StudentID': 3, 'Name': 'Bob', 'Surname': 'Johnson'},
    {'StudentID': 4, 'Name': 'Mary', 'Surname': 'Brown'},
    {'StudentID': 5, 'Name': 'Jack', 'Surname': 'Davis'}
]

grades = [
    {'StudentID': 1, 'CourseCode': 'CS101', 'Grade': 4.0},
    {'StudentID': 1, 'CourseCode': 'CS102', 'Grade': 3.0},
    {'StudentID': 1, 'CourseCode': 'CS103', 'Grade': 2.0},
    {'StudentID': 1, 'CourseCode': 'CS104', 'Grade': 1.0},
    {'StudentID': 1, 'CourseCode': 'CS105', 'Grade': 5.0},
    {'StudentID': 2, 'CourseCode': 'CS101', 'Grade': 2.0},
    {'StudentID': 2, 'CourseCode': 'CS102', 'Grade': 1.0},
    {'StudentID': 2, 'CourseCode': 'CS103', 'Grade': 5.0},
    {'StudentID': 2, 'CourseCode': 'CS104', 'Grade': 4.0},
    {'StudentID': 2, 'CourseCode': 'CS105', 'Grade': 3.0},
    {'StudentID': 3, 'CourseCode': 'CS101', 'Grade': 3.0},
    {'StudentID': 3, 'CourseCode': 'CS102', 'Grade': 2.0},
    {'StudentID': 3, 'CourseCode': 'CS103', 'Grade': 1.0},
    {'StudentID': 3, 'CourseCode': 'CS104', 'Grade': 5.0},
    {'StudentID': 3, 'CourseCode': 'CS105', 'Grade': 4.0},
    {'StudentID': 4, 'CourseCode': 'CS101', 'Grade': 1.0},
    {'StudentID': 4, 'CourseCode': 'CS102', 'Grade': 2.0},
    {'StudentID': 4, 'CourseCode': 'CS103', 'Grade': 5.0},
    {'StudentID': 4, 'CourseCode': 'CS104', 'Grade': 4.0},
    {'StudentID': 4, 'CourseCode': 'CS105', 'Grade': 3.0},
    {'StudentID': 5, 'CourseCode': 'CS101', 'Grade': 2.0},
    {'StudentID': 5, 'CourseCode': 'CS102', 'Grade': 1.0},
    {'StudentID': 5, 'CourseCode': 'CS103', 'Grade': 5.0},
    {'StudentID': 5, 'CourseCode': 'CS104', 'Grade': 4.0},
    {'StudentID': 5, 'CourseCode': 'CS105', 'Grade': 3.0}
    ]

courses = [course['CourseCode'] for course in courses_dict]

for lecturer in lecturers:
    session.add(Lecturer(title=lecturer['Title'], name=lecturer['Name'], surname=lecturer['Surname']))
    session.commit()

for course in courses_dict:
    session.add(Course(code=course['CourseCode'], name=course['CourseName']))
    session.commit()

for student in students:
    session.add(Student(id=student['StudentID'], name=student['Name'], surname=student['Surname']))
    session.commit()

# for grade in grades:
#     session.add(Grade(student_id=grade['StudentID'], course_code=grade['CourseCode'], grade=grade['Grade']))
#     session.commit()

# for student in students:
#     session.execute(update(Student).where(Student.id == student['StudentID']).values(course_code=courses))
#     session.commit()
# session.execute(Student.__table__.insert(), courses)

# task = session.query(Lecturer).where(Lecturer.id == 2)

# task = session.query(Grade).where(Grade.student_id == 1, Grade.course_code == 'CSCI-111')
# if task.first() is not None:
#     session.execute(update(Grade).where(Grade.student_id == 1, Grade.course_code == 'CSCI-111').values(grade=5.0))
#     session.commit()
# else:
#     session.add(Grade(student_id=1, course_code='CSCI-111', grade=5.0))
#     session.commit()


# task = session.query(Student).where(Student.id == 1012023)
# if task.first() is not None:
#     session.execute(update(Student).where(Student.id == 1012023).values(name='Joey'))
#     session.commit()
# else:
#     session.add(Student(id=1012023, name='Joey', surname='Smith', course_code='CSCI-111'))
#     session.commit()

print(session.query(Lecturer).all())
print(session.query(Course).all())
print(session.query(Student).all())
# print(session.query(Grade).all())
