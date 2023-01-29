from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# create a new Chrome browser instance
browser = webdriver.Chrome()

# navigate to the website
browser.get('https://www.example.com/login')

# find the email and password fields and enter the login credentials
email_field = browser.find_element_by_name('email')
email_field.send_keys('example@email.com')
password_field = browser.find_element_by_name('password')
password_field.send_keys('mypassword')

# submit the login form
password_field.send_keys(Keys.RETURN)

# wait for the page to load
browser.implicitly_wait(10)

# extract data from the page
data = browser.find_element_by_id('data').text

# print the data
print(data)

# close the browser
browser.quit()
