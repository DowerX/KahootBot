from selenium import webdriver
from time import sleep

class Bot:
    def __init__(self):
        self.driver = webdriver.Chrome()

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
        self.driver.close()

    def vote(self, id):
        try:
            buttons = self.driver.find_elements_by_xpath('//*[@role="button"]')
            buttons[id].click()
        except:
            print(f"Tried to vote for No. {id} but there only were {len(buttons)} options. Error")