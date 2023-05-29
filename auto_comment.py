from selenium.webdriver.common.by import By

# 自动完成学生评价


def auto_comment(driver, time):
    driver.find_element(By.ID, "cdNav").find_elements(By.CLASS_NAME, "nav")[
        0].find_elements(By.CLASS_NAME, "dropdown")[4].find_element(By.ID, "drop1").click()
    time.sleep(3)
    driver.find_element(By.ID, "cdNav").find_elements(By.CLASS_NAME, "nav")[0].find_elements(By.CLASS_NAME, "open")[
        0].find_elements(By.CLASS_NAME, "dropdown-menu")[0].find_elements(By.TAG_NAME, "li")[0].find_elements(By.TAG_NAME, "a")[0].click()
    time.sleep(8)
    driver.switch_to.window(driver.window_handles[-1])
    # 在新窗口中执行操作
    driver.find_element(By.ID, "btn_yd").click()
    time.sleep(3)
    # for 循环从1到15一个一个试过去
    for i in range(1, 16):
        # 判断一下是否存在
        if driver.find_elements(By.ID, str(i)):
          driver.find_element(By.ID, str(i)).click()
          time.sleep(3)
          # 遍历所有class为form-group的元素
          form_groups = driver.find_elements(By.CLASS_NAME, "form-group")
          i = 0
          for form_group in form_groups:
              # 如果是第一次循环，那么点击的是第二个radio，否则点击的是第一个radio
              radio_pjfs = form_group.find_elements(By.CLASS_NAME, "radio-pjf")
              if i == 0:
                radio_pjfs[1].click()
                i += 1
              else:
                radio_pjfs[0].click()
          # 点保存按钮
          driver.find_element(By.ID, "btn_xspj_bc").click()
          time.sleep(1)
          driver.find_element(By.ID, "btn_ok").click()
          time.sleep(1)