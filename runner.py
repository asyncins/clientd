import importlib

from pathlib import Path
from pathlib import PurePath

from settings import *


def execute(egg, project):
    """将egg路径添加到sys.path，然后导入该包"""
    sys.path.insert(0, str(egg))
    project = importlib.import_module(project)
    # 执行hello项目中的run方法
    project.run()


if __name__ == '__main__':
    logging_format(logging.INFO)  # 设置日志格式
    # egg包路径
    file = PurePath.joinpath(Path.cwd(), 'project', 'hello-1.5-py3.7.egg')
    execute(file, 'hello')
