import logging

#logging.basicConfig(level=logging.INFO, filename='example.log', filemode='w')
logging.basicConfig(level=logging.DEBUG, filename='example.log', format='%(asctime)s %(levelname)s:%(message)s',
	datefmt='%m/%d/%Y %I:%M:%S %p')

logging.debug('This message will be ignored.')
logging.info('This should be logged.')
logging.warning('And this, too')