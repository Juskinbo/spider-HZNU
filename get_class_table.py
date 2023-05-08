from selenium.webdriver.common.by import By

# 获取课表
def get_class_table(driver, time):
    driver.find_element(By.ID, "cdNav").find_elements(By.CLASS_NAME, "nav")[0].find_elements(By.CLASS_NAME, "dropdown")[3].find_element(By.ID, "drop1").click()
    time.sleep(3)
    driver.find_element(By.ID, "cdNav").find_elements(By.CLASS_NAME, "nav")[0].find_elements(By.CLASS_NAME, "open")[
        0].find_elements(By.CLASS_NAME, "dropdown-menu")[0].find_elements(By.TAG_NAME, "li")[1].find_elements(By.TAG_NAME, "a")[0].click()
    time.sleep(3)
    # 跳转到课表页面
    driver.switch_to.window(driver.window_handles[-1])
    # 在新窗口中执行操作
    driver.find_element(By.ID, "shcPDF").click()
    time.sleep(5)
