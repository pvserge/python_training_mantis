import string
import random
from model.project import Project


def random_project_name(prefix, maxlen):
    symbols = string.ascii_letters
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def test_add_project(app):
    app.session.login(app.config['webadmin']['username'], app.config['webadmin']['password'])
    project = Project(name=random_project_name("Project_", 10))
    if app.project.count() > 0:
        for item in app.project.get_project_list():
            if item.name == project.name:
                app.project.delete_by_name(project)
    old_project_list = app.project.get_project_list()
    app.project.create(project)
    new_projects_list = app.project.get_project_list()
    old_project_list.append(project)
    assert sorted(old_project_list, key=lambda prj: prj.name) == sorted(new_projects_list, key=lambda prj: prj.name)
    app.session.logout()

