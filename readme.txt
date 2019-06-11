//目标
    ->对126邮箱进行注册测试（https://reg.mail.163.com/unireg/call.do?cmd=register.entrance&from=163mail_right）

//功能实现
1.自动运行用例
2.自动生成测试报告
3.自动断言与截图
4.自动将最新的测试报告以邮件方式发送
5.PO+Unittest+ddt

//目录结构
basepage: po模型主干区
caseOfTest: 主要测试执行
config: 配置文件和基础配置
handles: 主要的操作功能
middleware: 必要的中间流程 查找元素方式
report: 测试报告存放位置
testBegin: 调用操作功能 准备测试
tools: 第三方工具
main.py: 执行之后开始测试

//附加信息
    ->作者:陈文硕
    ->日期:2019/6/10