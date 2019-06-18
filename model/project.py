from sys import maxsize


class Project:

    def __init__(self, name=None, status=None, inherit=None, viewstate=None, description=None):
        self.name = name
        self.status = status
        self.inherit = inherit
        self.viewstate = viewstate
        self.description = description

    def __repr__(self):
        return "%s" % self.name

    def __eq__(self, other):
        return self.name is None or other.name is None or self.name == other.name

