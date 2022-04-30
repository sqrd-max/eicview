import logging

logging.basicConfig(level=logging.DEBUG)
logging.warning('Watch out!')  # will print a message to the console
logging.info('I told you so')

logger = logging.getLogger("haha")
logger.warning("Haha")
logger.info("hyhy")