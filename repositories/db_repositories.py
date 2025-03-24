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

