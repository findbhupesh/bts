import time
from easygui import msgbox
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support    import expected_conditions as EC
from lib                           import auto

def upld_inv(web,data):
    wait = WebDriverWait(web, 10)
    web.get("https://bills.hpcl.co.in/Vendor/index.jsp")
    auto.send_keys(web,"//input[@id='username']","28084998")
    auto.send_keys(web,"//input[@id='password']","balhpcl@18")
    time.sleep(15)
    auto.click_btn(web,"//input[@id='submit1']")

    auto.click_btn(web,"//button[contains(text(),'Continue')]")
    auto.click_btn(web,"//button[contains(text(),'Continue')]")
    win1 = web.current_window_handle
    auto.click_btn(web,"//a[contains(text(),'e-Invoice')]")
    auto.click_btn(web,"//a[@href='create_tx.jsp']")
    
    wait.until(EC.number_of_windows_to_be(2))
    for window_handle in web.window_handles:
        if window_handle != win1:
            web.switch_to.window(window_handle)
            break
  
    auto.click_btn(web,"//span[contains(@title,'Select Purchase Order')]")
    auto.send_keys(web,"//input[@class='select2-search__field']",data['BSTNK'][:8])
    auto.click_btn(web,"//li[contains(@id,'"+data['BSTNK'][:8]+"')]")
    auto.send_keys(web,"//input[@id='bill_no']",data['XBLNR'])
    auto.click_btn(web,"//input[@id='bill_dt']")
    auto.click_btn(web,"//a[contains(text(),'"+data['FKDAT'][-2:]+"')]")
    auto.send_keys(web,"//input[@id='taxable_amt']",data['NETWR'])
    auto.send_keys(web,"//input[@id='tax_amt']",data['MWSBK'])
    auto.send_keys(web,"//input[@id='bill_amt']",data['WRBTR'])
    auto.click_btn(web,"//span[@id='select2-locnnm-container']")
    auto.send_keys(web,"//input[@class='select2-search__field']",data['ABLAD'])
    auto.click_btn(web,"//li[contains(text(),'"+data['ABLAD']+"')]")
    auto.click_btn(web,"//span[@id='select2-creator_mail-container']")
    auto.click_btn(web,"//li[contains(@id,'"+data['ANRED']+"')]")
    auto.send_keys(web,"//input[@id='scan_page']",data['ZCOPY'])
    auto.send_keys(web,"//input[@id='challan_no']",data['CHNUM'])
    auto.send_keys(web,"//input[@id='digitalInvoiceFile']",data['XFILE'])
    auto.send_keys(web,"//textarea[@id='creator_rem']","This is test remark")
    auto.click_btn(web,"//input[@id='chkk']")
    auto.click_btn(web,"//input[@value='check']")
    #auto.click_btn(web,"//input[@id='submit2']")