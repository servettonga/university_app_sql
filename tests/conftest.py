import json

import pytest

from src.populate import Populate
from src.university import University

# Configurations
with open('src/config.json', 'r') as config_file:
    config = json.load(config_file)
database = config['database']
temp_db = config['temp_db']
raw_sql_path = config['sql_commands']

@pytest.fixture(scope='session')
def text():
    with open('src/text.json', 'r') as text:
        text = json.load(text)
    return text

@pytest.fixture(scope='session')
def populated(text):
    # Create University App
    university = University(database, raw_sql_path)
    populate = Populate()
    populate.populate_sample_data()
    return university

@pytest.fixture(scope='session')
def unpopulated(text):
    # Create University App
    university = University(temp_db, raw_sql_path)
    university._drop_tables()
    university._create_tables()
    return university
