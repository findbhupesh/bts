from datetime                                     import datetime
from selenium                                     import webdriver
from twocaptcha                                   import TwoCaptcha
from selenium.webdriver.common.by                 import By
from selenium.webdriver.support.ui                import Select
from selenium.webdriver.support.wait              import WebDriverWait
from selenium.webdriver.support                   import expected_conditions as EC
from selenium.webdriver.common.print_page_options import PrintOptions

import os,sys,base64,calendar,easyocr
class web:
    def __init__(self):
        prefs = {"download.default_directory":"C:\\SAP\\bts\\out\\"}
        option = webdriver.ChromeOptions()    
        option.add_experimental_option("prefs", prefs)
        option.add_experimental_option("detach",True)
    #    option.add_argument('--headless')
        option.add_argument('log-level=3')
        option.add_argument("--start-maximized")
        option.add_extension("cfg\\chropath_6_1_12_0.crx")
        self.con = webdriver.Chrome(options=option)

    def click_btn(self,*args, **kwargs):
        wait = WebDriverWait(self.con,10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, kwargs['xpath'])))
        try:
            element.click()
        except Exception as e:
            print(str(e))

    def send_keys(self,*args, **kwargs):
        try:
            self.con.find_element(By.XPATH,kwargs['xpath']).send_keys(kwargs['param'])
        except:
            pass

    def selectkey(self,*args, **kwargs):
        combob = Select(self.con.find_element(By.XPATH,kwargs['xpath']))
        combob.select_by_visible_text(kwargs['param'])

    def get_colno(self,*args, **kwargs):
        table = self.con.find_element(By.XPATH,kwargs['xpath'])
        tcols = table.find_elements(By.XPATH,'.//th')

        for i in range(len(tcols)):
            if kwargs['param'] in tcols[i].text:
                return i + 1

    def get_rowno(self,*args, **kwargs):
        table = self.con.find_element(By.XPATH,kwargs['xpath'])
        cells = table.find_elements(By.XPATH,".//tr/td["+str(kwargs['colno'])+"]")
        for i in range(len(cells)):
            if kwargs['param'] in cells[i].text:
                return i + 2
            
    def save_image(self,*args, **kwargs):
        if 'param' in kwargs:
            self.con.save_screenshot(kwargs['param'])
        else:
            print("Filename not given")
    def save_shot(self,*args, **kwargs):
        self.con.find_element(By.XPATH,kwargs['xpath']).screenshot("inp/captcha.png")

    def webpg_pdf(self,*args, **kwargs):
        print_options = PrintOptions()
        print_options.page_height = 29.70
        print_options.page_width  = 21.00
        print_options.scale       = 00.85
        print_options.orientation = 'portrait'
        print_options.shrink_to_fit = True
        pdf = self.con.print_page(print_options=print_options)
        with open(kwargs['param'], "wb") as f:
            f.write(base64.b64decode(pdf))
            
    def print_pdf(self,*args, **kwargs):
        os.system('.\\bin\\PDFtoPrinter.exe '+kwargs['param'])

    def read_text(self,*args, **kwargs):
        value = ''
        if 'xpath' in kwargs:
            try:
                value = self.con.find_element(By.XPATH,kwargs['xpath']).text
            except:
                pass
        if 'elmnt' in kwargs:
            try:
                value = kwargs['elmnt'].text
            except:
                pass

        return value
    
    def acc_alert(self,*args, **kwargs):
        try :
            self.con.switch_to.alert.accept()
        except:
            pass

    def get_docno(self,*args, **kwargs):
        doc_no = ''
        for word in kwargs['param']:
            if word.isdigit():
                doc_no = word
                break
        return doc_no
    def list_elmt(self,*args, **kwargs):
        elmts = None
        try:
            elmts = self.con.find_elements(By.XPATH,kwargs['xpath'])
        except:
            pass
        return elmts
     
              
    def set_caldt(self,*args, **kwargs):
        wait = WebDriverWait(self.con,10)
        self.click_btn(xpath=kwargs['xpath'])
        wait.until(EC.visibility_of_element_located((By.XPATH,"//div[@id='ui-datepicker-div']")))
        edate = kwargs['param']
        fdate = datetime.strptime(edate,"%Y-%m-%d")
        edate = str(fdate.day)
        emnth = int(fdate.month)
        cmnth = calendar.month_abbr[emnth]
        eyear = int(fdate.year)
        match kwargs['ctype']:
            case "1":
                smnth = self.read_text(xpath="//span[@class='ui-datepicker-month']")
                smnth = datetime.strptime(smnth, '%B').month
                syear = self.read_text(xpath="//span[@class='ui-datepicker-year']")
                syear = int(syear)

                if syear > eyear or smnth > emnth:
                    self.click_btn(xpath="//span[contains(text(),'Prev')]")
                    smnth = self.read_text(xpath="//span[@class='ui-datepicker-month']")
                    smnth = datetime.strptime(smnth, '%B').month
                    syear = self.read_text(xpath="//span[@class='ui-datepicker-year']")
                    syear = int(syear)

                if syear < eyear or smnth < emnth:
                    self.click_btn(xpath="//span[contains(text(),'Next')]")
                    smnth = self.read_text(xpath="//span[@class='ui-datepicker-month']")
                    smnth = datetime.strptime(smnth, '%B').month
                    syear = int(self.read_text(xpath="//span[@class='ui-datepicker-year']"))
                self.click_btn(xpath="//a[contains(text(),'"+edate+"')]")
            case "2":
                pass
            case "3":
                pass
            case "4":
                self.selectkey(xpath="//select[@class='ui-datepicker-month']",param=cmnth)
                self.selectkey(xpath="//select[@class='ui-datepicker-year']",param=str(eyear))
                self.click_btn(xpath="//td/a[contains(text(),'"+edate+"')]")
            case "5":
                pass
            case "6":
                pass

    def read_cell(self,*args, **kwargs):
        xdata = kwargs['param']
        tcols = self.con.find_elements(By.XPATH,kwargs['xpath']+'//th')
        colno = 0
        for i in range(len(tcols)):
            index = i + 1
            if xdata['valcol'] in tcols[i].text:
                colno = index
                break
        if colno > 0:
           #print("Search Column : "+ str(colno))
            rows = self.con.find_elements(By.XPATH,kwargs['xpath']+"//tbody/tr")
        else:
            return
        rowno = 0
        for i in range(len(rows)):
            index = i + 1
            value = self.read_text(xpath="//tbody/tr["+str(index)+"]/td["+str(colno)+"]")
            if xdata['svalue'] in value:
                rowno = index
                break
        #print("Row Number : "+ str(rowno))
        colno = 0
        for i in range(len(tcols)):
            index = i + 1
            if xdata['srccol'] in tcols[i].text:
                colno = index
                break
        #print("Found Column : "+ str(colno))
        match xdata['action']:
            case "click":
                self.click_btn(xpath="//tbody/tr["+str(rowno)+"]/td["+str(colno)+"]/a[1]/img[1]")
            case "text":
                return self.read_text(xpath=kwargs['xpath']+"/tbody/tr["+str(rowno)+"]/td["+str(colno)+"]")
    def read_attr(self,*args, **kwargs):
        elmt = self.con.find_element(By.XPATH,kwargs['xpath'])
        return elmt.get_attribute(kwargs['attr'])
    
    def read_capt(self,*args, **kwargs):
        solver = TwoCaptcha('94c83e9b7f077c2fa8111d883a914f27')
        try:
            result = solver.normal(kwargs['param'])
        except Exception as e:
            sys.exit(e)
        else:
            print(result)
           #sys.exit('solved: ' + str(result))
        return result["code"]    

    def read_tocr(self, *args, **kwargs):
        reader = easyocr.Reader(['en'])
        result = reader.readtext(kwargs['param'], detail = 0)
        print(result)
        return result[0]
