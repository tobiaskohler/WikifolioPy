#Simple config file. Put your USR and PWD into environment variables named WIKIFOLIO_USR and WIKIFOLIO_PWD
#Returns a dictionary with credentials
from logger import logger, CPrint
import os

def credentials():
    #Please set your WIKIFOLIO username (email) and password via environment variables (<export WIKI_USR='test@test.com'> and <export WIKIFOLIO_PWD='foobar'>)

    USR = os.getenv('WIKIFOLIO_USR')
    PWD = os.getenv('WIKIFOLIO_PWD')
    
    if USR==None and PWD==None:
        USR: str = input('Please provide your Wikifolio email address: ')
        PWD: str = input('Please provide your Wikifolio password: ')

    cre = {'USR': USR, 'PWD': PWD} 
    credentialMsg = f'Your Wikifolio email is set to: {USR}, your password to: {PWD}'
    CPrint.color('g', credentialMsg) 
    return cre

if __name__ == '__main__':
    CPrint.color('i', 'Testing module credentials...')
    credentials()
    CPrint.color('i', 'Finished testing!')
