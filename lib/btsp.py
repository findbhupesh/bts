import time,calendar,logging as log
from datetime                           import datetime,date,timedelta
from selenium.webdriver.support.wait    import WebDriverWait
from selenium.webdriver.support         import expected_conditions as EC
log.basicConfig(filename='out/logging.log', encoding='utf-8', level=log.DEBUG, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
class bpcl:
    def __init__(self,web):
        self.web = web
        self.con = web.con
        log.info("Class bpcl initiated")

    def do_login(self,data):
        self.con.get(data['url'])
        self.web.send_keys(xpath="//input[@id='principal']",param=data['usr'])
        self.web.send_keys(xpath="//input[@id='input_password']",param=data['pwd'])
        time.sleep(15)
        self.web.click_btn(xpath="//input[@value='Login']")
        
    def upld_inv(self,data):
        wait = WebDriverWait(self.con, 10)
        self.web.click_btn(xpath="//div[text()='My Applications']")
        self.web.click_btn(xpath="//a[text()='Digital Invoice Management']")
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

class hpcl:
    def __init__(self,web):
        self.web = web
        self.con = web.con

    def do_login(self,data):
        wait = WebDriverWait(self.con, 10)
        self.con.get(data['url'])
        self.web.send_keys(xpath="//input[@id='username']",param=data['usr'])
        self.web.send_keys(xpath="//input[@id='password']",param=data['pwd'])
        time.sleep(15)
        self.web.click_btn(xpath="//input[@id='submit1']")

    def upld_inv(self,data):
        self.con.get("https://bills.hpcl.co.in/Vendor/create_tx.jsp")
        self.web.click_btn(xpath="//span[contains(@title,'Select Purchase Order')]")
        self.web.send_keys(xpath="//input[@class='select2-search__field']",param=data['BSTNK'][:8])
        self.web.click_btn(xpath="//li[contains(@id,'"+data['BSTNK'][:8]+"')]")
        self.web.send_keys(xpath="//input[@id='bill_no']",param=data['XBLNR'])
        self.web.set_caldt(xpath="//input[@id='bill_dt']",param=data['FKDAT'], ctype = "4")
        self.web.send_keys(xpath="//input[@id='taxable_amt']",param=data['NETWR'])
        self.web.send_keys(xpath="//input[@id='tax_amt']",param=data['MWSBK'])
        self.web.send_keys(xpath="//input[@id='bill_amt']",param=data['WRBTR'])
        self.web.click_btn(xpath="//span[@id='select2-locnnm-container']")
        self.web.send_keys(xpath="//input[@class='select2-search__field']",param=data['ABLAD'])
        self.web.click_btn(xpath="//li[contains(text(),'"+data['ABLAD']+"')]")
        self.web.click_btn(xpath="//span[@id='select2-creator_mail-container']")
        self.web.click_btn(xpath="//li[contains(@id,'"+data['SPNAM']+"')]")
        self.web.send_keys(xpath="//input[@id='scan_page']",param=data['ZCOPY'])
        self.web.send_keys(xpath="//input[@id='challan_no']",param=data['CHNUM'])
        self.web.send_keys(xpath="//input[@id='digitalInvoiceFile']",param=data['XFILE'])
        self.web.send_keys(xpath="//textarea[@id='creator_rem']",param=data['REMRK'])
        self.web.click_btn(xpath="//input[@id='changeDefaultDisloc']")
        self.web.click_btn(xpath="//input[@id='chkk']")
        self.web.click_btn(xpath="//input[@value='check']")
        #self.web.click_btn("//input[@id='submit2']")

    def prnt_inv(self,data):
        wait = WebDriverWait(self.con, 10)
        self.con.get("https://bills.hpcl.co.in/Vendor/mytxreport.jsp")
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
        #self.web.print_pdf(param=file_name)
                 
class iocl():
    def __init__(self,web):
        self.web = web
        self.con = web.con

    def do_login(self,data):
        self.con.get(data['url'])
        self.web.send_keys(xpath="//input[@id='txtuserid']",param=data['usr'])
        self.web.send_keys(xpath="//input[@id='txtpwd']",param=data['pwd'])
        time.sleep(15)
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

    def prnt_inv(self,data):
        wait = WebDriverWait(self.con, 10)
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
        value = value[0:22]
        print(value)
        self.web.click_btn(xpath="//b[contains(text(),'Print Bill Entry Details')]")
        self.web.send_keys(xpath="//input[@id='bill_entry_no']",param=value)
        self.web.click_btn(xpath="//input[@value='DISPLAY PDF']")
        wait.until(EC.number_of_windows_to_be(2))
        wndw = self.con.window_handles[1]
        self.con.switch_to.window(wndw)
        self.con.close()
        file_name = 'out/'+value+'.pdf'
        self.web.print_pdf(param=file_name)