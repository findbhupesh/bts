from selenium import webdriver
from selenium.webdriver.common.by       import By
from selenium.webdriver.support.ui      import Select

def open_browser():
    option = webdriver.ChromeOptions()
    option.add_experimental_option("detach",True)
    option.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=option)
    return driver

def click_btn(*args):
    driver = args[0]
    xpaths = args[1]
    try:
        driver.find_element(By.XPATH,xpaths).click()
    except:
        pass

def send_keys(*args):
    driver = args[0]
    xpaths = args[1]
    xvalue = args[2]

    try:
        driver.find_element(By.XPATH,xpaths).send_keys(xvalue)
    except:
        pass

def selectkey(*args):
    driver = args[0]
    xpaths = args[1]
    xvalue = args[2]
    combob = Select(driver.find_element(By.XPATH,xpaths))
    combob.select_by_visible_text(xvalue)