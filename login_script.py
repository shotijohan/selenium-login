from selenium import webdriver
import time


#For Chrome drivers can be downloaded at https://sites.google.com/a/chromium.org/chromedriver/downloads
chrome_browser=webdriver.Chrome("/home/user/Downloads/chromedriver")
#For Firefox drivers can be downloaded at https://github.com/mozilla/geckodriver/releases
firefox_browser=webdriver.Firefox("/home/user/Downloads/geckodriver")

chrome_browser.get("link_here") #<-link here is the sign in link

# driver.find_element_by_css_selector('.button .c_button .s_button').click() <-this is just a sample of accessing a class.

username = chrome_browser.find_element_by_name("fieldUsername") 
#^ getting the element of the browser (Username)
password = chrome_browser.find_element_by_name("fieldPassword") 
#^ getting the element of the browser (Password)
login_button = chrome_browser.find_element_by_id('button-id') 
#^ getting the element of the browser (Login button, Sign-in button or Submit Button)

username.send_keys("username")
password.send_keys("yourpassword")
time.sleep(1) 
#^ lets the browser load for 1 sec

login_button.click() #<- clicks on the login, sign in or submit button
chrome_browser.close() #<-closes the browser
#to execute this script, you must have Python 2.7 or 3 in your computer already installed.
#simply type 'python login_script.py' on the terminal. 
#terminal should also be where the script is located