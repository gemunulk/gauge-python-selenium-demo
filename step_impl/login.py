from getgauge.python import step, DataStoreFactory

from step_impl.pages.page_factory import PageFactory


@step('On Login Page')
def navigate_to_login_page():
    PageFactory.login_page.visit()
    
@step('Login as <user_name> using <password>')
def login_as(user_name, password):
    PageFactory.login_page.login(user_name, password)

    