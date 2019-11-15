from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep

class Bot:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        prefs = {"profile.managed_default_content_settings.images": 2}
        chrome_options.add_experimental_option("prefs", prefs)
        chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(chrome_options=chrome_options)

    def login(self, pin, name):
        self.driver.get("https://kahoot.it/")
        pinBox = self.driver.find_element_by_id("game-input")
        pinBox.send_keys(pin)
        enterButton = self.driver.find_element_by_xpath('//*[@value="Submit"]')
        enterButton.click()
        sleep(2)
        nameBox = self.driver.find_element_by_id("nickname")
        nameBox.send_keys(name)
        enterButton = self.driver.find_element_by_xpath('//*[@value="Submit"]')
        enterButton.click()

    def quit(self):
        #self.driver.close()
        self.driver.quit()

    def vote(self, id):
        try:
            buttons = self.driver.find_elements_by_xpath('//*[@role="button"]')
            buttons[id].click()
        except:
            print(f"Tried to vote for No. {id} but there only were {len(buttons)} options. Error")