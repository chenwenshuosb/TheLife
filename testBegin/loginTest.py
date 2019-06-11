from handles.inputer import LoginHandle

class LoginTest():
    def __init__(self,driver):
        self.login=LoginHandle(driver)

    def baseRegister(self,email,password,ensurePassword,code,mobile):
        self.login.sendEmail(email)
        self.login.sendPassword(password)
        self.login.sendEnsurePassword(ensurePassword)
        self.login.sendCode(code)
        self.login.clickSubmit()

    def loginState(self):
        #因为测试的目标是126邮箱 所以没有登录状态 只有注册
        if self.login.getErrorOfEmail(''):
            return False
        return True
