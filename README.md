# Introduction
 robotic is a test framework based on Robot Framework for auto test
 
## 描述
此结构适用于所有自动化测试，可以在此框架上改造成适合项目的接口自动化、网页自动化、soa自动化，允许多环境配置，单用例、多用例运行、并发运行
简化robot本身的自带的一些功能，如有需要，请在robot_options中按照robot的规则添加

## Usage

1. Run through command line with '-r' in alpha channel or beta channel. 单线程运行

	``python robotic.py -r suites/eos/eosTestSuite.yaml alpha``


2. Run through command line with '-p' in alpha channel or beta channel, can run concurrency. 多线程运行

	``python robotic.py -p suites/eos/eosTestSuite.yaml alpha``


3. Run single robot file. 单robot文件运行

    ``python robotic.py -r suites/eos/robots/TC-Test.robot alpha``

## Test Log
Test log locates at robotic/log.html folder. And take note that it will be overwritten everytime you run tests.

## Test Report
Test reports will be generated at robotic/report.html . And take note that it will be overwritten everytime you run tests.

## 测试用例案例地址
https://github.com/bulkan/robotframework-requests/#readme

Thank you!
