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
        inst.bill_rep(data)
    case 'HPCL':
        data["test"] = pswd['HPCL']['tst']
        inst = hpcl(cweb)
        inst.do_login(pswd['HPCL'])
        btsno = inst.upld_inv(data)
        file_name = 'out/'+data['VBUND']+'_'+data['VBELN']+'_'+data['XBLNR']+'.txt'
        with open(file_name,'w') as outp:
            outp.write(btsno)
        
    case 'IOCL':
        data["test"] = pswd['IOCL']['tst']
        inst = iocl(cweb)
        inst.do_login(pswd['IOCL'])
        inst.upld_inv(data)
        btsno = inst.bill_rep(data)
        file_name = 'out/'+data['VBUND']+'_'+data['VBELN']+'_'+data['XBLNR']+'.txt'
        with open(file_name,'w') as outp:
            outp.write(btsno)
        data['BTSNO'] = btsno
        inst.prnt_inv(data)

#time.sleep(20)
#cweb.con.quit()
