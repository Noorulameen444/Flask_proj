import logging
import os
from datetime import datetime

def create_dir():
    '''
    Creates a Logs directory(if not present) and creates a sub directory
    with current date as it's name and returns the directory path.
    '''

    date = datetime.now().date()
    date = str(date)
    PD = os.path.abspath('.')
    LOG_DIR_NAME = 'Logs'
    LOG_DIR_PATH = os.path.join(PD,LOG_DIR_NAME)

    try:
        os.mkdir(LOG_DIR_PATH)
    except:
        pass

    LOGS_PATH = os.path.join(LOG_DIR_PATH,date)

    try:
        os.mkdir(LOGS_PATH)
    except:
        pass

    return LOGS_PATH


def generate_file_name(filename,filepath):
    '''
    Generates the file name of the log file based on the name of the file in which it is run
    and returns the orginal file's name with extension and the filepath of the log file.
    '''
    
    org_name = os.path.basename(filename)
    name = os.path.splitext(org_name)[0]
    file_path = os.path.join(filepath,name) #previously filename
    return (org_name,file_path)


def custom_log_obj(*args):
    '''
    Creates a custom logging object and returns it.
    '''

    name_obj = args[0]
    org_name = name_obj[0]
    file_path = name_obj[1]
    
    logger = logging.getLogger(org_name)
    logger.setLevel(logging.INFO)

    handler = logging.FileHandler(f'{file_path}.log')
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    handler.setFormatter(formatter)
    logger.addHandler(handler)

    return logger


def custom_logger(current_filename):
    '''Creates a custom logging object and creates a custom sub directory and
    custom log file in Logs directory. 
    '''

    filepath = create_dir()
    name_list = generate_file_name(current_filename,filepath)
    log_obj = custom_log_obj(name_list)

    return log_obj
