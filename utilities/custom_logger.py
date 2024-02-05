import inspect
import logging
import os


def customLogger(logLevel=logging.DEBUG):
    # Gets the name of the class / method from where this method is called
    loggerName = inspect.stack()[1][3]
    logger = logging.getLogger(loggerName)

    # By default, log all messages
    logger.setLevel(logging.DEBUG)

    # Specify the path to the 'logs' folder one level back from the current script
    log_folder_path = os.path.join(os.path.dirname(__file__), '..', 'logs')
    os.makedirs(log_folder_path, exist_ok=True)

    fileHandler = logging.FileHandler(os.path.join(log_folder_path, 'automation.log'), mode='a')
    # fileHandler = logging.FileHandler("automation.log", mode='a')
    fileHandler.setLevel(logLevel)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)

    return logger