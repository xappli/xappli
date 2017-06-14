# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#browser = webdriver.Firefox()
browser = webdriver.PhantomJS()
browser.get("http://reser.camp-cabins.com/cc_reserve/sv_open")

main_window_handle = None
while not main_window_handle:
    main_window_handle = browser.current_window_handle
browser.find_element_by_name("email").clear()
browser.find_element_by_name("email").send_keys("hideno.lee@i.softbank.jp")
browser.find_element_by_name("passwd").clear()
browser.find_element_by_name("passwd").send_keys("505312")
browser.find_element_by_name("btnlogin").click()

signin_window_handle = None
while not signin_window_handle:
    for handle in browser.window_handles:
        if handle != main_window_handle:
            signin_window_handle = handle
            break
browser.switch_to.window(signin_window_handle)
#time.sleep(2)

browser.find_element_by_css_selector("input[type=\"image\"]").click()

#time.sleep(2)
Select(browser.find_element_by_name("space0")).select_by_visible_text(u"カントリーキャビン“焚火”")#施設
Select(browser.find_element_by_name("cin_yy0")).select_by_visible_text("2017")#予約年
Select(browser.find_element_by_name("cin_mm0")).select_by_visible_text("9")#予約月
Select(browser.find_element_by_name("cin_dd0")).select_by_visible_text("19")#予約日
browser.find_element_by_css_selector(u"img[alt=\"上記の内容で予約する\"]").click()

#time.sleep(2)
browser.find_element_by_name("n2017_9_19_num1").clear()
browser.find_element_by_name("n2017_9_19_num1").send_keys("2")#大人人数
browser.find_element_by_name("n2017_9_19_num4").clear()
browser.find_element_by_name("n2017_9_19_num4").send_keys("1")#幼児人数
browser.find_element_by_name("n2017_9_19_car1").clear()
browser.find_element_by_name("n2017_9_19_car1").send_keys("1")#普通車台数
browser.find_element_by_name("pet_yn").click()#ペットの有無
browser.find_element_by_name("n2017_9_19_pet3").clear()
browser.find_element_by_name("n2017_9_19_pet3").send_keys("1")#小型犬頭数
browser.find_element_by_css_selector(u"img[alt=\"上記内容で変更する\"]").click()

#time.sleep(2)
browser.find_element_by_name("check1_0").click()
browser.find_element_by_name("check1_1").click()
browser.find_element_by_name("check1_2").click()
browser.find_element_by_name("check1_3").click()
browser.find_element_by_name("check1_4").click()
browser.find_element_by_name("check1_5").click()
browser.find_element_by_name("check2_0").click()
browser.find_element_by_name("check2_1").click()
browser.find_element_by_name("check2_2").click()
browser.find_element_by_name("check2_3").click()
browser.find_element_by_name("check2_4").click()
browser.find_element_by_name("check2_5").click()
browser.find_element_by_name("check2_6").click()
browser.find_element_by_name("check2_7").click()
browser.find_element_by_name("check2_8").click()
browser.find_element_by_name("check2_9").click()
browser.find_element_by_name("check2_10").click()
browser.find_element_by_name("check2_11").click()
browser.find_element_by_name("check2_12").click()
browser.find_element_by_css_selector(u"img[alt=\"上記内容で変更する\"]").click()

#time.sleep(2)
browser.find_element_by_css_selector(u"img[alt=\"予約を確定する\"]").click()

#time.sleep(2)
browser.save_screenshot("test.jpg") # capture result page
browser.quit()

print("end")
