import sqlite3
from typing import Tuple

from constants import (DATABASE,
                       CREATE_TABLE_PROJECTS,
                       CREATE_PROJECT,
                       GET_PROJECTS,
                       GET_PROJECT,
                       CREATE_TABLE_TASKS,
                       CREATE_TASK)


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


def create_project(project: Tuple):
    projects_from_db = get_projects()
    project_from_db = list(filter(lambda p: p[1] == project[0], projects_from_db))
    if len(project_from_db) > 0:
        # Update project
        return

    try:
        # 1. KORAK Kreiranje konekcije
        with sqlite3.connect(DATABASE) as conn:
            # 2. KORAK Kreiranje Cursor objekta za rad s bazom (predstavlja nasu bazu)
            cursor = conn.cursor()

            # 3. KORAK Izvrsavanje SQL Query naredbi
            cursor.execute(CREATE_PROJECT, project)

            # Pokreni postupak snimanja promjena u bazi!!!
            conn.commit()

    except sqlite3.OperationalError as e:
        print(f'Failed to open database: {e}')

    except Exception as ex:
        print(f'Dogodila se greska {ex}.')


def get_project(project_id: int):
    try:
        # 1. KORAK Kreiranje konekcije
        with sqlite3.connect(DATABASE) as conn:
            # 2. KORAK Kreiranje Cursor objekta za rad s bazom (predstavlja nasu bazu)
            cursor = conn.cursor()

            # 3. KORAK Izvrsavanje SQL Query naredbi
            cursor.execute(GET_PROJECT, (project_id,))
            projects = cursor.fetchall()

            # Vrati podatke koji su dohvaceni iz baze
            if len(projects) > 0:
                return projects[0]
            else:
                return None

    except sqlite3.OperationalError as e:
        print(f'Failed to open database: {e}')

    except Exception as ex:
        print(f'Dogodila se greska {ex}.')


def get_projects():
    try:
        # 1. KORAK Kreiranje konekcije
        with sqlite3.connect(DATABASE) as conn:
            # 2. KORAK Kreiranje Cursor objekta za rad s bazom (predstavlja nasu bazu)
            cursor = conn.cursor()

            # 3. KORAK Izvrsavanje SQL Query naredbi
            cursor.execute(GET_PROJECTS)
            projects = cursor.fetchall()

            # Vrati podatke koji su dohvaceni iz baze
            if len(projects) > 0:
                return projects
            else:
                return None

    except sqlite3.OperationalError as e:
        print(f'Failed to open database: {e}')

    except Exception as ex:
        print(f'Dogodila se greska {ex}.')


def create_task(project_id: int):
    # TODO Provjeriti postoji li ovaj projekt u bazi?
    # Ako postoji azuriraj ga, a ako ne postoji kreiraj ga

    try:
        # 1. KORAK Kreiranje konekcije
        with sqlite3.connect(DATABASE) as conn:
            # 2. KORAK Kreiranje Cursor objekta za rad s bazom (predstavlja nasu bazu)
            cursor = conn.cursor()

            # 3. KORAK Izvrsavanje SQL Query naredbi
            cursor.execute(CREATE_TASK,
                           ('Task 1', 1, 1,
                            '2025-01-31', '2025-02-10', project_id))

            # Pokreni postupak snimanja promjena u bazi!!!
            conn.commit()

    except sqlite3.OperationalError as e:
        print(f'Failed to open database: {e}')

    except Exception as ex:
        print(f'Dogodila se greska {ex}.')
