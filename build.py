import os
import sys
import logging
from pathlib import Path
from pathlib import PurePath
import subprocess
from os.path import join

from settings import *


SETUP_TEMPLATE = """from setuptools import setup, find_packages
setup(name='%(project)s', version='%(version)s', packages=find_packages())
"""


def builder(name, target_space):
    """ 用setuptools打包 """
    os.chdir(target_space)  # 切换工作路径
    generate_setup(target_space, project=name, version='1.5')
    # 在目标路径执行打包命令
    execute = subprocess.run([sys.executable, 'setup.py', 'bdist_egg', '-d', target_space],
                   stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if not execute.returncode:
        logging.info('Project [%s] was build.The egg in [%s]' % (name, target_space))
    else:
        logging.warning('subprocess return code not is %s!' % execute.returncode)


def generate_setup(path, **kwargs):
    """生成setup.py文件，并写入基础配置"""
    with open(join(path, 'setup.py'), 'w', encoding='utf-8') as f:
        file = SETUP_TEMPLATE % kwargs
        f.write(file)


if __name__ == '__main__':
    logging_format(logging.INFO)  # 设置日志格式
    space = PurePath.joinpath(Path.cwd(), 'project')  # 目标路径
    builder('hello', space)  # 执行打包
