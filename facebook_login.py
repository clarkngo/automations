# this is to test my first automation using Python in MacOS
# Steps:
# 1 - Check if you have Selenium with command "pip freeze | grep selenium"
#     If you don't have it, "pip install selenium"
# 2 - Download ChromeDriver at https://sites.google.com/a/chromium.org/chromedriver/
# 3 - Unzip and place in a folder. I placed the 'chromedriver' at /User/clarkngo/drivers
# 4 - Edit your path with command "sudo nano /etc/paths"
# 5 - Add the path of your driver in /etc/paths (Example: /User/clarkngo/drivers)
# 6 - Execute the code below
# Resources:
# https://youtu.be/-6H3xyhPK3I
# https://www.kenst.com/2015/03/including-the-chromedriver-location-in-macos-system-path/

from selenium import webdriver
from getpass import getpass

user = input('Enter username or email id: ')
password = getpass('Enter your password: ')

driver = webdriver.Chrome()
driver.get('http://www.facebook.com/')

username_box = driver.find_element_by_id('email')
username_box.send_keys(user)

password_box = driver.find_element_by_id('pass')
password_box.send_keys(password)

login_button = driver.find_element_by_id('u_0_b')
login_button.submit()
