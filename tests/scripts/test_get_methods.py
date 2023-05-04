import pytest


def test_get_lecturer_returns_existing_entry(populated) -> None:
    for row in populated.get_lecturer(lecturer_id=1):
        assert row[0] == 1
        assert row[1] == 'Dr.'
        assert row[2] == 'John'
        assert row[3] == 'Smith'

def test_get_lecturer_raises_exception_for_non_existent_entry(populated) -> None:
    with pytest.raises(Exception) as e_info:
        populated.get_lecturer(lecturer_id=100)
    assert str(e_info.value) == populated.text['get']['lecturer_not_found']

def test_get_lecturers_returns_existing_entry(populated) -> None:
    rows = populated.get_lecturers()
    assert rows[0][0] == 1
    assert rows[0][1] == 'Dr.'
    assert rows[0][2] == 'John'
    assert rows[0][3] == 'Smith'

def test_is_lecturer_assigned_returns_true_for_assigned_lecturer(populated) -> None:
    assert populated.is_lecturer_assigned(course_code='CS101')

def test_is_lecturer_assigned_returns_false_for_unassigned_lecturer(populated) -> None:
    assert not populated.is_lecturer_assigned(course_code='CS106')

def test_get_lecturers_raises_exception_for_no_lecturers(unpopulated) -> None:
    with pytest.raises(Exception) as e_info:
        unpopulated.get_lecturers()
    assert str(e_info.value) == unpopulated.text['get']['lecturers_not_found']

def test_get_lecturer_courses_returns_existing_entry(populated) -> None:
    for row in populated.get_lecturer_courses(lecturer_id=1):
        assert row[0] == 'CS101'
        assert row[1] == 'Introduction to CS'

def test_get_lecturer_courses_returns_empty_list_for_not_assigned_lecturer(populated) -> None:
    assert populated.get_lecturer_courses(lecturer_id=6) == []

def test_get_course_returns_existing_entry(populated) -> None:
    for row in populated.get_course(course_code='CS101'):
        assert row[0] == 'CS101'
        assert row[1] == 'Introduction to CS'

def test_get_course_raises_exception_for_non_existent_entry(populated) -> None:
    with pytest.raises(Exception) as e_info:
        populated.get_course(course_code='CS202')
    assert str(e_info.value) == populated.text['get']['course_not_found']

def test_get_courses_returns_existing_entry(populated) -> None:
    rows = populated.get_courses()
    assert rows[0][0] == 'CS101'
    assert rows[0][1] == 'Introduction to CS'
    assert rows[0][2] == 'Dr.'
    assert rows[0][3] == 'John'
    assert rows[0][4] == 'Smith'
    assert rows[5][0] == 'CS106'
    assert rows[5][1] == 'EMPTY COURSE'
    assert rows[5][2] is None

def test_get_courses_raises_exception_for_no_courses(unpopulated) -> None:
    with pytest.raises(Exception) as e_info:
        unpopulated.get_courses()
    assert str(e_info.value) == unpopulated.text['get']['courses_not_found']

def test_get_student_returns_existing_entry(populated) -> None:
    for row in populated.get_student(student_id=20230001):
        assert row[0] == 20230001
        assert row[1] == 'Mike'
        assert row[2] == 'Doe'

def test_get_student_raises_exception_for_non_existent_entry(populated) -> None:
    with pytest.raises(Exception) as e_info:
        populated.get_student(student_id=100)
    assert str(e_info.value) == populated.text['get']['student_not_found']

def test_get_students_returns_existing_entry(populated) -> None:
    rows = populated.get_students()
    assert rows[0][0] == 20230001
    assert rows[0][1] == 'Mike'
    assert rows[0][2] == 'Doe'

def test_get_students_raises_exception_for_no_students(unpopulated) -> None:
    with pytest.raises(Exception) as e_info:
        unpopulated.get_students()
    assert str(e_info.value) == unpopulated.text['get']['students_not_found']

def test_is_enrolled_returns_true_for_existing_entry(populated) -> None:
    assert populated.is_enrolled(id=20230001, code='CS101')

def test_is_enrolled_returns_false_for_non_existent_entry(populated) -> None:
    assert not populated.is_enrolled(id=20230001, code='CS105')

def test_get_student_enrollments_returns_existing_entry(populated) -> None:
    rows = populated.get_student_enrollments(student_id=20230001)
    assert rows[0][1] == 'CS101'
    assert rows[0][2] == 20230001
    assert rows[0][3] == 4.5
    assert rows[1][1] == 'CS102'
    assert rows[1][2] == 20230001
    assert rows[1][3] == 3.2
    assert rows[2][1] == 'CS103'
    assert rows[2][2] == 20230001
    assert rows[2][3] == 2.7
    assert rows[3][1] == 'CS104'
    assert rows[3][2] == 20230001
    assert rows[3][3] == 4.0

def test_get_student_enrollments_returns_empty_list_for_not_enrolled(populated) -> None:
    assert populated.get_student_enrollments(student_id=20230018) == []

def test_get_grade_returns_existing_entry(populated) -> None:
    assert populated.get_grade(student_id=20230001, course_code='CS101') == 4.5

def test_get_grade_returns_none_for_non_existent_grade(populated) -> None:
    assert populated.get_grade(student_id=20230002, course_code='CS101') is None

def test_get_grade_raises_exception_for_non_existent_student(populated) -> None:
    with pytest.raises(Exception) as e_info:
        populated.get_grade(student_id=100, course_code='CS101')
    assert str(e_info.value) == populated.text['get']['student_not_found']

def test_get_course_grades_returns_existing_entry(populated) -> None:
    rows = populated.get_course_grades(course_code='CS101')
    assert rows[0][0] == 20230001
    assert rows[0][1] == 'Mike'
    assert rows[0][2] == 'Doe'
    assert rows[0][3] == 4.5
    assert rows[1][0] == 20230002
    assert rows[1][1] == 'Samantha'
    assert rows[1][2] == 'Doe'
    assert rows[1][3] is None

def test_get_course_grades_returns_empty_list_for_not_enrolled(populated) -> None:
    assert populated.get_course_grades(course_code='CS106') == []
