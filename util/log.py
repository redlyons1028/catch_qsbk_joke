# -*- coding: utf-8 -*-

import logging
from logging import handlers


class Logger(object):
    # 日志等级
    level_relations = {
        'debug': logging.DEBUG,
        'info': logging.INFO,
        'warning': logging.WARNING,
        'error': logging.ERROR,
        'crit': logging.CRITICAL
    }

    # 日志输出格式
    fmt = '%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'

    def __init__(self,
                 filename,
                 level='info',
                 when='D',
                 backCount=3):
        self.logger = logging.getLogger(filename)
        format_str = logging.Formatter(self.fmt)
        self.logger.setLevel(self.level_relations.get(level))
        # 终端输出日志
        sh = logging.StreamHandler()
        sh.setFormatter(format_str)
        # 日志写入文件
        th = handlers.TimedRotatingFileHandler(filename=filename,
                                               when=when,
                                               backupCount=backCount,
                                               encoding='utf-8')
        th.setFormatter(format_str)
        self.logger.addHandler(sh)
        self.logger.addHandler(th)


if __name__ == '__main__':
    log = Logger('all.log', level='debug')
    log.logger.debug('debug')
    log.logger.info('info')
    log.logger.warning('warning')
    log.logger.error('error')
    log.logger.critical('critical')
