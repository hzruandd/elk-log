import logging
import logging.handlers
from logging import Logger
from logging.handlers import TimedRotatingFileHandler

def init_logger(logger_name):
    if logger_name not in Logger.manager.loggerDict:
        logger = logging.getLogger(logger_name)
        logger.setLevel(logging.DEBUG)
        # handler all
        handler = TimedRotatingFileHandler('./all.log', when='midnight',backupCount=7)
        datefmt = '%Y-%m-%d %H:%M:%S'
        format_str = '[%(asctime)s]: %(name)s %(levelname)s %(lineno)s %(message)s'
        formatter = logging.Formatter(format_str, datefmt)
        handler.setFormatter(formatter)
        handler.setLevel(logging.INFO)
        logger.addHandler(handler)
        # handler error
        handler = TimedRotatingFileHandler('./error.log', when='midnight',backupCount=7)
        datefmt = '%Y-%m-%d %H:%M:%S'
        format_str = '[%(asctime)s]: %(name)s %(levelname)s %(lineno)s %(message)s'
        formatter = logging.Formatter(format_str, datefmt)
        handler.setFormatter(formatter)
        handler.setLevel(logging.ERROR)
        logger.addHandler(handler)

    logger = logging.getLogger(logger_name)
    return logger


def getlogger():
    handler = logging.handlers.RotatingFileHandler("delete.log",
                                                   maxBytes=10*1024*1024,
                                                   backupCount=5)
    fmt = '%(asctime)s-%(filename)s:%(lineno)s-%(name)s-%(message)s'

    formatter = logging.Formatter(fmt)
    handler.setFormatter(formatter)

    logger = logging.getLogger('HuaShi')
    logger.addHandler(handler)
    level = getattr(logging, "DEBUG")
    logger.setLevel(level)
    return logger

LOG = getlogger()

