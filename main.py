from datetime import datetime as dt
from repositories import (init_database,
                          create_project,
                          create_task,
                          get_projects,
                          get_project)

from repositories.sa_db_repo import (Base, engine, Project, Task, session)


def main():
    #region SQLITE3 module
    # init_database()
    # project = ('Demo project 12', '2024-12-06', '2025-03-10')
    # create_project(project)

    # project_id = 6 # TODO Dohvatiti iz baze!!!
    # task = ('Task 12', 1, 1,
    #         '2024-12-06', '2025-03-10', project_id)
    # create_task(task)

    # project = get_project(5)
    # print(project)

    # projects = get_projects()
    # print(projects)
    #endregion

    Base.metadata.create_all(engine)

    project = Project(name='Integrate SQL Alchemy',
                      begin_date=dt.strptime('2025-01-31', '%Y-%m-%d'),
                      end_date=dt.strptime('2025-02-28', '%Y-%m-%d'))

    task = Task(name = 'Install SQL Alchemy',
                priority = 'High',
                status = 'New',
                begin_date = dt(2025, 1, 31, 15, 35),  #.strptime('2025-01-31', '%Y-%m-%d'),
                end_date = dt.strptime('2025-01-31', '%Y-%m-%d'))

    task.project = project
    session.add_all([project, task])

    session.commit()



if __name__ == '__main__':
    main()
