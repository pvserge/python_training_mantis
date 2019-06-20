from model.project import Project
import random


def test_delete_project(app):
    username = app.config['webadmin']['username']
    password = app.config['webadmin']['password']
    app.session.login(username, password)
    if len(app.soap.get_project_list(username, password)) == 0:
        app.project.create(Project(name="New Project"))
    old_project_list = app.soap.get_project_list(username, password)
    project = random.choice(old_project_list)
    app.project.delete_by_name(project)
    new_projects_list = app.soap.get_project_list(username, password)
    old_project_list.remove(project)
    assert sorted(old_project_list, key=lambda prj: prj.name) == sorted(new_projects_list, key=lambda prj: prj.name)
    app.session.logout()

