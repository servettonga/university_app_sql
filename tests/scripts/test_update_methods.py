import pytest


def test_update_lecturer_updates_name(populated):
    before = populated.get_lecturer(lecturer_id=1)
    ph = {'id': 1, 'title': 'Dr.', 'name': 'Philip', 'surname': 'Smith'}
    populated.update_lecturer(lecturer_id=ph['id'], title=ph['title'], name=ph['name'], surname=ph['surname'])
    after = populated.get_lecturer(lecturer_id=1)
    assert before[0][2] != ph['name']
    assert before != after

def test_update_lecturer_updates_surname(populated):
    before = populated.get_lecturer(lecturer_id=1)
    ph = {'id': 1, 'title': 'Dr.', 'name': 'Philip', 'surname': 'Lee'}
    populated.update_lecturer(lecturer_id=ph['id'], title=ph['title'], name=ph['name'], surname=ph['surname'])
    after = populated.get_lecturer(lecturer_id=1)
    assert before[0][3] != ph['surname']
    assert before != after

def test_update_lecturer_updates_title(populated):
    before = populated.get_lecturer(lecturer_id=1)
    ph = {'id': 1, 'title': 'Prof.', 'name': 'John', 'surname': 'Smith'}
    populated.update_lecturer(lecturer_id=ph['id'], title=ph['title'], name=ph['name'], surname=ph['surname'])
    after = populated.get_lecturer(lecturer_id=1)
    assert before[0][1] != ph['title']
    assert before != after

def test_update_lecturer_raises_error_if_lecturer_does_not_exist(populated):
    with pytest.raises(Exception) as e_info:
        populated.update_lecturer(lecturer_id=100, title='Dr.', name='Philip', surname='Smith')
    assert str(e_info.value) == populated.text['get']['lecturer_not_found']

def test_update_course_updates_name(populated):
    before = populated.get_course(course_code='CS102')
    ph = {'course_code': 'CS102', 'name': 'Data Structures and Algorithms'}
    populated.update_course(course_code=ph['course_code'], new_code=ph['course_code'], new_name=ph['name'])
    after = populated.get_course(course_code='CS102')
    assert before[0][1] != ph['name']
    assert before != after

def test_update_course_updates_code(populated):
    before = populated.get_course(course_code='CS102')
    ph = {'course_code': 'CS102', 'name': 'Data Structures and Algorithms', 'new_code': 'CS108'}
    populated.update_course(course_code=ph['course_code'], new_code=ph['new_code'], new_name=ph['name'])
    after = populated.get_course(course_code='CS108')
    assert before[0][0] != ph['new_code']
    assert after[0][0] == ph['new_code']
    assert before != after

def test_update_course_raises_error_if_course_does_not_exist(populated):
    with pytest.raises(Exception) as e_info:
        populated.update_course(course_code='CS202', new_code='CS108', new_name='Data Structures and Algorithms')
    assert str(e_info.value) == populated.text['get']['course_not_found']

def test_update_course_lecturer_updates_not_assigned_course(populated):
    ph = {'course_code': 'CS106', 'lecturer_id': 1}
    before = populated.get_course(course_code=ph['course_code'])
    populated.course_lecturer(course_code=ph['course_code'], lecturer_id=ph['lecturer_id'])
    after = populated.get_course(course_code=ph['course_code'])
    assert before[0][2] != ph['lecturer_id']
    assert before != after

def test_update_course_lecturer_raises_error_if_already_assigned(populated):
    ph = {'course_code': 'CS102', 'lecturer_id': 1}
    with pytest.raises(Exception) as e_info:
        populated.course_lecturer(course_code=ph['course_code'], lecturer_id=ph['lecturer_id'])
    assert str(e_info.value) == populated.text['update']['assign']['already_assigned']

def test_update_student_updates_name(populated):
    before = populated.get_student(student_id=20230001)
    ph = {'id': 20230001, 'new_id': 20230001, 'name': 'Philip', 'surname': 'Doe'}
    populated.update_student(id=ph['id'], new_id=ph['new_id'], name=ph['name'], surname=ph['surname'])
    after = populated.get_student(student_id=20230001)
    assert before[0][1] != ph['name']
    assert before != after

def test_update_student_updates_surname(populated):
    ph = {'id': 20230001, 'new_id': 20230001, 'name': 'Philip', 'surname': 'Lee'}
    before = populated.get_student(student_id=ph['id'])
    populated.update_student(id=ph['id'], new_id=ph['new_id'], name=ph['name'], surname=ph['surname'])
    after = populated.get_student(student_id=ph['id'])
    assert before[0][2] != ph['surname']
    assert before != after

def test_update_student_updates_id(populated):
    ph = {'id': 20230001, 'new_id': 20230102, 'name': 'Philip', 'surname': 'Doe'}
    before = populated.get_student(student_id=ph['id'])
    populated.update_student(id=ph['id'], new_id=ph['new_id'], name=ph['name'], surname=ph['surname'])
    after = populated.get_student(student_id=ph['new_id'])
    assert before[0][0] != ph['new_id']
    assert before != after

def test_update_student_raises_error_if_student_does_not_exist(populated):
    with pytest.raises(Exception) as e_info:
        populated.update_student(id=100, new_id=100, name='Philip', surname='Doe')
    assert str(e_info.value) == populated.text['get']['student_not_found']

def test_update_student_raises_error_if_student_id_already_exists(populated):
    ph = {'id': 20230001, 'new_id': 20230002, 'name': 'Philip', 'surname': 'Doe'}
    with pytest.raises(Exception) as e_info:
        populated.update_student(id=ph['id'], new_id=ph['new_id'], name=ph['name'], surname=ph['surname'])
    assert str(e_info.value) == populated.text['update']['student']['student_exists']

def test_enroll_student_enrolls_not_enrolled_course(populated):
    ph = {'student_id': 20230001, 'course_code': 'CS105'}
    before = populated.is_enrolled(id=ph['student_id'], code=ph['course_code'])
    populated.enroll_student(student_id=ph['student_id'], course_code=ph['course_code'])
    after = populated.is_enrolled(id=ph['student_id'], code=ph['course_code'])
    assert before is False
    assert after is True

def test_enroll_student_raises_error_if_student_does_not_exist(populated):
    with pytest.raises(Exception) as e_info:
        populated.enroll_student(student_id=100, course_code='CS105')
    assert str(e_info.value) == populated.text['get']['student_not_found']

def test_enroll_student_raises_error_if_course_does_not_exist(populated):
    with pytest.raises(Exception) as e_info:
        populated.enroll_student(student_id=20230001, course_code='CS202')
    assert str(e_info.value) == populated.text['get']['course_not_found']

def test_enroll_student_raises_error_if_course_already_enrolled(populated):
    ph = {'student_id': 20230001, 'course_code': 'CS102'}
    with pytest.raises(Exception) as e_info:
        populated.enroll_student(student_id=ph['student_id'], course_code=ph['course_code'])
    assert str(e_info.value) == populated.text['update']['enroll']['already_enrolled']

def test_add_grade_adds_grade_for_enrolled_course_not_graded(populated):
    ph = {'student_id': 20230002, 'course_code': 'CS101', 'grade': 4.3}
    before = populated.get_grade(student_id=ph['student_id'], course_code=ph['course_code'])
    populated.add_grade(student_id=ph['student_id'], course_code=ph['course_code'], grade=ph['grade'])
    after = populated.get_grade(student_id=ph['student_id'], course_code=ph['course_code'])
    assert before is None
    assert after == ph['grade']

def test_add_grade_raises_error_if_student_does_not_exist(populated):
    with pytest.raises(Exception) as e_info:
        populated.add_grade(student_id=100, course_code='CS101', grade=4.3)
    assert str(e_info.value) == populated.text['get']['student_not_found']

def test_add_grade_raises_error_if_course_does_not_exist(populated):
    with pytest.raises(Exception) as e_info:
        populated.add_grade(student_id=20230002, course_code='CS202', grade=4.3)
    assert str(e_info.value) == populated.text['get']['course_not_found']

def test_add_grade_raises_error_if_course_already_graded(populated):
    ph = {'student_id': 20230002, 'course_code': 'CS102', 'grade': 4.3}
    with pytest.raises(Exception) as e_info:
        populated.add_grade(student_id=ph['student_id'], course_code=ph['course_code'], grade=ph['grade'])
    assert str(e_info.value) == populated.text['create']['grade']['alread_graded']

def test_add_grade_raises_error_if_not_enrolled(populated):
    ph = {'student_id': 20230001, 'course_code': 'CS105', 'grade': 4.3}
    with pytest.raises(Exception) as e_info:
        populated.add_grade(student_id=ph['student_id'], course_code=ph['course_code'], grade=ph['grade'])
    assert str(e_info.value) == populated.text['create']['grade']['not_enrolled']

def test_update_grade_updates_existing_grade(populated):
    ph = {'student_id': 20230001, 'course_code': 'CS101', 'grade': 4.3}
    before = populated.get_grade(student_id=ph['student_id'], course_code=ph['course_code'])
    populated.update_grade(student_id=ph['student_id'], course_code=ph['course_code'], grade=ph['grade'])
    after = populated.get_grade(student_id=ph['student_id'], course_code=ph['course_code'])
    assert before != ph['grade']
    assert after == ph['grade']

def test_update_grade_raises_error_if_student_does_not_exist(populated):
    with pytest.raises(Exception) as e_info:
        populated.update_grade(student_id=100, course_code='CS101', grade=4.3)
    assert str(e_info.value) == populated.text['get']['student_not_found']

def test_update_grade_raises_error_if_course_does_not_exist(populated):
    with pytest.raises(Exception) as e_info:
        populated.update_grade(student_id=20230001, course_code='CS202', grade=4.3)
    assert str(e_info.value) == populated.text['get']['course_not_found']

def test_update_grade_raises_error_if_course_not_graded(populated):
    ph = {'student_id': 20230002, 'course_code': 'CS101', 'grade': 4.3}
    with pytest.raises(Exception) as e_info:
        populated.update_grade(student_id=ph['student_id'], course_code=ph['course_code'], grade=ph['grade'])
    assert str(e_info.value) == populated.text['update']['grade']['not_graded']
