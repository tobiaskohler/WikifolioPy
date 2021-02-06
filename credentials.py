#Simple config file. Put your USR and PWD into environment variables named WIKIFOLIO_USR and WIKIFOLIO_PWD
#Returns a dictionary with credentials

import os

def credentials():
    USR = os.getenv('WIKIFOLIO_USR')
    PWD = os.getenv('WIKIFOLIO_PWD')

    credentials = {'USR': USR, 'PWD': PWD} 
 
    return credentials

if __name__ == 'main':
    credentials()
