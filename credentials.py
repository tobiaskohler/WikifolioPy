#Simple config file. Put your USR and PWD into environment variables named WIKIFOLIO_USR and WIKIFOLIO_PWD
#Returns a dictionary with credentials

import os

def credentials():
    #Please set your WIKIFOLIO username (email) and password via environment variables (<export WIKI_USR='test@test.com'> and <export WIKIFOLIO_PWD='foobar'>)

    USR = os.getenv('WIKIFOLIO_USR')
    PWD = os.getenv('WIKIFOLIO_PWD')

    #URL to your wikifolio
    WIKI = 'url'


    credentials = {'USR': USR, 'PWD': PWD, 'WIKI': WIKI} 
    return credentials

if __name__ == 'main':
    credentials()
