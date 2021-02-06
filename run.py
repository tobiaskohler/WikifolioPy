from wikifolioPy import WikifolioPy

if __name__ == '__main__':
    '''Only relevant parameter is the url to wikifolio'''
    
    url = 'DummyURL'
    
    w = WikifolioPy(url)
    w.login()
    w.logout()
