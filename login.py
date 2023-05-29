from get_class_table import get_class_table
from auto_comment import auto_comment
from selenium import webdriver
from selenium.webdriver.common.by import By
import time  # 用于控制时间
import json  # 用于读取json文件
# 跳转逻辑（校园网情况下）：输入教务系统 url 之后会先跳转到统一身份验证登录
# 登录成功之后会跳转到教务系统登录页面，然后再跳转到统一身份验证登录，最后跳转到教务系统首页
# 不一定，有时候可能只会先统一身份验证登录，然后跳转到教务系统登录，然后跳转教务系统首页


def login():
    url = "https://jwxt.hznu.edu.cn"  # 教务系统网址
    # 读取json文件
    # 读取账号密码
    # username = input("请输入账号：")
    # password = input("请输入密码：")
    with open('config.json', 'r') as f:
        data = json.load(f)
        username = data['username']
        password = data['password']
        mode = data['mode']
    # 创建一个浏览器对象
    # 设置浏览器为中文
    options = webdriver.ChromeOptions()
    options.add_argument('lang=zh_CN.UTF-8')
    # options.add_argument('--headless') # 无头模式
    driver = webdriver.Chrome(options=options)
    # 打开教务系统网页
    driver.get(url)
    # 最大化窗口
    driver.maximize_window()
    time.sleep(3)
    # 跳转到统一身份验证登录
    # 填写用户密码
    driver.find_element(By.ID, "username").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login_submit").click()
    time.sleep(3)
    # 跳转到教务系统登录
    # 点击id为tysfyzdl的按钮
    driver.find_element(By.ID, "tysfyzdl").click()
    # time.sleep(3)
    # # 跳转到统一身份验证登录
    # driver.find_element(By.ID, "username").send_keys(username)
    # driver.find_element(By.ID, "password").send_keys(password)
    # driver.find_element(By.ID, "login_submit").click()
    time.sleep(3)
    if (mode == "auto_comment"):
        auto_comment(driver, time)
    elif (mode == "get_class_table"):
        get_class_table(driver, time)


if __name__ == "__main__":
    login()
