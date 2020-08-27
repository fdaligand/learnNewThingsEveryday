import datetime
import logging
from logging.handlers import RotatingFileHandler
import sys

logging.debug('This is a debug message')
logging.info('This is a info message')
logging.warning('This is a warning message')
# default level is warning

debug_logger = logging.getLogger('debug_logger')
debug_logger.setLevel(logging.DEBUG)
debug_logger.debug('This is a debug message')
# now debug is printed

# create a handler that only show message up to INFO
# default stream is sys.stderr
handler_logger = logging.getLogger('handler_logger')
handler_logger.setLevel(logging.DEBUG)
handler_logger.propagate = False # do not propagate message out of the handler
handler = logging.StreamHandler(stream=sys.stderr)
handler.setLevel(logging.INFO)

handler_logger.addHandler(handler)

handler_logger.debug('This is a debug message not see through handler')
handler_logger.info('This is a info message see through handler')
handler_logger.warning('This is a warning message see through handler')

# log to a file (rotating)
rotating_logger = logging.getLogger("rotating_logger")
rotating_logger.setLevel(logging.DEBUG)

rotating_handler = RotatingFileHandler('rotating.log', mode='a', maxBytes=200, backupCount=2)
formatter = logging.Formatter(fmt="{asctime} : {message}", style="{", ) # use str.format() style !
rotating_handler.setFormatter(formatter)
rotating_logger.addHandler(rotating_handler)
rotating_logger.debug("write a debug message to file")


# customize log_record
# add custom argument in formatter

old_factory = logging.getLogRecordFactory()
def record_factory(*args, **kwargs):
    record = old_factory(*args, **kwargs)
    record.custom_args = "plop"
    record.today = datetime.datetime.today()
    return record


logging.setLogRecordFactory(record_factory)

custom_log_record_logger = logging.getLogger('custom_logrecord')
custom_log_record_logger.setLevel(logging.DEBUG)
custom_handler = logging.StreamHandler(stream=sys.stderr)
custom_formatter = logging.Formatter(fmt="{asctime} || {custom_args} {today} : {message}", style="{", ) # use str.format() style !
custom_handler.setFormatter(custom_formatter)
custom_log_record_logger.addHandler(custom_handler)
custom_log_record_logger.debug("try to log a custom arg")

# TODO : continue reading on
# https://docs.python.org/3/howto/logging-cookbook.html#adding-contextual-information-to-your-logging-output
