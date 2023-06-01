from selenium                                     import webdriver
from selenium.webdriver.common.by                 import By
from selenium.webdriver.support.ui                import Select
from selenium.webdriver.support.wait              import WebDriverWait
from selenium.webdriver.support                   import expected_conditions as EC
from pyhtml2pdf                                   import converter
from selenium.webdriver.common.print_page_options import PrintOptions
import os,base64
class web():
    def __init__(self):
        option = webdriver.ChromeOptions()
        option.add_experimental_option("detach",True)
        option.add_argument("--start-maximized")
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
        self.con.save_screenshot("C:\\SAP\\bts\\files\\screenshot0.png")
        
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
        os.system('.\\drivers\\PDFtoPrinter.exe '+kwargs['param'])

