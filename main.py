#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
    References
        INPUT YOUR REFERNCE PAGES
"""
__version__ = '0.1.0.0a0'

import sys

from modParsing.parsing import KernelParsing
from modGitAnalysis.humanfactor import CommentAnalyzer
from modConSQL.connsql import PythonSQL

reload(sys)
sys.setdefaultencoding('utf-8')


class Usage(Exception):
    def __init__(self, msg):
        self.msg = msg


def main(argv=None):
    parser = KernelParsing()
    cmmtAnalyze = CommentAnalyzer()

    # Analizing Methods
    cmmtAnalyze.extractChangeID()
    cmmtAnalyze.extractDiffCode()
    for x in cmmtAnalyze.addedCode:
        print "-------------------------------------------------------------------------------"
        print x

    # API Extraction Module
    fileList = parser.makeFileList()
    for file in fileList:
        #print "Analyzing", file, "..."
        codeList = open(file, 'r').readlines()
        apiList = parser.findApi(codeList)
        apiName = parser.refineApis(apiList)
        out = open('output.txt', 'a')
        for api in apiName:
            out.write("%s\n" % api)
        out.close()

if __name__ == "__main__":
    sys.exit(main())
