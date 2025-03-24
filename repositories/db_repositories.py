import sqlite3
from constants import (DATABASE,
                       CREATE_TABLE_PROJECTS,
                       CREATE_TABLE_TASKS)


def init_database():
    create_tables_statements = [
        CREATE_TABLE_PROJECTS,
        CREATE_TABLE_TASKS
    ]

    try:
        # 1. KORAK Kreiranje konekcije
        with sqlite3.connect(DATABASE) as conn:
            # 2. KORAK Kreiranje Cursor objekta za rad s bazom (predstavlja nasu bazu)
            cursor = conn.cursor()

            # 3. KORAK Izvrsavanje SQL Query naredbi
            for statement in create_tables_statements:
                cursor.execute(statement)

            # Pokreni postupak snimanja promjena u bazi!!!
            conn.commit()

            # 4. KORAK Zatvarnje konekcije na bazu
            # - with automatski zatvara konekciju
            # conn.close()
    except sqlite3.OperationalError as e:
        print(f'Failed to open database: {e}')

    except Exception as ex:
        print(f'Dogodila se greska {ex}.')


def create_project():
    insert_project_statement = '''
        INSERT INTO projects(name, begin_date, end_date)
        VALUES(?, ?, ?)
    '''

    # TODO Provjeriti postoji li ovaj projekt u bazi?
    # Ako postoji azuriraj ga, a ako ne postoji kreiraj ga

    try:
        # 1. KORAK Kreiranje konekcije
        with sqlite3.connect(DATABASE) as conn:
            # 2. KORAK Kreiranje Cursor objekta za rad s bazom (predstavlja nasu bazu)
            cursor = conn.cursor()

            # 3. KORAK Izvrsavanje SQL Query naredbi
            cursor.execute(insert_project_statement, ('Priject name', '2025-01-25', '2025-02-28'))

            # Pokreni postupak snimanja promjena u bazi!!!
            conn.commit()

    except sqlite3.OperationalError as e:
        print(f'Failed to open database: {e}')

    except Exception as ex:
        print(f'Dogodila se greska {ex}.')


def get_project():
    pass


def get_projects():
    pass


def create_task(project_id: int):
    insert_task_statement = '''
        INSERT INTO tasks(name, priority, status_id,
                            begin_date, end_date, project_id)
        VALUES(?, ?, ?, ?, ?, ?)
    '''

    # TODO Provjeriti postoji li ovaj projekt u bazi?
    # Ako postoji azuriraj ga, a ako ne postoji kreiraj ga

    try:
        # 1. KORAK Kreiranje konekcije
        with sqlite3.connect(DATABASE) as conn:
            # 2. KORAK Kreiranje Cursor objekta za rad s bazom (predstavlja nasu bazu)
            cursor = conn.cursor()

            # 3. KORAK Izvrsavanje SQL Query naredbi
            cursor.execute(insert_task_statement,
                           ('Task 1', 1, 1,
                            '2025-01-31', '2025-02-10', project_id))

            # Pokreni postupak snimanja promjena u bazi!!!
            conn.commit()

    except sqlite3.OperationalError as e:
        print(f'Failed to open database: {e}')

    except Exception as ex:
        print(f'Dogodila se greska {ex}.')
