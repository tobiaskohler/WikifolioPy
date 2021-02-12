#This module logs into wikifolio.com and  retrieves an active requests.session. The session object allows you to persist certain parameters across requests (like e.g. the connectionToken, if a websocket connection shall be established). It also persists cookies across all requests. 

import requests
from bs4 import BeautifulSoup
from credentials import credentials
from logger import logger, CPrint 


class SessionActivator():
    '''Class to be instantiated to have an active wikifolio session enabled'''

    def __init__(self):

        cre = credentials()
        self.usr = cre['USR']
        self.pwd = cre['PWD']
        self.s = requests.Session()
        self.loginUrl = 'https://www.wikifolio.com/dynamic/de/de/login/login/'
        self.headers = {'useragent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.16; rv:83.0) Gecko/20100101 Firefox/83.0'}
        self.login_url = self.s.get(url='https://www.wikifolio.com/dynamic/de/de/login/login').content
        self.soup_login = BeautifulSoup(self.login_url, 'html.parser')


    def activateSession(self):

        #### FRAGILE PARAMETER; MIGHT CHANGE DUE TO AMENDMENTS WITHIN EXTERNAL PROD CODE ####
        request_verification_token = self.soup_login.select_one('input[name="__RequestVerificationToken"]')['value']
        ufprt = self.soup_login.select_one('input[name="ufprt"]')['value']

        payload = {
        'Username': self.usr, 
        'Password': self.pwd, 
        '__RequestVerificationToken': request_verification_token, 
        'ufprt': ufprt
        }

        logger.info(f"Successfully identified all relevant parameters: {payload['__RequestVerificationToken']}, {payload['ufprt']}")
        self.s.post(self.loginUrl, headers=self.headers, data=payload)
        successMsg = 'Login successfull!'
        CPrint.color('g', successMsg)
        logger.info(successMsg)

        ##ConnectionToken only necessary for Websockets:
        connectionTokenUrl='https://www.wikifolio.com/de/de/signalr/negotiate'
        connectionTokenContext = self.s.get(connectionTokenUrl, headers=self.headers).text
        connectionTokenRaw = connectionTokenContext.split(":")
        connectionToken = str(connectionTokenRaw[2].split(",")[0].strip())
        connectionTokenMsg = f'Successfully identified the connection Token: {connectionToken}' 

        CPrint.color('g', connectionTokenMsg)
        logger.info(connectionTokenMsg)


        returnValue = {
            'session': self.s,
            'connectionToken': connectionToken
        }

        return returnValue

if __name__ == "__main__":
    CPrint.color('i', "Testing module activateSession...")
    sessionActivator = SessionActivator()
    sessionActivator.activateSession()
    CPrint.color('i', "Finished testing!")
