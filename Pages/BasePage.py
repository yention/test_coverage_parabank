from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


from Pages.Page import Page


class BasePage(Page):

    LOGO_ICON = (By.CSS_SELECTOR, 'img.logo')

    def __init__(self, driver):
        super(BasePage, self).__init__(driver)
        self.driver = driver
        self.url = str()

    def go_to_page(self):
        self.driver.get(self.url)

    def is_visible(self):
        condition = self.wait.untill(EC.visibility_of_element_located(self))
        return bool(condition)

    def is_clickable(self):
        condition = self.wait.untill(EC.element_to_be_clickable(self))
        return bool(condition)

