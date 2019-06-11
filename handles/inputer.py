from basepage.loginPage import LoginPage

#自动输入功能
class LoginHandle():

    def __init__(self,driver):
        self.driver=driver
        self.login=LoginPage(self.driver)
    def sendEmail(self,email):
        self.login.getEmailElement().send_keys(email)

    def sendPassword(self,password):
        self.login.getPasswordElement().send_keys(password)

    def sendEnsurePassword(self,ensurePassowrd):
        self.login.getEnsurePasswordElement().send_keys(ensurePassowrd)

    def sendCode(self,code):
        self.login.getCodeElement().send_keys(code)

    def sendMobile(self,mobile):
        self.login.getMobileElement().send_keys(mobile)

    def clickSubmit(self):
        self.login.getButtonElement().click()

    # def getErrorOfEmail(self,info):
    #     try:
    #         textError=self.login.getEmailError()
    #     except:
    #         textError=None
    #     return textError
    def getErrorOfEmail(self):
        if self.login.getEmailError():
            return True
        return False






