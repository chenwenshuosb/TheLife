from middleware.findElement import FindElement


#需要测试的元素
class LoginPage():
    def __init__(self,driver):
        self.find=FindElement(driver)

    #每个输入框进行测试
    def getEmailElement(self):
        return self.find.getElement('register','email')

    def getPasswordElement(self):
        return self.find.getElement('register','password')

    def getEnsurePasswordElement(self):
        return self.find.getElement('register','ensurePassword')

    def getCodeElement(self):
        return self.find.getElement('register','code')

    def getMobileElement(self):
        return self.find.getElement('register','mobile')

    def getButtonElement(self):
        return self.find.getElement('register','reg')

    def getEmailError(self):
        return self.find.getElement('register','emailError')

    def getPasswordError(self):
        return self.find.getElement('register','passwordError')


