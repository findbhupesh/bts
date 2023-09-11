import sys,time,json,os
from lib.auto                           import web
from lib.bank                           import scbl


cfg_file = 'cfg/bank.json'
file = open(cfg_file)
bank = json.load(file)

cweb = web()
cweb.con.implicitly_wait(15)
data = {}
url_code = 'SCBL'

match url_code:
    case 'SCBL':
        print(bank['SCBL'])
        inst = scbl(cweb)
        inst.do_login(bank['SCBL'])
        inst.upld_file(data)