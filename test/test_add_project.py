from model.project import Project


def test_add_project(app):
    project = Project(name="777")
    if app.project.count() > 0:
        for item in app.project.get_project_list():
            if item.name == project.name:
                app.project.delete_by_name(project)
    old_project_list = app.project.get_project_list()
    app.project.create(project)
    new_projects_list = app.project.get_project_list()
    old_project_list.append(project)
    assert sorted(old_project_list, key=lambda prj: prj.name) == sorted(new_projects_list, key=lambda prj: prj.name)
