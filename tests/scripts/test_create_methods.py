import pytest


def test_create_lecturer_creates_with_parameters(unpopulated, db) -> None:
    ph: dict[str, str] = {'title': 'Dr.', 'name': 'Ethan', 'surname': 'Brown'}
    unpopulated.create_lecturer(title=ph['title'], name=ph['name'], surname=ph['surname'])
    db.execute('SELECT * FROM lecturer WHERE name = :name AND surname = :surname', ph)
    result = db.fetchone()
    assert result[1] == ph['title']
    assert result[2] == ph['name']
    assert result[3] == ph['surname']

def test_create_lecturer_raises_error_with_missing_parameters(unpopulated) -> None:
    with pytest.raises(TypeError):
        unpopulated.create_lecturer()

def test_create_lecturer_raises_error_with_invalid_parameters(unpopulated) -> None:
    with pytest.raises(TypeError):
        unpopulated.create_lecturer(title='Dr.', name='Ethan', surname='Brown', email='XXXXXXXXXXXXXXX')

def test_create_course_creates_with_parameters(unpopulated, db) -> None:
    ph: dict[str, str] = {'code': 'CS101', 'name': 'Introduction to CS'}
    unpopulated.create_course(course_code=ph['code'], course_name=ph['name'])
    db.execute('SELECT * FROM course WHERE code = :code', ph)
    result = db.fetchone()
    assert result[0] == ph['code']
    assert result[1] == ph['name']

def test_create_course_raises_error_with_missing_parameters(unpopulated) -> None:
    with pytest.raises(TypeError):
        unpopulated.create_course()

def test_create_course_doesnt_create_duplicate_courses(unpopulated) -> None:
    with pytest.raises(Exception) as e_info:
        unpopulated.create_course(course_code='CS101', course_name='Introduction to CS')
        unpopulated.create_course(course_code='CS101', course_name='Introduction to CS')
    assert str(e_info.value) == unpopulated.text['create']['course']['course_exists']

def test_create_student_creates_with_parameters(unpopulated, db) -> None:
    ph: dict[str, str] = {'name': 'Mike', 'surname': 'Doe', 'id': 20230001}
    unpopulated.create_student(name=ph['name'], surname=ph['surname'], id=ph['id'])
    db.execute('SELECT * FROM student WHERE name = :name AND surname = :surname AND id = :id', ph)
    result = db.fetchone()
    assert result[0] == ph['id']
    assert result[1] == ph['name']
    assert result[2] == ph['surname']

def test_create_student_raises_error_with_missing_parameters(unpopulated) -> None:
    with pytest.raises(TypeError):
        unpopulated.create_student()

def test_create_student_raises_error_with_invalid_parameters(unpopulated) -> None:
    with pytest.raises(TypeError):
        unpopulated.create_student(name='Mike', surname='Doe', id='20230001', email='XXXXXXXXXXXXXXX')

def test_create_student_raises_error_with_duplicate_id(unpopulated) -> None:
    with pytest.raises(Exception) as e_info:
        unpopulated.create_student(name='Mike', surname='Doe', id=20230001)
        unpopulated.create_student(name='Mike', surname='Doe', id=20230001)
    assert str(e_info.value) == unpopulated.text['create']['student']['student_exists']
