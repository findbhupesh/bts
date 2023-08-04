import sys,time,calendar,logging as log
from datetime                           import datetime,date,timedelta
from selenium.webdriver.support.wait    import WebDriverWait
from selenium.webdriver.support         import expected_conditions as EC

log.basicConfig(filename='out/logging.log', encoding='utf-8', level=log.DEBUG, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
class bpcl:
    def __init__(self,web):
        self.web = web
        self.con = web.con

    def do_login(self,data):
        self.con.get(data['url'])
        self.web.send_keys(xpath="//input[@id='principal']",param=data['usr'])
        self.web.send_keys(xpath="//input[@id='input_password']",param=data['pwd'])
        self.web.save_shot(xpath="//img[@id='captcha']")
        code = self.web.read_capt(param="inp/captcha.png").upper()
        print(code)
        self.web.send_keys(xpath="//input[@id='captcha']",param=code)
        self.web.click_btn(xpath="//input[@value='Login']")
        
    def upld_inv(self,data):
        wait = WebDriverWait(self.con, 10)
        self.web.click_btn(xpath="//div[text()='My Applications']")
        time.sleep(2)
        self.web.click_btn(xpath="//a[contains(text(),'Digital Invoice Management')]")
        wait.until(EC.number_of_windows_to_be(2))
        wndw = self.con.window_handles[1]
        self.con.switch_to.window(wndw)
        self.web.send_keys(xpath="//input[@id='PONumber']",param=data['BSTNK'])
        self.web.send_keys(xpath="//input[@id='InvoiceRefNo']",param=data['XBLNR'])
        self.web.set_caldt(xpath="//input[@id='InvoiceDate']",param=data['FKDAT'], ctype = "4")
        self.web.send_keys(xpath="//input[@id='InvoiceAmount']",param=data['WRBTR'])
        self.web.click_btn(xpath="//input[@id='PONumber']")
        self.web.click_btn(xpath="//button[contains(text(),'Proceed')]")
        self.web.send_keys(xpath="//input[@id='chooseFile']",param=data['XFILE'])
        self.web.click_btn(xpath="//input[@id='deliveryCheckBox']")
        if not data['test']:
            self.web.click_btn(xpath="//button[text()='Submit']")
            
        
    def bill_rep(self,data):
        wait = WebDriverWait(self.con, 10)
        time.sleep(5)
        self.web.click_btn(xpath="//div[text()='Report']")
        self.web.click_btn(xpath="//a[text()='Vendor Invoice Status']")
        wait.until(EC.number_of_windows_to_be(2))
        wndw = self.con.window_handles[1]
        self.con.switch_to.window(wndw)
        self.web.click_btn(xpath="//input[@value='My Invoice']")
        self.web.send_keys(xpath="//input[@id='txtInvoiceRegNumber']",param=data['XBLNR'])
        self.web.click_btn(xpath="//input[@id='btnSubmit']")
        docno = self.web.read_text(xpath="(//tbody/tr[1]/td[1])[1]")
        print(docno)
        file_name = 'out/'+data['VBUND']+'_'+data['VBELN']+'_'+data['XBLNR']+'.txt'
        with open(file_name,'w') as outp:
            outp.write(docno)
            
class hpcl:
    def __init__(self,web):
        self.web = web
        self.con = web.con

    def do_login(self,data):
        self.con.get(data['url'])
        self.web.click_btn(xpath="//a[contains(text(),'click here to Login')]")
        self.web.send_keys(xpath="//input[@id='empno']",param=data['usr'])
        self.web.send_keys(xpath="//input[@id='password']",param=data['pwd'])
        self.web.click_btn(xpath="//button[@id='submitBtn']")

    def upld_inv(self,data):
        self.con.get("https://vss.hpcl.co.in/vss/billsubmission")
        self.web.send_keys(xpath="//input[@id='poNumberSearch']",param=data['BSTNK'][:10])
        time.sleep(2)
        self.web.click_btn(xpath="//ul[@id='ui-id-1']/li[1]/div[1]")
        time.sleep(2)
        self.web.selectkey(xpath="//select[@id='typeOfInvoice']",param=data["INVTY"],option='value')
        self.web.send_keys(xpath="//input[@id='fileupload']",param=data['XFILE'])
        self.web.click_btn(xpath="//select[@id='receivingPlant']")
        self.web.selectkey(xpath="//select[@id='receivingPlant']",param=data['ABLAD'],option='vtext')
        self.web.click_btn(xpath="//select[@id='paymentAccountNo']")    
        self.web.selectkey(xpath="//select[@id='paymentAccountNo']",param=1, option='index')        
        if not data['test']:
            self.web.click_btn("//input[@id='submitInvoice']")

    def prnt_inv(self,data):
        wait = WebDriverWait(self.con, 10)
        self.con.get("https://vss.hpcl.co.in/vss/submittedbills")
        param = {}
        param["valcol"] = "Invoice No."
        param["svalue"] = data['XBLNR']
        param["srccol"] = "Print"
        param['action'] = "click"
        self.web.read_cell(xpath="//table[@id='AutoNumber1']",param=param)
        wait.until(EC.number_of_windows_to_be(2))
        wndw = self.con.window_handles[1]
        self.con.switch_to.window(wndw)
        file_name = 'out/'+data['VBUND']+'_BTSPRINT_'+data['XBLNR']+'.pdf'
        self.web.webpg_pdf(param=file_name)
        self.web.print_pdf(param=file_name)
    def save_bts(self,data):
        btsno = ''
        file_name = 'out/'+data['VBUND']+'_'+data['VBELN']+'_'+data['XBLNR']+'.txt'
        with open(file_name,'w') as outp:
            outp.write(btsno)

                 
class iocl():
    def __init__(self,web):
        self.web = web
        self.con = web.con

    def do_login(self,data):
        self.con.get(data['url'])
        self.web.send_keys(xpath="//input[@id='txtuserid']",param=data['usr'])
        self.web.send_keys(xpath="//input[@id='txtpwd']",param=data['pwd'])
        self.web.save_shot(xpath="//img[@id='captchaImage']")
        text = self.web.read_tocr(param="inp/captcha.png")
        code = self.web.read_capt(param="inp/captcha.png")
        data = ""
        for x in code:
            if 'Alphabets' in text:
                if x.isalpha():
                    data = data + x
            else:
                if x.isdigit():
                    data = data + x
        print(data)
        self.web.send_keys(xpath="//input[@id='captcha']",param=data)
        time.sleep(5)
        self.web.click_btn(xpath="//button[1]")
        

    def upld_inv(self,data):
        self.web.click_btn(xpath="//a[@href='/BTS/billdetails.action']")
        self.web.selectkey(xpath="//select[@id='div_code']",param=data["SPNAM"])
        self.web.selectkey(xpath="//select[@id='comp_code']",param=data["ABLAD"])
        self.web.send_keys(xpath="//input[@id='gstin_number']",param=data['GSTIN'])
        self.web.send_keys(xpath="//input[@id='po_number']",param=data['BSTNK'])
        self.web.send_keys(xpath="//input[@id='bill_no']",param=data['XBLNR'])
        self.web.set_caldt(xpath="//input[@id='bill_date']",param=data['FKDAT'], ctype="1")
        self.web.send_keys(xpath="//input[@id='bill_amt']",param=data['WRBTR'])
        self.web.send_keys(xpath="//textarea[@id='comments']",param=data['REMRK'])
        self.web.click_btn(xpath="//input[@name='checkMe']")
        self.web.click_btn(xpath="//input[@name='checkAcc']")
        if not data['test']:
            self.web.click_btn(xpath="//input[@id='submitbutton']")
            message = self.web.read_text(xpath="//span[contains(text(),'Details saved successfully')]") 
            self.web.click_btn(xpath="//span[text()='Okay']")
            return self.web.get_docno(param=message)
    
    def bill_rep(self,data):
        self.web.click_btn(xpath="//b[contains(text(),'Period Wise Report')]") 
        st_date = datetime.strptime(data['FKDAT'],"%Y-%m-%d")
        en_date = st_date + timedelta(days=5)
        en_date = en_date.date()
        cu_date = date.today()
        if en_date > cu_date:
            en_date = cu_date

        self.web.set_caldt(xpath="//input[@id='fromDate']",param=data['FKDAT'], ctype = "1")
        self.web.set_caldt(xpath="//input[@id='toDate']",  param=str(en_date), ctype = "1")
        self.web.click_btn(xpath="//input[@value='View Bills']")
        param = {}
        param["valcol"] = "Bill No. & Date"
        param["svalue"] = data['XBLNR']
        param["srccol"] = "Bill Entry No. & Date"
        param['action'] = "text"
        value = self.web.read_cell(xpath="//table[2]",param=param)
        value = value[0:22].rstrip()
        return value

    def prnt_inv(self,data):
        wait = WebDriverWait(self.con, 10)
        btsno = ''
        if data['BTSNO'] == None:
            btsno = self.bill_rep(data)
        else:
            btsno = data['BTSNO']

        self.web.click_btn(xpath="//b[contains(text(),'Print Bill Entry Details')]")
        self.web.send_keys(xpath="//input[@id='bill_entry_no']",param=btsno)    
        self.web.click_btn(xpath="//input[@value='DISPLAY PDF']")
        wait.until(EC.number_of_windows_to_be(2))
        wndw = self.con.window_handles[1]
        self.con.switch_to.window(wndw)
        time.sleep(2)
        self.con.close()
        file_name = 'out/'+btsno+'.pdf'
        self.web.print_pdf(param=file_name)
