# this code demonstrate how to add contextual information to the log
# either a fix context or a dynamic context

import logging
from pythonjsonlogger import jsonlogger
# call to basicConfig set default handler and formatter
import sys

logging.basicConfig(level=logging.DEBUG, style='{')
json_formatter = jsonlogger.JsonFormatter()
json_handler = logging.StreamHandler()
json_handler.setFormatter(json_formatter)

class IpAdapter(logging.LoggerAdapter):
    """"Add ip address to the log message and to extra info"""

    def process(self, msg, kwargs):
        kwargs['extra'] = {'IP': self.extra['IP']}
        return "IP:%s %s" % (self.extra['IP'], msg), kwargs


def print_some_message(logger):

    logger.debug('this is a debug message')
    logger.debug('this is a debug message with params %s %s', 'param1', 'param2')
    logger.debug('this is a debug message with different ip', extra={'IP':'5.6.7.8'})
    logger.error('this is an error message')



if __name__ == '__main__':

    logger_with_extra = logging.getLogger('logger_with_extra')
    logger_with_extra.propagate = False # don't trace info with other formatter

    # log extra info
    handler = logging.StreamHandler(stream=sys.stderr)
    ip_formatter = logging.Formatter("%(levelname)s:%(name)s:IP=%(IP)s:%(message)s'")
    handler.setFormatter(ip_formatter)
    logger_with_extra.addHandler(handler)
    logger_with_extra.addHandler(json_handler)
    logger_with_extra.debug('log debug with extra info', extra={'IP': '1.2.3.4'})
    # if you set your key to None, it is not logged
    logger_with_extra.debug('Log with None value', extra={'IP':None})
    # if you omit extra, it assert an error but continue
    logger_with_extra.debug('omit extra dict when logging raise error', extra={'plop': 0})

    # add contextual info to all message
    # without need to pass it for each logging calls
    logger = logging.getLogger('logger_with_adapter')
    logger.addHandler(json_handler)
    adapter = IpAdapter(logger, {'IP': '127.0.0.1'})
    print_some_message(adapter)