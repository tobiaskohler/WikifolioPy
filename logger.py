import logging
import pathlib
from datetime import datetime

class CPrint:

    now = datetime.now()
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")
    
    info = '\033[95m'
    green = '\033[92m'
    red = '\033[91m'
    end = '\033[0m'
    normal = '\033[0;30;47m'

    def color(color, string):
        string = str(string)
        if color == 'g':
            print(f'{CPrint.current_time} {CPrint.green}' + string + f'{CPrint.end}')
        elif color == 'r':
            print(f'{CPrint.current_time} {CPrint.red}' + string + f'{CPrint.end}')
        elif color == 'i':
            print(f'{CPrint.current_time} {CPrint.info}' + string + f'{CPrint.end}')
        elif color == 'n':
            print(f'{CPrint.current_time} {CPrint.normal}' + string + f'{CPrint.end}')
        else:
            print(string)

# create logs folder
pathlib.Path('logs').mkdir(parents=True, exist_ok=True) 

today = datetime.now().strftime('%Y-%m-%d')
filename = f'logs/{today}.log'

logging.basicConfig(filename=filename, filemode='a', format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s', datefmt='%H:%M:%S', level=logging.DEBUG)

# create logger
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
