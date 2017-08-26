from getgauge.python import step, DataStoreFactory

from step_impl.pages.page_factory import PageFactory


@step('User <user_name> is successfully logged in')
def user_is_successfully_logged(user_name):
    PageFactory.reservation_page.validate_reservation_page()
    