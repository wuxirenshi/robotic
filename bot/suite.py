# -*- coding: utf-8 -*-
from __future__ import division

import os
import yaml

from settings import configure


class DictToObject(object):
    """
    字典转对象
    """
    def __init__(self, conf):
        self.conf = conf

    def __getattr__(self, item):
        return self.conf[item]


obj = DictToObject(configure)


class ResolveFile(object):
    """
    解析传入的文件
    """
    def __init__(self, name, is_concurrency=False):
        self.name = name
        self.is_concurrency = is_concurrency

    def get_data(self):
        """
        load yaml文件
        :return:
        """
        yaml_file = self.get_yaml()
        return yaml.load(open(yaml_file))

    def get_yaml(self):
        """
        获取测试文件
        :return:
        """
        if self.is_yaml:
            return self.name

        if self.is_robot:
            path = os.path.dirname(os.path.dirname(self.name))
            return os.path.join(path, '{}TestSuite.yaml'.format(self.item))

    def get_robot(self):
        """
        robot文件列表
        :return:
        """
        if self.is_yaml:
            yaml_data = self.get_data()
            return [os.path.join(yaml_data[obj.TEST_CASES_PATH], robot_name)
                    for robot_name in yaml_data[obj.TEST_CASES]]
        if self.is_robot:
            return [self.name]

    @property
    def is_yaml(self):
        """
        判断是否是yaml文件
        :return:
        """
        return self.name.endswith('yaml')

    @property
    def is_robot(self):
        """
        判断是否是robot文件
        :return:
        """
        return self.name.endswith('robot')

    @property
    def item(self):
        """
        项目名
        :return:
        """
        if self.is_yaml:
            return os.path.basename(os.path.dirname(self.name))

        if self.is_robot:
            path = os.path.dirname(os.path.dirname(self.name))
            return os.path.basename(path)


class TestCase(object):
    """
    测试用例类
    """
    def __init__(self, pre_condition, run_condition, post_condition, is_concurrency=False):
        self.pre_condition = pre_condition
        self.run_condition = run_condition
        self.post_condition = post_condition
        self.is_concurrency = is_concurrency

    def execute(self):
        """
        运行流程
        """
        self.pre_condition.build()

        if self.is_concurrency:
            self.run_condition.start_concurrency()
            self.post_condition.dispose_concurrency()
        else:
            self.run_condition.start()

        self.post_condition.dispose()

