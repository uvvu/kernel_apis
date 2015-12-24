#!/usr/bin/env python
import os
import re


def filterSet():
    declare = "^("
    declare += "static"
    declare += "|extern"
    declare += "|int"
    declare += "|char"
    declare += "|void"
    declare += "|bool"
    declare += "|unsigined"
    declare += ")"

    regex = "(" + "\s+.*?\(" + ")"

    declare = declare + regex

    return declare


def findApi(codeList):
    apiList = []
    declare = filterSet()

    p = re.compile(declare)

    for x in range(0, len(codeList)):
        if re.match(p, codeList[x]):
            apiList.append(re.match(p, codeList[x]).group())

    return apiList


def makeFileList():
    fileList = []
    for (path, dir, files) in os.walk("./"):
        for file in files:
            if file.endswith('.h'):
                fileList.append(os.path.join(path, file))
                # print file

    return fileList


def main():
    declare = filterSet()
    fileList = makeFileList()

    for file in fileList:
        codeList = open(file, 'r').readlines()
        apiList = findApi(codeList)
        out = open('output.txt', 'a')
        for api in apiList:
            out.write("%s\n" % api)
        out.close()


if __name__ == '__main__':
    main()

