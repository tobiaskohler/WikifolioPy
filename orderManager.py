
from activateSession import activateSession
from logger import logger
from bs4 import BeautifulSoup
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException


class OrderManager():

    def __init__(self, session):
        self.session = session



    def enterMarket(isin, ordertype, quantity):

        return None


    def enterLimit(isin, ordertype, quantity, limit):

        return None

