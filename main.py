#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lib.HTMLTestRunner import HTMLTestRunner
import sys
import unittest
import time
import logging
from lib.Pil import Pil
from lib.Logger import Logger
from testcase.login import BugfreeLogin1

def fun_suite():
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    suite.addTests(loader.loadTestsFromTestCase(BugfreeLogin1))
    return suite

if __name__ == "__main__":
    #unittest.main()
    logger = Logger().getlog()
    logger.info('start testcase...')
    fp=open('./result_%s.html' % time.strftime("%Y-%m-%d %H-%M-%S"), 'wb')
    runner=HTMLTestRunner(stream=fp,
                          title=u'我们仨首次生成的测试报告',
                          description=u'下面是本次测试执行结果哦~~')
    runner.run(fun_suite())
    Pil()
    fp.close()
    sys.exit(0)
    logger.info('stop testcase...')