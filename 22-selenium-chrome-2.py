from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# @link:https://stackoverflow.com/a/60168019/4000911
options = webdriver.ChromeOptions()
options.add_argument('--remote-debugging-port=9222')
dr = webdriver.Chrome(options=options)

dr.get("file:///home/avraham/Documents/Elearning/devops/DevopsExperts/devops1223/Python/lesson4/tip_calc_2/index.html")

# dr.get("https://github.com")
billamt = dr.find_element(by="id", value="billamt")
billamt.send_keys("100")
dr.find_element(by="xpath", value="//*[@id=\"serviceQual\"]/option[3]").click()
dr.find_element(by="id", value="peopleamt").send_keys("5")
dr.find_element(by="id", value="musicQual").send_keys("5")
dr.find_element(by="id", value="calculate").click()
actual = dr.find_element(by="id", value="tip").text
expected = "9"
assert expected == actual