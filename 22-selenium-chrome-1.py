from selenium import webdriver
from time import sleep

# chrome_options = webdriver.ChromeOptions()
# dr = webdriver.Chrome(options=chrome_options)

# @link:https://stackoverflow.com/a/60168019/4000911
options = webdriver.ChromeOptions()
options.add_argument('--remote-debugging-port=9222')
dr = webdriver.Chrome(options=options)

dr.get("https://www.google.com")
# dr.get("file:///home/avraham/Documents/Elearning/devops/DevopsExperts/devops1223/Python/lesson4/tip_calc_2/index.html")
sleep(10)
