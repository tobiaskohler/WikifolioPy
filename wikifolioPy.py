
#WikifolioPy imports all submodules and calls them within its own methods. This is to allow a more conventient use of the bot.
from credentials import credentials
from activateSession import SessionActivator
from controlBrowser import BrowserController
from checkAccountBalance import CheckAccountBalance


class WikifolioPy:
    '''Main class to be instantiated from, all modules are bundled into that class.

    Subsequent methods are implemented and provided by the <modules>:

    login, logout <controlBrowser.py>

    get_cash_amount <checkAccountBalance.py>

    ....


    '''

    def __init__(self, symbol):
        self.symbol = symbol 
        self.credentials = credentials()
        self.browserController = BrowserController(self.credentials)
        self.checkAccountBalance = CheckAccountBalance(self.symbol)
        self.s = SessionActivator(self.credentials).activateSession()
        self.session = self.s['session']
        self.connectionToken = self.s['connectionToken']

    def login(self):
        self.browserController.login()

    def logout(self):
        self.browserController.logout()

    def get_portfolio_items(self):
        return None

    def get_cash_amount(self):
        self.checkAccountBalance.check_balance(self.session) 

    def enter_order(self):
        return None
