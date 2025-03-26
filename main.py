from repositories import (init_database,
                          create_project,
                          create_task,
                          get_projects,
                          get_project)

from repositories.sa_db_repo import (Base, engine)


def main():
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

    Base.metadata.create_all(engine)


if __name__ == '__main__':
    main()
