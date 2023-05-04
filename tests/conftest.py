import json
import sqlite3

import pytest

from src.populate import Populate
from src.university import University

# Configurations
with open('src/config.json', 'r') as config_file:
    config = json.load(config_file)
university_db = config['database']
temp_db = config['temp_db']
raw_sql_path = config['sql_commands']

@pytest.fixture(scope='session')
def text():
    with open('src/text.json', 'r') as text:
        text = json.load(text)
    return text

@pytest.fixture(scope='function')
def populated(text):
    # Create University App
    university = University(university_db, raw_sql_path)
    populate = Populate()
    populate.populate_sample_data()
    yield university
    university.connection.close()

@pytest.fixture(scope='function')
def unpopulated(text):
    # Create University App
    university = University(temp_db, raw_sql_path)
    university._create_tables()
    yield university
    university._drop_tables()
    university.connection.close()

@pytest.fixture(scope='session')
def db():
    connection = sqlite3.connect(temp_db)
    cursor = connection.cursor()
    yield cursor
    connection.commit()
    connection.close()
