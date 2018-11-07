# -*- coding: utf-8 -*-

import sys
import os
import shutil
from multiprocessing import Pool

from robot.run import RobotFramework
from robot.api import ExecutionResult
from robot.api import TestSuiteBuilder, ResultWriter

import settings
from .suite import obj, DictToObject


class PreCondition(object):
    """
    前置处理
    """
    def __init__(self, resolve):
        self.resolve = resolve

    def build(self):
        """
        设置配置信息到settings中
        """
        data = self.resolve.get_data()
        if sys.argv[-1] in [
            obj.ALPHA,
            obj.BETA,
        ]:
            constant = data.get(sys.argv[-1])
            setattr(settings, 'roles', constant)
        else:
            constant = data.get(obj.ALTA)
            setattr(settings, 'roles', constant)


class RunCondition(object):
    """
    运行
    """
    PASS = 0
    opt = {
        'LOG': 'log.html',
        'REPORT': 'report.html',
        'OUTPUT': 'output.xml',
        'RERUN': 'rerunfailed',
        'NAME': 'name'
    }

    def __init__(self, resolve, options):
        self.resolve = resolve
        self.options = options
        self.bot = DictToObject(self.opt)

    def need_run(self):
        """
        判断是否允许再次运行失败项
        :return:
        """
        result = ExecutionResult(self.bot.OUTPUT)
        if result.statistics.suite.stat.failed == self.PASS:
            return False

        if os.path.exists(self.bot.LOG) and os.path.exists(self.bot.REPORT):
            os.remove(self.bot.LOG)
            os.remove(self.bot.REPORT)
        return True

    def start(self):
        """
        单线程运行
        """
        robot = self.resolve.get_robot()
        self.options[self.bot.NAME] = self.resolve.item

        if self.options.get(self.bot.RERUN):
            if self.need_run():
                self.options['log'] = None
                self.options['report'] = None
                self.run(robot, self.options)
        else:
            self.run(robot, self.options)

    def start_concurrency(self):
        """
        多线程运行
        """
        robot = self.resolve.get_robot()
        pool = Pool(processes=len(robot))
        for suite_robot in robot:
            pool.apply_async(run_single, [suite_robot])
        pool.close()
        pool.join()

    def run(self, robot, options):
        RobotFramework().execute(*robot, **options)


def run_single(data_sources):
    suite = TestSuiteBuilder().build(data_sources)
    suite.configure()
    suite.run(output=u'{0}/{1}.xml'.format(obj.RESULTS_DIR, os.path.basename(data_sources)))


class PostCondition(object):
    """
    后置处理
    """
    def __init__(self, resolve, options):
        self.resolve = resolve
        self.options = options

    def dispose(self):
        """
        如果带rerunfailed，重新生成测试报告
        如果运行yaml文件，处理数据，生成覆盖率报告
        """
        pass

    def dispose_concurrency(self):
        """
        删除生成的多个测试报告
        """
        self.result_aggregate()
        shutil.rmtree(obj.RESULTS_DIR, ignore_errors=True)

    def result_aggregate(self):
        """
        聚合测试报告
        """
        xml_files = [os.path.join(obj.RESULTS_DIR, f) for f in os.listdir(obj.RESULTS_DIR) if f.endswith('.xml')]
        ResultWriter(*xml_files).write_results(name=self.resolve.item, output='output.xml')
