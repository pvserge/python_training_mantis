from model.project import Project
import random


def test_delete_project(app):
    if app.project.count() == 0:
        app.project.create(Project(name="New Project"))
    old_project_list = app.project.get_project_list()
    project = random.choice(old_project_list)
    app.project.delete_by_name(project)
    new_projects_list = app.project.get_project_list()
    old_project_list.remove(project)
    assert sorted(old_project_list, key=lambda prj: prj.name) == sorted(new_projects_list, key=lambda prj: prj.name)
