from selenium.webdriver.support.ui import Select
from model.project import Project


class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def open_project_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/manage_proj_page.php") and
                len(wd.find_elements_by_xpath("//input[@value='Create New Project']")) > 0):
            wd.find_element_by_link_text("Manage").click()
            wd.find_element_by_link_text("Manage Projects").click()

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def select_field_value(self, field_name, value):
        wd = self.app.wd
        if value is not None:
            Select(wd.find_element_by_name(field_name)).select_by_visible_text(value)

    def set_checkbox(self, checkbox_name, value):
        wd = self.app.wd
        if value is not None:
            if not wd.find_element_by_name('inherit_global').is_selected():
                wd.find_element_by_name(checkbox_name).click()

    def fill_form(self, project):
        self.change_field_value("name", project.name)
        self.select_field_value("status", project.status)
        self.set_checkbox("inherit_global", project.inherit)
        self.change_field_value("view_state", project.viewstate)
        self.change_field_value("description", project.description)

    def create(self, project):
        wd = self.app.wd
        # open edit page
        self.open_project_page()
        wd.find_element_by_xpath("//input[@value='Create New Project']").click()
        # fill contact form
        self.fill_form(project)
        # submit form
        wd.find_element_by_xpath("//input[@value='Add Project']").click()
        self.open_project_page()
        self.project_cache = None

    def count(self):
        wd = self.app.wd
        self.open_project_page()
        return len(wd.find_elements_by_xpath("//a[contains(@href,'manage_proj_edit_page.php?project_id=')]"))

    project_cache = None

    def get_project_list(self):
        if self.project_cache is None:
            wd = self.app.wd
            self.open_project_page()
            self.project_cache = []
            for element in wd.find_elements_by_xpath("//a[contains(@href,'manage_proj_edit_page.php?project_id=')]"):
                text = element.text
                self.project_cache.append(Project(name=text))
        return list(self.project_cache)

    def delete_by_name(self, project):
        wd = self.app.wd
        self.open_project_page()
        # click on project name
        wd.find_element_by_xpath("//a[contains(text(),'%s')]" % project.name).click()
        # click Delete button
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()
        # confirm deletion
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()
        self.open_project_page()
        self.project_cache = None
