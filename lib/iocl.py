import time
from selenium.webdriver.support.ui      import WebDriverWait
from selenium.webdriver.support         import expected_conditions as EC
from lib                                import auto
def upld_inv(web,data):
    web.get("https://associates.indianoil.co.in/BTS/vendor_login")
    auto.send_keys(web,"//input[@id='txtuserid']","11921208")
    auto.send_keys(web,"//input[@id='txtpwd']","396968")
    time.sleep(15)
    auto.click_btn(web,"//button[1]")
    auto.click_btn(web,"//a[@href='/BTS/billdetails.action']")
    auto.selectkey(web,"//select[@id='div_code']","IBP")
    auto.selectkey(web,"//select[@id='comp_code']","Indian Oil Corp-IBP Div")
    auto.send_keys(web,"//input[@id='gstin_number']","GST")
    auto.send_keys(web,"//input[@id='po_number']",data['BSTNK'])
    auto.send_keys(web,"//input[@id='bill_no']",data['XBLNR'])
    auto.click_btn(web,"//input[@id='bill_date']")
    auto.click_btn(web,"//a[contains(text(),'"+data['FKDAT'][-2:]+"')]")
    auto.send_keys(web,"//input[@id='bill_amt']",data['WRBTR'])
    auto.send_keys(web,"//textarea[@id='comments']","This is a test comments")
    auto.click_btn(web,"//input[@name='checkMe']")
    auto.click_btn(web,"//input[@name='checkAcc']")
