"""配置文件"""
import sys
import logging


def logging_format(level):
    # 设置日志级别和格式
    logger = logging.getLogger()
    logger.setLevel(level)
    fmt = logging.Formatter("%(asctime)s - %(message)s")
    sh = logging.StreamHandler(stream=sys.stdout)    # output to standard output
    sh.setFormatter(fmt)
    logger.addHandler(sh)
