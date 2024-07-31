from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys 
import time, math


class Locators():
    WEIGH_BUTTON = (By.CSS_SELECTOR, "#weigh")
    RESET_BUTTON = (By.CSS_SELECTOR, "button.button:nth-child(1)")
    RESULT_INFO = (By.CSS_SELECTOR, '.result > button:nth-child(2)')
    GOLD_BUTTON_ARRAY = (By.CSS_SELECTOR,".coins")
    LEFT_GRID = (By.CSS_SELECTOR,'#left_0')
    RIGHT_GRID = (By.CSS_SELECTOR,'#right_0')
    WEIGHINGS_INFO = (By.CSS_SELECTOR,'.game-info > ol:nth-child(2)')
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
    
    #Not sure wait for presences of locators are necessary 
    #since the app is reactjs so the elements are already loaded, but going to include them for good practice
    def click_weigh_button(self):
        self.wait_for(Locators.WEIGH_BUTTON)
        element = self.driver.find_element(*Locators.WEIGH_BUTTON).click()
        #using sleep to wait for the page to load the weigh button press as there is some delay
        #for results to propagate
        print('Log: Clicked Weigh Button, Waiting 4s')
        time.sleep(4)

    def click_reset_button(self):
        self.wait_for(Locators.RESET_BUTTON)
        element = self.driver.find_element(*Locators.RESET_BUTTON).click()
        print('Log: Clicked Reset Button')
        

    def click_goldbar(self,number):
        gold_id = 'coin_'+ str(number)
        element = self.driver.find_element(By.ID, gold_id).click()
        
        alert = self.wait.until(EC.alert_is_present())
        print("Log: The alert says: " + alert.text)
        alert.accept()
    
    def get_result(self):
        self.wait_for(Locators.RESULT_INFO)
        element = self.driver.find_element(*Locators.RESULT_INFO)
        return element.text
    
    """Returns a list of weighings currently on the page"""
    def get_weighings(self):
        time.sleep(2)
        element = self.driver.find_element(*Locators.WEIGHINGS_INFO)
        list_weighings = element.find_elements(By.TAG_NAME, 'li')
        
        weighings = []
        for weighing in list_weighings:
            weighings.append(weighing.text)

        return weighings
        
    
    """Finds the length of list of gold bars incase it changes."""
    def get_array_length(self):
        element = self.driver.find_element(*Locators.GOLD_BUTTON_ARRAY)
        buttons_in_div = element.find_elements(By.TAG_NAME, 'button')
        return len(buttons_in_div)
    
    """Fills left or right grid with a range of numbers"""
    def fill_grid(self,side,range_start=None,range_end=None):
        range_start = int(range_start)
        range_end = int(range_end)
        if side =='left':

            self.driver.find_element(*Locators.LEFT_GRID).click()

        if side =='right':
            self.driver.find_element(*Locators.RIGHT_GRID).click()
       
        #print(f"Log: Filling {side} grid")
        actions = ActionChains(self.driver)
        for i in range(range_start,range_end):
            actions = actions.send_keys(i)
            actions = actions.send_keys(Keys.TAB)            
        actions.perform()

