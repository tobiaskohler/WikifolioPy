from logger import logger, CPrint
from wikifolioPy import WikifolioPy

if __name__ == '__main__':
    '''Only relevant parameter is the symbol of the  wikifolio'''
    
    symbol = 'WF0GLDIVST'
   

    CPrint.color('i', 'Starting WikifolioPy...')
    w = WikifolioPy(symbol)
    w.login()
    w.logout()
    w.get_cash_amount()
    CPrint.color('i', 'Finished!')
