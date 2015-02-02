from setuptools import setup
from setuptools.command.test import test as TestCommand
import hungry
import sys


def get_requirements(suffix=''):
    with open('requirements%s.txt' % suffix) as f:
        result = f.read().splitlines()
    return result


def get_long_description():
    with open('README.rst') as f:
        result = f.read()
    return result


class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = ['--cov=hungry']
        self.test_suite = True

    def run_tests(self):
        import pytest

        errcode = pytest.main(self.test_args)
        sys.exit(errcode)


setup(
    name='hungry',
    version=hungry.__version__,
    description='Easily eats exceptions using decorators',
    long_description=get_long_description(),
    author='Deniz Dogan',
    author_email='deniz@dogan.se',
    url='https://github.com/denizdogan/hungry',
    license='MIT',
    packages=['hungry', 'test'],
    platforms='any',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Operating System :: OS Independent',
    ],
    install_requires=get_requirements(),
    tests_require=get_requirements('-dev'),
)
