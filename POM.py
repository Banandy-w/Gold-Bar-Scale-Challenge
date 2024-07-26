from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class Locators():
    WEIGH_BUTTON = (By.CSS_SELECTOR, "#weigh")
    RESET_BUTTON = (By.CSS_SELECTOR, "button.button:nth-child(1)")
    RESULT_INFO = (By.CSS_SELECTOR, '.result > button:nth-child(2)')
    ARRAY = (By.CSS_SELECTOR,".coins")

class BasePage():        
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    """Returns True if an elment is visible"""
    def is_visible(self, by_locator):
        element = self.wait.until(EC.visibility_of_element_located(by_locator))
        return bool(element)
    
    """Opens URL"""
    def open_page(self, URL):
        self.driver.get(URL)

    """Waits for page to load a certain element"""
    def wait_for(self,by_locator):
        self.wait.until(EC.presence_of_element_located(by_locator))

class BalancePage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)
    
    def click_weigh_button(self):
        element = self.driver.find_element(*Locators.WEIGH_BUTTON)
        element.click()

    def click_reset_button(self):
        element = self.driver.find_element(*Locators.RESET_BUTTON)
        element.click()

    def get_result(self):
        element = self.driver.find_element(*Locators.RESULT_INFO)
        return element.text
    
    """Finds the length of list of gold bars incase it changes."""
    def get_array_length(self):
        element = self.driver.find_element(By.CSS_SELECTOR,'.coins')
        buttons_in_div = element.find_elements(By.TAG_NAME, 'button')
        return len(buttons_in_div)