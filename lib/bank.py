import sys,time,calendar,logging as log
from datetime                           import datetime,date,timedelta
from selenium.webdriver.support.wait    import WebDriverWait
from selenium.webdriver.support         import expected_conditions as EC
from selenium.webdriver.common.alert    import Alert

log.basicConfig(filename='out/logging.log', encoding='utf-8', level=log.DEBUG, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

class scbl:
    def __init__(self,web):
        self.web = web
        self.con = web.con
        
    def do_login(self,data):
        
        wait = WebDriverWait(self.con, 10)
        self.con.get(data['url'])
        self.web.click_btn(xpath="//a[@class='close_overlay']")
        self.web.click_btn(xpath="//a[@id='btnEbanking']")
        wait.until(EC.number_of_windows_to_be(2))
        wndw = self.con.window_handles[1]
        self.con.switch_to.window(wndw)
        self.web.send_keys(xpath="//input[@id='AuthenticationFG.USER_PRINCIPAL']",param=data['usr'])
        self.web.send_keys(xpath="//input[@id='AuthenticationFG.ACCESS_CODE']",param=data['pwd'])
        self.web.save_shot(xpath="//img[@id='IMAGECAPTCHA']")
        code = self.web.read_capt(param="inp/captcha.png").upper()
        print('code :',code)
        self.web.send_keys(xpath="//input[@id='AuthenticationFG.VERIFICATION_CODE']",param=code)
        self.web.click_btn(xpath="//input[@id='VALIDATE_CREDENTIALS' and @value='LOGIN']")
    
    def upld_file(self,data):
        time.sleep(5)
        self.web.click_btn(xpath="(//a[contains(text(),'Upload a File')])[2]")
        self.web.click_btn(xpath="//div[text()='Other Bank upload']")
        self.web.send_keys(xpath="//input[@name='FileUploadCRUDFG.FILE_NAME']",param='Payment File')
        self.web.send_keys(xpath="//input[@name='FileUploadCRUDFG.REMARKS']",param='Sample File')
        self.web.send_keys(xpath="//input[@name='FileUploadCRUDFG.FILE_PATH']",param="C:\\SAP\\bts\\out\\Other_Bank_CIB.txt")
        self.web.click_btn(xpath="//input[@name='Action.UPLOADFILE_CONFIRM']")
        self.web.send_keys(xpath="//input[@name='FileUploadCRUDFG._NEXT_APPROVER_']",param='SOMCHECKER')
        self.web.send_keys(xpath="//input[@name='FileUploadCRUDFG._USER_REMARKS_']",param='For Checking')
    #   self.web.click_btn(xpath="//div[text()='Within Bank upload']")
    