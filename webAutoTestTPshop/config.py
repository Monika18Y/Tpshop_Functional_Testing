"""
配置文件
"""
import os
import logging.handlers

BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # 返回当前文件所在文件夹的绝对路径（当前文件是配置文件）
print(BASE_DIR)


def config_log():
    logger = logging.getLogger()  # 实例化日志器
    logger.setLevel(level=logging.WARNING)  # 设置日志输出级别---
    sh = logging.StreamHandler()  # 实例化处理器--到控制台
    th = logging.handlers.TimedRotatingFileHandler(filename=BASE_DIR + '/log/info.log',
                                                   when='S',
                                                   interval=5,
                                                   backupCount=4)  # 到文件
    fmt = '%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s'
    formatter = logging.Formatter(fmt)
    # 将格式器添加到处理器
    sh.setFormatter(formatter)
    th.setFormatter(formatter)
    # 将处理器添加到日志器
    logger.addHandler(sh)
    logger.addHandler(th)
