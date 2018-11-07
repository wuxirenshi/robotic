# Introduction
 robotic is a test framework based on Robot Framework for auto test

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
