from suds.client import Client
from suds import WebFault
from model.project import Project


class SoapHelper:

    def __init__(self, app):
        self.app = app
        self.client = Client("http://localhost/mantisbt-1.2.20/api/soap/mantisconnect.php?wsdl")

    def can_login(self, username, password):
        try:
            self.client.service.mc_login(username, password)
            return True
        except WebFault:
            return False

    def get_project_list(self, username, password):
        pr_list = []
        try:
            projects = self.client.service.mc_projects_get_user_accessible(username, password)
            for project in projects:
                pr_list.append(Project(name=project.name))
            return pr_list
        except WebFault:
            return None

