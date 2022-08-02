from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        add_button.click()
        self.solve_quiz_and_get_code()

# The shellcoder's handbook has been added to your basket.
# {} has been added to your basket.
# div.alert-success
# The shellcoder's handbook <strong>
# has been added to your basket.

# Your basket total is now £9.99
# Your basket total is now £{}
# div.alert-info
# Your basket total is now
# £9.99 <strong>


