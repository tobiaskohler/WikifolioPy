#This module operates the headless browsers (Firefox). Contains a lot of FRAGILE HTML references. Needs to be up to date with current, external code.

from logger import logger, CPrint
import time
from credentials import credentials
import random

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary


class BrowserController():

    def __init__(self):
        self.binary = FirefoxBinary('/Applications/Firefox.app/Contents/MacOS/firefox-bin')
        self.executablePath = '/usr/local/Cellar/geckodriver/0.28.0/bin/geckodriver'
        self.options = Options()
        self.options.headless = True 
        self.driver = webdriver.Firefox(executable_path=self.executablePath, firefox_binary=self.binary, options=self.options)
        self.actions = ActionChains(self.driver)

        self.credentials = credentials()
        initMsg = f"Initialized Browser (Geckodriver-Path: {self.executablePath}, given Wikifolio-User: {self.credentials['USR']})"
        logger.info(initMsg)
        CPrint.color('g', initMsg)

    def move_mouse_to_random_position(self,driver):

        try:
            max_x, max_y = self.driver.execute_script("return [window.innerWidth, window.innerHeight];")
            body = self.driver.find_element_by_tag_name("body")
            self.actions = ActionChains(self.driver)
            x = random.randint(0, max_x)
            y = random.randint(0, max_y)
            self.actions.move_to_element_with_offset(body, x, y)
            self.actions.perform()
            self.actions.reset_actions()

        except Exception as e:
            exceptionMsg = f'It seems like something went wrong. Probably the DOM elements have changed. Please check code.\n Full Exception message: {e}'
            logger.info(exceptionMsg)
            CPrint.color('r', exceptionMsg)


    def login(self):
        try:
            self.driver.get("https://www.wikifolio.com/")
            self.driver.maximize_window()

            self.move_mouse_to_random_position(self.driver)

            einverstandenButton = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.c-button--bold')))
            einverstandenButton.click()

            time.sleep(2)

            loginButton = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "html/body/div[3]/header/div/div/div/div[2]/button/span")))
            loginButton.click()

            usernameInput = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.ID, "Username")))
            usernameInput.send_keys(self.credentials['USR'])

            self.actions.send_keys(Keys.TAB)
            self.actions.send_keys(self.credentials['PWD'])
            self.actions.perform()
            self.actions.reset_actions()

            time.sleep(2)

            self.actions.send_keys(Keys.TAB)
            self.actions.send_keys(Keys.RETURN)
            self.actions.perform()
            self.actions.reset_actions()
            
            loginMsg = "Log in successful"
            logger.info(loginMsg)
            CPrint.color('g', loginMsg)

        except Exception as e:
            exceptionMsg = f'It seems like something went wrong. Probably the DOM elements have changed. Please check code.\n Full Exception message: {e}'
            logger.info(exceptionMsg)
            CPrint.color('r', exceptionMsg)

    def logout(self):
        try:
            time.sleep(5)

            self.driver.quit()

            logoutMsg = "Log out successful. Closed all headless Firefox browsers."
            logger.info(logoutMsg)
            CPrint.color('g', logoutMsg) 

        except Exception as e:
            exceptionMsg = f'It seems like something went wrong. Probably the DOM elements have changed. Please check code.\n Full Exception message: {e}'
            logger.info(exceptionMsg)
            CPrint.color('r', exceptionMsg)
    

if __name__ == "__main__":
    CPrint.color('i', "Testing module controlBrowser...")
    controlBrowser = BrowserController()
    controlBrowser.login()
    time.sleep(3)
    controlBrowser.logout()
    CPrint.color('i', "Finished testing controlBrowser!")
