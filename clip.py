# Safeway coupon auto clipper program
# install selenium, python, selenium for python and geckodriver
# to run: python clip.py [email] [password]

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import sys

if len(sys.argv) != 3:
	print "Program requires two agruments, [email] [password]"

# Firefox 
driver = webdriver.Firefox(executable_path='/Applications/geckodriver')

# ------------------------------
# The actual test scenario: Test the codepad.org code execution service.

# Go to codepad.org
driver.get('https://www.safeway.com/CMS/account/login/')

# Select the Python language option
python_link = driver.find_element_by_id('input-email')
python_link.send_keys(sys.argv[1])

# Enter some text!
text_area = driver.find_element_by_id('password-password')
text_area.send_keys(sys.argv[2])

time.sleep(2)

# Submit the form!
text_area.send_keys(Keys.RETURN)

time.sleep(30)

driver.get('http://www.safeway.com/ShopStores/Justforu-Coupons.page#/category/all')

height = 0

while height != driver.execute_script("return document.body.scrollHeight"):
	height = driver.execute_script("return document.body.scrollHeight")
	print height
	time.sleep(5)
	driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
	time.sleep(10)

time.sleep(30)

like = driver.find_elements_by_class_name('lt-place-add-button')
for x in range(0,len(like)):
    if like[x].is_displayed():
        like[x].click()

print "script completed"

# Close the browser!
driver.quit()
