# -*- coding: utf-8 -*-

from .suite import TestCase


class TestDirector(object):
    """
    条件组装
    """
    def __init__(self, builder):
        self.builder = builder

    def build_suite(self):
        """
        生成测试集
        :return:
        """
        pre_condition = self.builder.pre_condition()
        run_condition = self.builder.run_condition()
        post_condition = self.builder.post_condition()
        return TestCase(pre_condition, run_condition, post_condition, self.builder.resolve.is_concurrency)
