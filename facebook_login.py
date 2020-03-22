# this is to test my first automation using Python in MacOS
# Step 1 - Download ChromeDriver at https://sites.google.com/a/chromium.org/chromedriver/
# Step 2 - Unzip and place in a folder. I placed the 'chromedriver' at /User/clarkngo/drivers
# Step 3 - Edit your path with command "sudo nano /etc/paths"
# Step 4 - Add the path of your driver in /etc/paths (Example: /User/clarkngo/drivers)
# Step 5 - Execute the code below
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
