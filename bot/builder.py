# -*- coding: utf-8 -*-

from .control import (
    PreCondition,
    RunCondition,
    PostCondition
)


class TestBuilder(object):
    """
    测试用例整个build流程
    """
    def __init__(self, resolve, options):
        self.resolve = resolve
        self.options = options

    def pre_condition(self):
        """
        前置条件
        :return:
        """
        return PreCondition(self.resolve)

    def run_condition(self):
        """
        运行配置
        :return:
        """
        return RunCondition(self.resolve, self.options)

    def post_condition(self):
        """
        后置条件
        :return:
        """
        return PostCondition(self.resolve, self.options)