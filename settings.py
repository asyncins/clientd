import sys
import logging


def logging_format(level):
    logger = logging.getLogger()
    logger.setLevel(level)
    fmt = logging.Formatter("%(asctime)s - %(message)s")
    sh = logging.StreamHandler(stream=sys.stdout)    # output to standard output
    sh.setFormatter(fmt)
    logger.addHandler(sh)
