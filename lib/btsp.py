import time,calendar
from selenium.webdriver.support.wait    import WebDriverWait
from selenium.webdriver.support         import expected_conditions as EC

class bpcl:
    def __init__(self,web):
        self.web = web
        self.con = web.con

    def do_login(self,data):
        self.con.get("https://econnect.bpcl.in/selfservice-ext/pub/login.html")
        self.web.send_keys(xpath="//input[@id='principal']",param="VC157213")
        self.web.send_keys(xpath="//input[@id='input_password']",param="Baldist@2223")
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
        self.web.click_btn(xpath="//input[@id='InvoiceDate']")
        self.web.click_btn(xpath="//a[contains(text(),'"+data['FKDAT'][-2:]+"')]")
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
        self.con.get("https://bills.hpcl.co.in/Vendor/index.jsp")
        self.web.send_keys(xpath="//input[@id='username']",param="28084998")
        self.web.send_keys(xpath="//input[@id='password']",param="balhpcl@18")
        time.sleep(15)
        self.web.click_btn(xpath="//input[@id='submit1']")

    def upld_inv(self,data):
        self.con.get("https://bills.hpcl.co.in/Vendor/create_tx.jsp")
        self.web.click_btn(xpath="//span[contains(@title,'Select Purchase Order')]")
        self.web.send_keys(xpath="//input[@class='select2-search__field']",param=data['BSTNK'][:8])
        self.web.click_btn(xpath="//li[contains(@id,'"+data['BSTNK'][:8]+"')]")
        self.web.send_keys(xpath="//input[@id='bill_no']",param=data['XBLNR'])
        self.web.click_btn(xpath="//input[@id='bill_dt']")
        ccyr = data['FKDAT'][0:4].lstrip('0')
        imon = int(data['FKDAT'][5:7])
        cday = data['FKDAT'][8:10].lstrip('0')
        cmon = calendar.month_abbr[imon]
        self.web.selectkey(xpath="//select[@class='ui-datepicker-month']",param=cmon)
        self.web.selectkey(xpath="//select[@class='ui-datepicker-year']",param=ccyr)
        self.web.click_btn(xpath="//a[contains(text(),'"+cday+"')]")
        self.web.send_keys(xpath="//input[@id='taxable_amt']",param=data['NETWR'])
        self.web.send_keys(xpath="//input[@id='tax_amt']",param=data['MWSBK'])
        self.web.send_keys(xpath="//input[@id='bill_amt']",param=data['WRBTR'])
        self.web.click_btn(xpath="//input[@id='changeDefaultDisloc']")
        self.web.click_btn(xpath="//span[@id='select2-locnnm-container']")
        self.web.send_keys(xpath="//input[@class='select2-search__field']",param=data['ABLAD'])
        self.web.click_btn(xpath="//li[contains(text(),'"+data['ABLAD']+"')]")
        self.web.click_btn(xpath="//span[@id='select2-creator_mail-container']")
        self.web.click_btn(xpath="//li[contains(@id,'"+data['SPNAM']+"')]")
        self.web.send_keys(xpath="//input[@id='scan_page']",param=data['ZCOPY'])
        self.web.send_keys(xpath="//input[@id='challan_no']",param=data['CHNUM'])
        self.web.send_keys(xpath="//input[@id='digitalInvoiceFile']",param=data['XFILE'])
        self.web.send_keys(xpath="//textarea[@id='creator_rem']",param="This is test remark")
        self.web.click_btn(xpath="//input[@id='chkk']")
        self.web.click_btn(xpath="//input[@value='check']")
        #self.web.click_btn("//input[@id='submit2']")

    def prnt_inv(self,data):
        wait = WebDriverWait(self.con, 10)
        self.con.get("https://bills.hpcl.co.in/Vendor/mytxreport.jsp")
        i = self.web.get_colno(xpath="//table[@id='AutoNumber1']",param="Invoice No.")
        j = self.web.get_rowno(xpath="//table[@id='AutoNumber1']",param=data['XBLNR'],colno=i)
        i = self.web.get_colno(xpath="//table[@id='AutoNumber1']",param="Print")
        self.web.click_btn(xpath="//tbody/tr["+str(j)+"]/td["+str(i)+"]/a[1]/img[1]")
        wait.until(EC.number_of_windows_to_be(2))
        wndw = self.con.window_handles[1]
        self.con.switch_to.window(wndw)
        file_name = 'out/'+data['VBUND']+'_BTSPRINT_'+data['XBLNR']+'.pdf'
        self.web.webpg_pdf(param=file_name)
        self.web.print_pdf(param=file_name)
                 
class iocl():
    def __init__(self,web):
        self.web = web
        self.con = web.con

    def do_login(self,data):
        self.con.get("https://associates.indianoil.co.in/BTS/vendor_login")
        self.web.send_keys(xpath="//input[@id='txtuserid']",param="11921208")
        self.web.send_keys(xpath="//input[@id='txtpwd']",param="396968")
        time.sleep(15)
        self.web.click_btn(xpath="//button[1]")
        self.web.click_btn(xpath="//a[@href='/BTS/billdetails.action']")

    def upld_inv(self,data):
        self.web.selectkey(xpath="//select[@id='div_code']",param="IBP")
        self.web.selectkey(xpath="//select[@id='comp_code']",param="Indian Oil Corp-IBP Div")
        self.web.send_keys(xpath="//input[@id='gstin_number']",param=data["gstin"])
        self.web.send_keys(xpath="//input[@id='po_number']",param=data['BSTNK'])
        self.web.send_keys(xpath="//input[@id='bill_no']",param=data['XBLNR'])
        self.web.click_btn(xpath="//input[@id='bill_date']")
        self.web.click_btn(xpath="//a[contains(text(),'"+data['FKDAT'][-2:]+"')]")
        self.web.send_keys(xpath="//input[@id='bill_amt']",param=data['WRBTR'])
        self.web.send_keys(xpath="//textarea[@id='comments']",param="This is a test comments")
        self.web.click_btn(xpath="//input[@name='checkMe']")
        self.web.click_btn(xpath="//input[@name='checkAcc']")