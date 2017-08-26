from getgauge.python import step, DataStoreFactory

from step_impl.pages.page_factory import PageFactory

@step('Logout from the application')
def logout_from_the_application():
    PageFactory.logout_page.visit()
    
    