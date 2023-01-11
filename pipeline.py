from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import requests
import time
import csv
import output as logc


def driver_setup():
    logc.status('Setting up', webdriver, 'INFO')
    return webdriver.Firefox(executable_path=r'./driver/geckodriver')


def get(webdriver, url):
    logc.status('Redirecting', url, 'INFO')
    webdriver.get(url)


def send(driver, keys):
    logc.status('Sending keys', keys, 'INFO')
    driver.send_keys(keys)


def click(driver):
    logc.status('Clicking', driver, 'INFO')
    driver.click()


def clear(driver):
    logc.status('Clearing', driver, 'INFO')
    driver.clear()


def get_xpath(webdriver, tag, id, id_name, attr=None):

    # Clean
    tag.lower()
    id.lower()

    # String path
    path = f"//{tag}[@{id}='{id_name}']"
    path_attr = f"{attr}"

    # Find path
    if attr is None:
        return webdriver.find_element(By.XPATH, path)
    else:
        attr.lower()
        return webdriver.find_element(By.XPATH, path).get_attribute(path_attr)


def get_xpath_current(webdriver, tag, id, id_name, attr=None):

    # Clean
    tag.lower()
    id.lower()

    # String path
    path = f".//{tag}[@{id}='{id_name}']"
    path_attr = f"{attr}"

    # Find path
    if attr is None:
        return webdriver.find_element(By.XPATH, path)
    else:
        attr.lower()
        return webdriver.find_element(By.XPATH, path).get_attribute(path_attr)


def get_xpath_current_text(webdriver, tag, id, id_name, attr=None):

    # Clean
    tag.lower()
    id.lower()

    # String path
    path = f".//{tag}[@{id}='{id_name}']"
    path_attr = f"{attr}"

    # Find path
    if attr is None:
        return webdriver.find_element(By.XPATH, path).text
    else:
        attr.lower()
        return webdriver.find_element(By.XPATH, path).get_attribute(path_attr).text


def get_xpaths(webdriver, tag, id, id_name, attr=None):

    # Clean
    tag.lower()
    id.lower()

    # String path
    path = f"//{tag}[@{id}='{id_name}']"
    path_attr = f"{attr}"

    # Find path
    if attr is None:
        # NO ATTR
        return webdriver.find_elements(By.XPATH, path)
    else:
        attr.lower()
        return webdriver.find_elements(By.XPATH, path)


def get_xpaths_current(webdriver, tag, id, id_name, attr=None):

    # Clean
    tag.lower()
    id.lower()

    # String path
    path = f".//{tag}[@{id}='{id_name}']"
    path_attr = f"{attr}"

    # Find path
    if attr is None:
        return webdriver.find_elements(By.XPATH, path)
    else:
        attr.lower()
        return webdriver.find_elements(By.XPATH, path).get_attribute(path_attr)


def get_id(webdriver, id):
    id.lower()
    return webdriver.find_element(By.ID, id)


def wait_to_find_frame_xpath(webdriver, time, id, id_name):
    '''WebDriverWait(driver, 20).until(EC.frame_to_be_available_and_switch_to_it(
        (By.XPATH, "//iframe[@id='duo_iframe']")))'''
    id.lower()
    path = f"//iframe[@{id}='{id_name}']"
    WebDriverWait(webdriver, time).until(
        EC.frame_to_be_available_and_switch_to_it((By.XPATH, path)))


def wait_to_be_clickable(webdriver, time, tag, id, id_name):
    '''WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
    (By.XPATH, "//button[normalize-space()='Send Me a Push']"))).click()'''
    tag.lower()
    id.lower()
    path = f"//{tag}[@{id}='{id_name}']"
    WebDriverWait(webdriver, time).until(
        EC.element_to_be_clickable((By.XPATH, path))).click()


def wait_to_be_clickable_custom_id(webdriver, time, tag, id, id_name):
    '''WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
    (By.XPATH, "//button[normalize-space()='Send Me a Push']"))).click()'''
    tag.lower()
    id.lower()
    path = f"//{tag}[{id}='{id_name}']"
    WebDriverWait(webdriver, time).until(
        EC.element_to_be_clickable((By.XPATH, path))).click()


def find_images_from_directory(webdriver, tag, id, id_name, attr=None):
    images = get_xpaths(webdriver, tag, id, id_name)
    if attr is None:
        for i in images:
            src = str(i.get_attribute('src'))
            with open(src.rsplit('/', 1)[-1], 'wb') as handle:
                response = requests.get(src, stream=True)

                if not response.ok:
                    print(response)

                for block in response.iter_content(1024):
                    if not block:
                        break
                    handle.write(block)
            print(src.rsplit('/', 1)[-1])
    else:
        print("None")


def find_all_names(webdriver):
    names = webdriver.find_elements(
        By.CSS_SELECTOR, "*[aria-label^='View profile for']")
    with open('names.csv', 'w') as file:
        writer = csv.writer(file)
        for i in names:
            name = str(i.get_attribute('aria-label'))
            name2 = name.split('.')
            names3 = name2[0].split('View profile for ')
            writer.writerow([names3[1]])
            # names3[1] has the name


def get_user_data(webdriver):
    users = get_xpaths(webdriver, 'div', 'class', 'card-block card-block--10')
    logc.status('Found', users, 'FOUND')
    with open('users.csv', 'w', encoding='UTF8', newline='') as file:
        header = ['Name', 'Year', 'Interests', 'Picture URL', 'Shortened URL']
        data = []
        writer = csv.writer(file)
        writer.writerow(header)
        for user in users:
            name = user.find_element(
                By.CSS_SELECTOR, "*[aria-label^='View profile for']").text
            year = get_xpath_current_text(
                user, 'p', 'class', 'h5 media-heading')
            interests_elements = get_xpaths_current(
                user, 'p', 'class', 'h5 media-heading color-cg--user')
            interests = ""
            for row in interests_elements:
                item = row.find_elements(By.TAG_NAME, 'span')
                for spans in item:
                    interests += str(spans.get_attribute('data-original-title'))
            try:
                bio = user.find_element(
                    By.CSS_SELECTOR, "[aria-label='Tooltip. [ bio underscore full ]']").get_attribute('full-text')
            except NoSuchElementException:
                bio = "No Bio Present"
            picture_url = str(get_xpath_current(
                user, 'img', 'class', 'media-object media-object--bordered', 'src'))
            picture_url_shortened = picture_url.rsplit('/', 1)[-1]
            data.append(
                [name, year, interests, picture_url, picture_url_shortened])
            writer.writerows(data)
            data.clear()
            '''
            Optional debuging print statements
            logc.status('Found', name, 'FOUND')
            logc.status('Found', year, 'FOUND')
            logc.status('Found', interests, 'FOUND')
            logc.status('Found', bio, 'FOUND')
            logc.status('Found', picture_url, 'FOUND')
            logc.status('Fouund', picture_url_shortened, 'FOUND')
            print("-------------")'''


def make_post(webdriver, content):
    post = get_xpath(webdriver, 'textarea', 'class', 'form-control')
    post.click()
    post.clear()
    post.send_keys(content)

    # Account for appending latency
    time.sleep(2)
    submit_btn = get_xpath(webdriver, 'a', 'id', 'feed_post_post__post-btn')
    submit_btn.click()
