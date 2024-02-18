from selenium import webdriver
from time import sleep

dr = webdriver.Firefox()
# dr.get("https://www.google.com")
dr.get("file:///home/avraham/Documents/Elearning/devops/DevopsExperts/devops1223/Python/lesson4/tip_calc_2/index.html")
sleep(10)
