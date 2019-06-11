import os
from config import settings

class GetNewReport():

    # 获取最新的测试报告

    def theLastReport(self):

        #listdir方法用于返回指定文件夹内的文件名称的列表
        myList=os.listdir(settings.reportDir)
        if not myList:
            myList=['myReport.html']
        lastReport=self.getLastReport(myList)
        return lastReport

    #遍历报告文件夹,取出最先的一条
    def getLastReport(self,myList):
        reportList=[]
        for l in myList:
            if l.endswith('html'):
                reportList.append(l)
        newReport=reportList[-1]
        return newReport


if __name__=='__main__':
    newReport=GetNewReport()
    newReport.theLastReport()