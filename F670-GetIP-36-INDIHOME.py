# Auto restart modem untuk cari IP 36 Indihome F670
# by minkziibuby 07/08/2024
# karena tidak ada super admin, jadi pakai method restart ONT

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options


import time


ipont = "http://192.168.1.1/"
user = "user"
password = "user"

options = Options()
driver = webdriver.Chrome(options=options)

#options.add_experimental_option("detach", True)

try:
    driver.implicitly_wait(20)

    while True:

        driver.get(ipont)
        driver.set_window_size(900, 900)
        #page Login
        driver.find_element(By.ID, "Frm_Username").click()
        driver.find_element(By.ID, "Frm_Username").send_keys(user)
        driver.find_element(By.ID, "Frm_Password").send_keys(password)
        driver.find_element(By.ID, "LoginId").click()
        driver.switch_to.frame(1)
        #check IP
        driver.find_element(By.ID, "smWanStatu").click()
        #cari IP
        ipaddr = driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/div[3]/table[2]/tbody/tr[5]/td[2]/input")
        input_text = ipaddr.get_attribute('value')
        print("IP : ",input_text)
        
        if input_text.startswith(("36")):
            print("IP sudah didapatkan, Tidak Perlu Restart")
            break
        
        driver.find_element(By.ID, "Fnt_mmManager").click()
        driver.find_element(By.ID, "smSysMgr").click()
        driver.find_element(By.ID, "Submit1").click()
        driver.find_element(By.ID, "msgconfirmb").click()
        print("Restarting..")
        time.sleep(90)
finally:
    driver.quit()