#!/usr/bin/env python
import os
import re

class KernelParsing:
    def __init__(self):
        self.declare = ""
        self.declare = "^("
        self.declare += "static"
        self.declare += "|extern"
        self.declare += "|int"
        self.declare += "|char"
        self.declare += "|void"
        self.declare += "|bool"
        self.declare += "|unsigined"
        self.declare += ")"

        self.regex = "(" + "\s+.*?\(" + ")"

        self.declare = self.declare + self.regex


    def findApi(self, codeList):
        apiList = []
        declare = self.declare

        p = re.compile(declare)

        for x in range(0, len(codeList)):
            if re.match(p, codeList[x]):
                apiList.append(re.match(p, codeList[x]).group())

        return apiList


    def makeFileList(self):
        fileList = []
        for (path, dir, files) in os.walk("/home/taeyoung/work/linux_kernel/linux/"):
            for file in files:
                if file.endswith('.h'):
                    fileList.append(os.path.join(path, file))

        return fileList


    def refineApis(self, apiList):
        apiName = []
        for i in range(0, len(apiList)):
            api = (apiList[i].split(' ')[-1]).split('(')[0]
            api = api.replace("*", "")
            apiName.append(api)

        apiName = list(set(apiName))

        return apiName


