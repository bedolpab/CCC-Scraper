import time
import pipeline as pipeline
import locals
from selenium.webdriver.common.by import By
import time


driver = pipeline.driver_setup()
pipeline.get(driver, locals.LOGIN_PAGE)
# Login Portal
login1 = pipeline.get_xpath(
    driver, 'a', 'class', 'btn btn--school btn--full-width', 'href')
pipeline.get(driver, login1)

# Login Credentials (Email)
time.sleep(5)
login_cred = pipeline.get_xpath(driver, 'input', 'id', 'i0116')
pipeline.click(login_cred)
pipeline.clear(login_cred)
pipeline.send(login_cred, locals.EMAIL)

# Login Credentials (Email - Button)
login_btn = pipeline.get_id(driver, 'idSIButton9')
pipeline.click(login_btn)

# Login Credentials (Password)
time.sleep(6)
login_pass = pipeline.get_id(driver, 'passwordInput')
pipeline.click(login_pass)
pipeline.clear(login_pass)
pipeline.send(login_pass, locals.PASSWORD)

# Login Credentiasl (Password - Button)
login_btn2 = pipeline.get_id(driver, 'submitButton')
pipeline.click(login_btn2)

time.sleep(7)
pipeline.wait_to_find_frame_xpath(driver, 50, 'id', 'duo_iframe')
pipeline.wait_to_be_clickable_custom_id(
    driver, 50, 'button', 'normalize-space()', 'Send Me a Push')
time.sleep(10)

pipeline.get(driver, locals.COLUMBIA_HOME_PAGE)
time.sleep(5)
pipeline.get(driver, locals.COLUMBIA_DIRECTORY_PAGE)
time.sleep(3)

# Endless page scroll
# Move to a method
SCROLL_PAUSE_TIME = 5

# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(SCROLL_PAUSE_TIME)
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height


input("Retreive user data: ")
pipeline.get_user_data(driver)

'''
CREATING A POST
driver.get(locals.COLUMBIA_FEED_PAGE)
time.sleep(10)
pipeline.make_post(driver,locals.POST_MESSAGE)'''

''' 
Downloading all images from directory
- Input is asked because page loads content slow, so you'll have to manually scroll to load all pages until feature is impelemented

input("LOAD ALL IMAGES, 'ENTER' TO RUN")
pipeline.find_images_from_directory(driver, 'img', 'class', 'media-object media-object--bordered')
'''
