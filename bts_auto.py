import sys,time,json,os
from selenium                           import webdriver
from selenium.webdriver.support.wait    import WebDriverWait
from lib.auto                           import web
from lib.btsp                           import bpcl,hpcl,iocl

files = os.listdir("inp/")
inp_file = sys.argv[1]+'.json'
for file in files:
    if inp_file in file:
        json_file = file

cfg_file = 'cfg/pass.json'
file = open(cfg_file)
pswd = json.load(file)

cweb = web()
cweb.con.implicitly_wait(15)
file = open('inp/'+json_file)
data = json.load(file)
url_code = data['VBUND']

match url_code:
    case 'BPCL':
        data["test"] = pswd['BPCL']['tst']
        inst = bpcl(cweb)
        inst.do_login(pswd['BPCL'])
        inst.upld_inv(data)
    case 'HPCL':
        data["test"] = pswd['HPCL']['tst']
        inst = hpcl(cweb)
        inst.do_login(pswd['HPCL'])
        inst.upld_inv(data)
        inst.prnt_inv(data)
        
    case 'IOCL':
        data["test"] = pswd['IOCL']['tst']
        inst = iocl(cweb)
        inst.do_login(pswd['IOCL'])
        btsno = inst.upld_inv(data)
        data['BTSNO'] = btsno
        inst.prnt_inv(data)

time.sleep(5)
cweb.con.quit()
