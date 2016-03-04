#!/usr/bin/python
"""
    References
        1. INPUT YOUR REFERENCE PAGES
"""
import re
import git

class CommentAnalyzer:
    def __init__(self):
        self.repository  = ("/home/taeyoung/work/linux_kernel/linux")
        self.changeIDList = []
        self.addedCode = []
        self.developerCommet = []
        self.repo = git.Repo(self.repository)

    def extractChangeID(self):
        """
            WRITE YOUR DESCIPTION DOWN HERE
        """
        self.changeIDList = list(self.repo.iter_commits())

    def extractDiffCode(self):
        tmpDiffList = []
        changeIDList = self.changeIDList
        cmmtDiff = []
        tmpAddedCode = []
        addedCode = []
        fullCode = []
        #for i in range(0, len(changeIDList) - 1):
        for i in range(0, 10):
            try:
                tmpDiffList.append(str(self.repo.git.diff(changeIDList[i], changeIDList[i + 1])))
                print "Processing... " + str(i) + " /" + str(len(changeIDList) - 2)
            except:
                print "Processing... " + str(i) + " /" + str(len(changeIDList) - 2) + " << str problem "
                tmpDiffList.append("No String Value")
                continue

        for i in range(0, len(tmpDiffList)):
            print "Extracting Added Codes beetween change IDs......"
            cmmtDiff = tmpDiffList[i]
            cmmtDiff = cmmtDiff.split('\n')
            for code in cmmtDiff:
                if re.match('\+', code):
                    tmpAddedCode.append(code)
            fullCode = "\n".join(tmpAddedCode)
            addedCode.append(fullCode)
            cmmtDiff = []
            fullCode = []

        self.addedCode = addedCode

    def extractDeveloperComment(self):
        print "TBD"
