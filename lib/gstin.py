import time,calendar,json,logging as log
import requests
from datetime                           import datetime,date,timedelta
from selenium.webdriver.support.wait    import WebDriverWait
from selenium.webdriver.support         import expected_conditions as EC

class gstin:
    def __init__(self,web):
        self.web = web
        self.con = web.con
    def launch_url(self,data):
        self.con.get('https://cleartax.in/s/chapter-1-live-animal-products-gst-rate-hsn-code')
        
    def find_chapt(self,data):
        xpath = "//a[contains(@href,'"+data['param']+"')]"
        self.web.click_btn(xpath=xpath)
        item = ''
        list = ''
        elmts = self.web.list_elmt(xpath="//table/tbody/tr/th")
        for i in range(len(elmts)):
            item += '"'+self.web.read_text(elmnt = elmts[i]) + '",'

        list += item +'\n'
        elmts = self.web.list_elmt(xpath="//table/tbody/tr")
        for i in range(len(elmts)):
            chlds = self.web.list_elmt(xpath="//table/tbody/tr["+str(i+1)+"]/td")
            item = ''
            for j in range(len(chlds)):
                item += '"'+self.web.read_text(elmnt = chlds[j]) + '",'
            list += item +'\n'
        with open('out/hsn_rates.csv','w') as out:
            out.write(list)
    
    def search_hsn(self,data):
        self.con.get('https://cleartax.in/s/gst-hsn-lookup')
        self.web.send_keys(xpath="//input[@id='input']",param=data['param'])
        self.web.click_btn(xpath="//button[text()='Search']")
        time.sleep(5)
        names = self.web.list_elmt(xpath='//table/thead/tr/th')
        head = ['chapter','hsndesc','hsncode','hsnrate','cesrate','effdate','revdate']
        rows = self.web.list_elmt(xpath='//table/tbody/tr')
        list = []
        for i in range(len(rows)):
            item = {}
            for j in range(len(head)):
                if i == 0:
                    item[head[j]] = self.web.read_text(xpath="//table/tbody/tr["+str(i+1)+"]/td["+str(j+1)+"]")
                else:

                    if j == 0:
                        item[head[j]] = self.web.read_text(xpath="//table/tbody/tr[1]/td["+str(j+1)+"]")
                    else:
                        item[head[j]] = self.web.read_text(xpath="//table/tbody/tr["+str(i+1)+"]/td["+str(j)+"]")

            list.append(item)
        strData = json.dumps(list)
        file_name = 'out/hsn_rate_'+data['param']+'.json'
        with open(file_name,'w') as out_file:
            out_file.write(strData)