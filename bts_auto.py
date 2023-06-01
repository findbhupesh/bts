import sys,time,json,os
from selenium                           import webdriver
from selenium.webdriver.support.wait    import WebDriverWait
from lib.auto                           import web
from lib.btsp                           import bpcl,hpcl,iocl

files = os.listdir("files/")
inp_file = sys.argv[1]+'.json'
for file in files:
    if inp_file in file:
        json_file = file

cweb = web()
cweb.con.implicitly_wait(15)
file = open('files/'+json_file)
data = json.load(file)
url_code = data['VBUND']

match url_code:
    case 'BPCL':
        inst = bpcl(cweb)
        inst.do_login(data)
        inst.upld_inv(data)
    case 'HPCL':
        inst = hpcl(cweb)
        inst.do_login(data)
        inst.upld_inv(data)
        inst.prnt_inv(data)
        
    case 'IOCL':
        inst = iocl(cweb)
        inst.do_login(data)
        inst.upld_inv(data)

# time.sleep(10)
# web.close()
# web.quit()