import os

#邮箱配置
sender='1135239005@qq.com' #发件人

recevices=['1758562069@qq.com'] #收件人

smtpServer='smtp.qq.com' #smtp服务器

passCode='qkdykoabirbvhifb' #授权码


baseDir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))# 项目文件路径

configDir = os.path.join(baseDir, 'config', 'config.ini')  # 配置文件路径

reportDir = os.path.join(baseDir, 'report') #测试报告文件路径

