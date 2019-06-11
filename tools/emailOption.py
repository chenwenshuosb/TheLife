import smtplib
from email.mime.text import MIMEText
from email.header import Header

import os

from config import settings
from tools.getNewReport import GetNewReport

newReport=GetNewReport()
reportFile=newReport.theLastReport()

class SendEmail():

    def __init__(self):

        self.recevices=settings.recevices  #收件人

        self.smtpServer=settings.smtpServer #smtp服务器ip
        self.passCode=settings.passCode #授权码
        self.sender=settings.sender #发件人


    def getReportFile(self,reportFile):
        #拼接到最新测试报告的位置
        reportPath=os.path.join(settings.reportDir,reportFile)
        #读取内容并且返回
        with open(reportPath,'rb') as fp:
            reportContent=fp.read()
        return reportContent

    def sendEmail(self,reportFile):
        reportContent=self.getReportFile(reportFile)
        message=MIMEText(reportContent,'html','utf-8')
        message['Subject']=Header('第一个项目的邮件发送题目','utf-8')
        message['From']=Header('Mr.陈自动化测试工程师','utf-8')
        message['To']=Header('我敬爱的项目经理','utf-8')

        server=smtplib.SMTP(settings.smtpServer,25)

        #设置debugger
        # server.set_debuglevel(1)

        server.login(self.sender,self.passCode)
        try:
            server.sendmail(self.sender,self.recevices,message.as_string())
            print("Email send successful")
        except smtplib.SMTPException as e:
            print('Email send fail')
        server.close()

