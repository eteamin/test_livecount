import sys
from src.messenger import Messenger
from src import livecounttest

__author__ = 'amin'
__version__ = '0.2.0a'


def main():
    livecounttest.test_live_count()
    sys.exit(0)
