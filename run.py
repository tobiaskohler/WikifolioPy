from activateSession import SessionActivator
from controlBrowser import BrowserController








if __name__ == '__main__':
    s = SessionActivator()
    s.activateSession()
    b = BrowserController()
    b.login()
    b.logout()
