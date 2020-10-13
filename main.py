# coding = utf-8
from selenium import webdriver
from time import sleep
import datetime
import json
import random
import os
import sys
path = os.path.abspath(os.path.dirname(sys.argv[0]))
# 初始化设置
def InitSetting():
    try:
        SettingFile = open(path + "\setting.dat")
        SettingData = json.load(SettingFile)
        print (u'读取到保存的设置: ')
        for key in SettingData:
            print ('[%s] %s' % (key, SettingData[key]))
        op = input('是否使用已保存的设置？[Y/N]')
        if not op in ['n', 'N', 'no', 'No', 'NO']:
            global Id, Password
            for key in ['Id', 'Password']:
                globals()[key] = SettingData[key]
        else:
            NewSetting()
    except:
        print (u'读取设置失败')
        NewSetting()
 
# 输入信息，保存到本地
def NewSetting():
    global Id, Password
    Id = input('请输入学号: ')
    Password = input('请输入密码: ')
    Data = dict()
    for key in ['Id', 'Password']:
        Data[key] = globals()[key]
    json.dump(Data, open(path + "\setting.dat", 'w'))


# 账号登录
def Register(driver):
    global Id, Password
    sleep(2)
    driver.find_element_by_id('username').clear()
    driver.find_element_by_id('username').send_keys(Id)
    driver.find_element_by_id('password').clear()
    driver.find_element_by_id('password').send_keys(Password)
    driver.find_element_by_id('login-submit').click()

# 内容填写
def Fill(driver):
    temperature = round(random.uniform(36, 37), 1)
    sleep(1)
    driver.find_element_by_id('p1_ChengNuo-inputEl-icon').click()
    sleep(1)
    driver.find_element_by_id('p1_TiWen-inputEl').clear()
    driver.find_element_by_id('p1_TiWen-inputEl').send_keys(str(temperature))
    sleep(1)
    driver.find_element_by_id('fineui_7-inputEl-icon').click()
    sleep(1)
    driver.find_element_by_id('p1_ctl00_btnSubmit').click()
    sleep(1)
    driver.find_element_by_id('fineui_14').click()
    sleep(1)
    driver.find_element_by_id('fineui_19').click()

def Reoprt():
    driver_url_edge = path + "\msedgedriver.exe"
    driver = webdriver.Edge(executable_path=driver_url_edge)
    today = datetime.date.today()
    hour = int(str(datetime.datetime.now())[11:13])
    uri = "https://selfreport.shu.edu.cn/XueSFX/HalfdayReport.aspx?day=" + str(today) + "&t=" + ("1" if hour < 18 else "2")
    driver.get(uri)
    Register(driver) # 登录账号
    Fill(driver) # 内容填写
    driver.close()

# def HistoryReport():
#     driver_url_edge = r"AutoReport\msedgedriver.exe"
#     driver = webdriver.Edge(executable_path=driver_url_edge)
#     today = datetime.date.today()
#     for i in range(2, 5):
#         date = today - datetime.timedelta(days=1)
#         for j in range(1, 3):
#             uri = "https://selfreport.shu.edu.cn/XueSFX/HalfdayReport.aspx?day=" + str(date) + "&t=" + str(j)
#             driver.get(uri)
#             Register(driver)
#             Fill(driver)
#             driver.close()
    # hour = int(str(datetime.datetime.now())[11:13])
    # uri = "https://selfreport.shu.edu.cn/XueSFX/HalfdayReport.aspx?day=" + str(today) + "&t=" + "1" if hour < 18 else "2"
    # driver.get(uri)
    # Register(driver) # 登录账号
    # Fill(driver) # 内容填写
    # driver.quit()



if __name__ == '__main__':
    # 全局设置
    Id, Password = '', ''
    InitSetting()
    Reoprt()
    # HistoryReport()




