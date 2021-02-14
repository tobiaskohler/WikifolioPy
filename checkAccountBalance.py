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
        self.url = f'https://www.wikifolio.com/api/wikifolio/{symbol}/portfolio'


    def check_balance(self, session):
        
        m1_start = f'Checking Account balance for {self.url} ...'
        CPrint.color('n', m1_start)
        logger.info(m1_start)

        try:
            
            r = session.get(self.url).text
            content = BeautifulSoup(r,'xml')

            #find Portfolio's Total Value (typically last Element of XML tree)
            totalValue = str(content.findAll('TotalValue'))
            x = totalValue.split('>')[-2:][0].split("<")[0]
            totalValueFloat = float(x)

            #find Portfolios free available Cash (last element before Total Value)
            cashValue = str(content.findAll('Value')[-1])
            y = cashValue.split('>')[-2:][0].split("<")[0]
            totalValueCashFloat = float(y)

            datum = datetime.today().astimezone()

            values = {}
            values['total'] = totalValueFloat 
            values['cash'] = totalValueCashFloat 

            #databaseHandling.appendTableWithPortfolioValue([[datum], [amount]])

            totalValueFloatText = f'Total portfolio value: {totalValueFloat} EUR.'
            logger.info(totalValueFloatText)
            CPrint.color('g', totalValueFloatText)

            totalValueCashFloatText = f'Free cash amount: {totalValueCashFloat} EUR.'
            logger.info(totalValueCashFloatText)
            CPrint.color('g', totalValueCashFloatText)

            return values


        except Exception as e:
            print(f'Fehler: {e}')
            logger.info(f'Fehler: {e}')



if __name__ == "__main__":
    symbol = 'WFNEBENWEU'
    from activateSession import SessionActivator
    from credentials import credentials
    cre = credentials()
    sessionActivator = SessionActivator(cre)
    returnValue = sessionActivator.activateSession()

    session = returnValue['session']

    CPrint.color('i', "Testing module checkAccountBalance...")
    accountBalanceChecker = CheckAccountBalance(symbol) 
    accountBalanceChecker.check_balance(session) 
    CPrint.color('i', "Finished testing checkAccountBalance!")

