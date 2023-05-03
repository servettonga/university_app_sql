import json
import sqlite3
from pathlib import Path


class Populate:
    def __init__(self) -> None:
        # Load configurations
        with open('src/config.json', 'r') as config_file:
            self.config = json.load(config_file)
        self.database = self.config['database']
        self.database = 'src/database/university.db'
        self.sql_command = Path(self.config['sql_commands'] + 'sample_data.sql').read_text()

    def populate_sample_data(self) -> None:
        # Connect to database
        conn = sqlite3.connect(self.database)
        c = conn.cursor()

        # Execute SQL commands
        c.executescript(self.sql_command)

        # Commit and close connection
        conn.commit()
        conn.close()


if __name__ == '__main__':
    populate = Populate()
    populate.populate_sample_data()
    print('Sample data populated successfully')
    print('Database: ' + populate.database)
    print('SQL commands: ' + 'sample_data.sql')
    print('Done')
    exit(0)
