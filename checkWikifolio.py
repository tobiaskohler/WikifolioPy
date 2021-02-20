from logger import logger, CPrint
import requests
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup
import re
import json
from datetime import datetime
from pathlib import Path
#import databaseHandling

class CheckWikifolio():
    '''Class to be instantiated to check current account balance'''

    def __init__(self, session, symbol):
       
        self.session = session
        self.todays_date = datetime.now().strftime('%Y-%m-%d')
        self.filename = Path(f'daily_trades/{self.todays_date}')
        Path('daily_trades').mkdir(parents=True, exist_ok=True)
        self.symbol = symbol
        self.url = f'https://www.wikifolio.com/api/wikifolio/{symbol}/portfolio'
        self.item_url = f'https://www.wikifolio.com/api/wikifolio/{symbol}/portfolio?country=de&language=de'


    def check_balance(self):
        '''returns a dictionary "values", containing both the total Portfolio Amount and the free available cash amount'''
        
        m1_start = f'Checking Account balance for {self.url} ...'
        CPrint.color('n', m1_start)
        logger.info(m1_start)

        try:
            
            r = self.session.get(self.url).text
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
            CPrint.color('r', e)
            logger.info(f'Error: {e}')

    def get_items(self):
        '''returns a dictionary containing all portfolio items (ISIN: QUANTITY)''' 

        m1_start = f'Scanning current Portfolio items for {self.url}...'
        CPrint.color('n', m1_start)
        logger.info(m1_start)

        try:

            r = self.session.get(self.item_url).text
            soup = BeautifulSoup(r, 'lxml-xml')
            soupString = str(soup.encode('ascii'))
            
            blob = re.split('[< >]', soupString)
            blob_len = len(blob)
            i = 0

            isin_list = []
            quan_list = []
            
            for index, elem in enumerate(blob):
                if elem == 'Isin':
                    isin_list.append(blob[index+1])

            for index, elem in enumerate(blob):
                if elem == '/WikifolioDetailPortfolioItemModel':
                    quantity = blob[index-3].strip()
                    quantity = float(quantity)
                    quan_list.append(quantity)

            portfolio_items = dict(zip(isin_list, quan_list))

            m1_success = f'Successfully retrieved all Portfolio Items: Items \n {portfolio_items}'
            CPrint.color('g', m1_success)
            logger.info(m1_success)

            return portfolio_items



            
        except Exception as e:
            CPrint.color('r', e)
            logger.info(f'Error: {e}')

if __name__ == "__main__":
    symbol = 'WF50060055'
    from activateSession import SessionActivator
    from credentials import credentials
    cre = credentials()
    sessionActivator = SessionActivator(cre)
    returnValue = sessionActivator.activateSession()

    session = returnValue['session']

    CPrint.color('i', "Testing module checkAccountBalance...")
    accountBalanceChecker = CheckAccountBalance(session, symbol) 
    accountBalanceChecker.check_balance() 
    accountBalanceChecker.get_items()
    CPrint.color('i', "Finished testing checkAccountBalance!")

