from selenium import webdriver
from fixture.session import SessionHelper
from fixture.project import ProjectHelper
from fixture.james import JamesHelper
from fixture.signup import SignupHelper
from fixture.mail import MailHelper
from fixture.soap import SoapHelper

class Application:

    def __init__(self, browser, config):
        browser_upper = browser.upper()
        if browser_upper == "FIREFOX":
            self.wd = webdriver.Firefox()
        elif browser_upper == "CHROME":
            self.wd = webdriver.Chrome()
        elif browser_upper == "IE":
            self.wd = webdriver.Ie()
        else:
            raise ValueError("Unrecognized browser %s" % browser)
        self.wd.implicitly_wait(1)
        self.session = SessionHelper(self)
        self.project = ProjectHelper(self)
        self.james = JamesHelper(self)
        self.signup = SignupHelper(self)
        self.mail = MailHelper(self)
        self.soap = SoapHelper(self)
        self.config = config
        self.base_url = config['web']['baseUrl']

    def open_home_page(self):
        wd = self.wd
        wd.get(self.base_url)

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def destroy(self):
        wd = self.wd
        wd.quit()
