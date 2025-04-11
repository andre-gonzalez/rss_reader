import logging
import os

def setup_logging():
    log_level = logging.DEBUG

    if not os.path.exists('logs'):
        os.makedirs('logs')

    log_file = 'logs/app.log'

    logger = logging.getLogger()
    logger.setLevel(log_level)

    if not logger.hasHandlers():
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(log_level)

        console_handler = logging.StreamHandler()
        console_handler.setLevel(log_level)

        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')


        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logger
