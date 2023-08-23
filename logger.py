import logging
import os

CWD = os.getcwd()
LOG_DIR = 'Logs'
LOG_DIR_PATH = os.path.join(CWD,LOG_DIR)

def Log(filepath):
    '''creates a custom logger object'''
    try:
        os.mkdir(LOG_DIR_PATH)
    except:
        pass

    name = os.path.basename(filepath)
    name = os.path.splitext(name)[0]
    filename = os.path.join(LOG_DIR_PATH,name)

    global logger
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    handler = logging.FileHandler(f'{filename}.log')
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    handler.setFormatter(formatter)
    logger.addHandler(handler)

    return logger