import os
from optparse import OptionParser
from bot.suite import ResolveFile
from bot.builder import TestBuilder
from bot.director import TestDirector


def parser_option():
    parser = OptionParser()
    parser.add_option(
        '-r', '--rebot',
        dest='test_suite_rebot',
        help='select yaml file or robot file', )
    parser.add_option(
        '-p', '--pabot',
        dest='test_suite_pabot',
        help='A parallel executor for Robot Framework test cases.', )
    (options, args) = parser.parse_args()
    return options, args


def main():
    robot_options = {}
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    options, args = parser_option()

    if options.test_suite_rebot:
        resolve = ResolveFile(options.test_suite_rebot)

    elif options.test_suite_pabot:
        resolve = ResolveFile(options.test_suite_pabot, is_concurrency=True)

    else:
        raise AttributeError

    builder = TestBuilder(resolve, robot_options)
    director = TestDirector(builder)
    suite = director.build_suite()
    suite.execute()


if __name__ == '__main__':
    main()
