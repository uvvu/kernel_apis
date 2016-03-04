#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
    References
        INPUT YOUR REFERNCE PAGES
"""
__version__ = '0.1.0.0a0'

import sys
import os
import git
import re
import MySQLdb
import sys
import itertools
import time

from modParsing.parsing import KernelParsing
from gitAnalysis.humanfactor import commentAnalyzer

reload(sys)
sys.setdefaultencoding('utf-8')


class Usage(Exception):
    def __init__(self, msg):
        self.msg = msg


def main(argv=None):
    parser = KernelParsing()

    fileList = parser.makeFileList()
    for file in fileList:
        codeList = open(file, 'r').readlines()
        apiList = parser.findApi(codeList)
        apiName = parser.refineApis(apiList)
        out = open('output.txt', 'a')
        for api in apiName:
            out.write("%s\n" % api)
        out.close()

if __name__ == "__main__":
    sys.exit(main())
