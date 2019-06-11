from tools.readConfig import ReadIniFile

#查找元素结点
class FindElement():
    def __init__(self,driver):
        self.driver=driver
    def getElement(self,section,option):

        read=ReadIniFile()
        data=read.readFile(section,option)
        #将配置文件数据进行分割
        by,value = data.split('|')
        #查看数据的查找方式和方式对应的值并且返回结果
        try:
            if by=='id':
                return self.driver.find_element_by_id(value)
            elif by=='name':
                return self.driver.find_element_by_name(value)
            elif by=='className':
                return self.driver.find_element_by_class(value)
            elif by=='xpath':
                return self.driver.find_element_by_xpath(value)

        except Exception as e:

            return None