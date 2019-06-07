"""Application logging."""

import logging
import sys


def setup_custom_logger(name):
    """Set up for app logging."""
    formatter = logging.Formatter(fmt='%(asctime)s %(levelname)-8s \
                                  %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    handler = logging.FileHandler('stouchator.log', mode='w')
    handler.setFormatter(formatter)
    screen_handler = logging.StreamHandler(stream=sys.stdout)
    screen_handler.setFormatter(formatter)
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(handler)
    logger.addHandler(screen_handler)
    return logger
