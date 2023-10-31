import logging
from logging.handlers import SysLogHandler

PAPERTRAIL_HOST = 'logs.papertrailapp.com' # logging account
PAPERTRAIL_PORT = 37554 #port for logging my logs

def main() -> None:
    logger =  logging.getLogger('bumho')
    logger.setLevel(logging.DEBUG)
    handler = SysLogHandler(address=(PAPERTRAIL_HOST,PAPERTRAIL_PORT))
    logger.addHandler(handler)

    logger.debug('This is a debug message.')



if __name__ == '__main__':
    main()
