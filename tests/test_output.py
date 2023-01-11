import output as logc
import pipeline as pipeline
from selenium import webdriver
import io
from contextlib import redirect_stdout


# Implemenet unit test for scraper
'''def test_output():
    driver = pipeline.driver_setup()
    f = io.StringIO()
    with redirect_stdout(f):
        logc.status('Setting up', driver, 'INFO')
    output = f.getvalue()
    assert output == f'Setting up : {driver}'
'''


def test_driver_setup():
    driver = pipeline.driver_setup()
    assert driver is not None


def test_get():
    driver = pipeline.driver_setup()
    pipeline.get(driver, 'https://www.google.com')
    assert driver.current_url == 'https://www.google.com/'
    
def test_send():
    driver = pipeline.driver_setup()
    pipeline.get(driver, 'https://www.google.com')
    pipeline.send(driver, 'test')
    
    
# Implement send, click, clear, get_xpath, get_xpath_current, get_id, wait_to_find_frame_xpath, wait_to_be_clickable_custom_id, get_user_data, make_post,
