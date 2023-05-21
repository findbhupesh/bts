import sys,time,json,os
from selenium                       import webdriver
from selenium.webdriver.support.ui  import WebDriverWait
from lib                            import bpcl,hpcl,iocl,auto

files = os.listdir("files/")
inp_file = sys.argv[1]+'.json'
for file in files:
    if inp_file in file:
        json_file = file

web = auto.open_browser()
web.implicitly_wait(15)
file = open('files/'+json_file)
data = json.load(file)
url_code = data['VBUND']

match url_code:
    case 'BPCL':
        bpcl.upld_inv(web,data)
    case 'HPCL':
        hpcl.upld_inv(web,data)
    case 'IOCL':
        iocl.upld_inv(web,data)