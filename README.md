# clientd
2019/05/22 19：00 华为云直播《PYTHON 项目部署与调度核心逻辑》客户端案例。本项目实现了 PYTHON 打包和导包运行
的功能。

PYTHON 项目打包并不复杂，主要用到 setuptools 模块。
导包运行则涉及 PYTHON PATH 和 importlib 模块。

# 使用方法
项目打包：运行 build.py 文件即可将 project 目录中的 hello 项目打包成为 egg 包。

导包运行：运行 runner.py 文件即可执行 egg 包中的 run() 方法。


