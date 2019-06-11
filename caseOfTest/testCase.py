import datetime
import time
import unittest
import ddt
from tools import HTMLTestRunner
from tools.getNewReport import GetNewReport
import os
from tools.emailOption import SendEmail
from selenium import webdriver
from config import settings
from handles.inputer import LoginHandle

@ddt.ddt
class MyUnitCase(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome(executable_path='chromedriver.exe')

        self.driver.get('https://reg.mail.163.com/unireg/call.do?cmd=register.entrance&from=163mail_right')

        #refresh刷新
        # self.driver.refresh()

        # self.driver.maximize_window()

        self.login=LoginHandle(self.driver)

        self.driver.implicitly_wait(5)

    def tearDown(self):
        for methodName,error in self._outcome.errors:
            if error:
                caseName=self._testMethodName
                reportErrorName=caseName+'.png'
                reportErrorPath=os.path.join(settings.reportDir,'screenshot',reportErrorName)
                self.driver.save_screenshot(reportErrorPath)
        self.driver.quit()

    @ddt.data(
        ('cws1135239005','cws12345','cws12456','ssss','17600035024'),
        ('1135239005','cws123456','cws123456','ssss','17600035024')
              )
    @ddt.unpack
    def testRegister(self,*data):
        email,password,ensurePassword,code,mobile=data
        self.login.sendEmail(email)
        self.login.sendPassword(password)
        self.login.sendEnsurePassword(ensurePassword)
        self.login.sendCode(code)
        self.login.sendMobile(mobile)
        time.sleep(2)
        loginError=self.login.getErrorOfEmail()
        self.assertFalse(loginError)

def run():
    suite=unittest.TestLoader().loadTestsFromTestCase(MyUnitCase)


    reportName=datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')+'.html'
    reportFile=os.path.join(settings.reportDir,reportName)
    with open(reportFile,'wb') as fp:
        runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title='This is my unitCase')
        runner.run(suite)
    lastReport=GetNewReport()
    reportFile=lastReport.theLastReport()
    sendEmail=SendEmail()
    sendEmail.sendEmail(reportFile)