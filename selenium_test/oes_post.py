from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

option = webdriver.ChromeOptions()
option.add_argument('disable-infobars')
browser = webdriver.Chrome(options  = option)
browser.get("http://10.254.5.177:8090")
browser.maximize_window()

browser.implicitly_wait(20) #隐式等待1s
name = browser.find_element_by_id('j_username')
name.send_keys("HA1")
password = browser.find_element_by_id('j_password')
password.send_keys("HA1")
btn = browser.find_element_by_id('loginbtn')
btn.click()

No_show = browser.find_element_by_xpath('/html/body/div[10]/div[1]')
#print(No_show.text)
No_show.click()

skip = browser.find_element_by_xpath('//*[@id="home_guide_index_box"]/div[6]/div')
skip.click()

open_main_menu = browser.find_element_by_id("module_click").click()

hr_menu = browser.find_element_by_xpath('//*[@id="moduleCententList"]/li[10]/a/i')
hr_menu.click()

time.sleep(5)
person_menu1 = browser.find_element_by_xpath('//*[@id="sidebar"]/li[4]')
person_menu1.click()

person_menu2 = browser.find_element_by_xpath('//*[@id="sidebar"]/li[4]/ul/li[1]')
person_menu2.click()

person_menu3 = browser.find_element_by_xpath('//*[@id="sidebar"]/li[4]/ul/li[1]/ul/li[2]/a')
person_menu3.click()

time.sleep(2)
browser.find_element_by_xpath('//*[@id="unieapx_layout_NavigatorPane_0grid1_customPageSizeComboBox"]/div[2]/a').click()
browser.find_element_by_xpath('//*[@id="unieap_form_ComboBoxPopup_0"]/div[2]/table/tbody/tr[3]').click()

str_xpath = '//*[@id="page-0"]/div[{0}]/table/tbody/tr/td[2]/div/div/a'
time.sleep(2)
max_page = browser.find_element_by_xpath('//*[@id="unieap_grid_view_toolbar_0"]/ul/li[8]').text
max_page = int(max_page)+1

for ipage in range(1,max_page):
    for irow in range(1,11):
        try:
            time.sleep(1)
            pageinput = browser.find_element_by_xpath('//*[@class="pageInput"]')
            pageinput.send_keys(str(ipage))
            pageinput.send_keys(Keys.ENTER)
            time.sleep(2)
            browser.find_element_by_xpath(str_xpath.format(irow)).click()
            browser.find_element_by_xpath('//*[@class="hr_emp_bom"]/a[2]').click()
            browser.find_element_by_xpath('//*[@id="x-dlg-dom"]/div[2]/a[2]').click()
            time.sleep(2)
        finally:
            pass
