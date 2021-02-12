from logger import logger, CPrint
import requests
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup
import re
import json
from datetime import datetime
from pathlib import Path
#import databaseHandling

class CheckAccountBalance():
    '''Class to be instantiated to check current account balance'''

    def __init__(self, symbol):
        
        self.todays_date = datetime.now().strftime('%Y-%m-%d')
        self.filename = Path(f'daily_trades/{self.todays_date}')
        Path('daily_trades').mkdir(parents=True, exist_ok=True)
        self.symbol = symbol
        self.url = 'https://www.wikifolio.com/api/wikifolio/{symbol}/portfolio'


    def check_balance(self, session):
        
        m1_start = "Checking Account balance..."
        CPrint.color('i', m1_start)
        logger.info(m1_start)

        try:

            r = session.get(self.url).text
            print(r)
            content = BeautifulSoup(r,'xml')
            print(content)
            tag = str(content.findAll('TotalValue'))
            print(tag)
            x = tag.split('>')[-2:][0].split("<")[0]
            print(x)
            amount = float(x)

            datum = datetime.today().astimezone()

            #databaseHandling.appendTableWithPortfolioValue([[datum], [amount]])

            messageText = f"Current available cash amount written to database"
            logger.info(messageText)
            CPrint.color('i', messageText)

            m1_end = f'Available Cash balance: {amount}' 
            CPrint.color('g', m1_end)
            logger.info(m1_end)


        except Exception as e:
            print(f'Fehler: {e}')
            logger.info(f'Fehler: {e}')



if __name__ == "__main__":
    symbol = 'wf0gldivst'
    from activateSession import SessionActivator
    sessionActivator = SessionActivator()
    returnValue = sessionActivator.activateSession()

    session = returnValue['session']




    CPrint.color('i', "Testing module checkAccountBalance...")
    accountBalanceChecker = CheckAccountBalance(symbol) 
    accountBalanceChecker.check_balance(session) 
    CPrint.color('i', "Finished testing checkAccountBalance!")
