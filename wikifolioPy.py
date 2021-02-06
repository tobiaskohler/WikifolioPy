#Main module
#WikifolioPy imports all submodules and calls them within its own methods. This is to allow a more conventient use of the bot.

from activateSession import SessionActivator
from controlBrowser import BrowserController



class WikifolioPy:

    def __init__(self, url):
        self.url = url
        self.sessionActivator = SessionActivator()
        self.browserController = BrowserController()

    def login(self):
        self.browserController.login()

    def logout(self):
        self.browserController.logout()

    def getPortfolioItems(self):
        return None

    def getPortfolioValue(self):
        return None

    def enterOrder(self):
        return None
