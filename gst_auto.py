import sys,time,json,os
from selenium                           import webdriver
from selenium.webdriver.support.wait    import WebDriverWait
from lib.auto                           import web
from lib.gstin                          import gstin

data = {}
cweb = web()
cweb.con.implicitly_wait(15)
inst = gstin(cweb)
if len(sys.argv) > 1:
    data['param'] = sys.argv[1]
else:
    print("Error : Please provide HSNno as argument ")
    exit()
inst.search_hsn(data)
# inst.find_chapt(data)
#time.sleep(5)
#cweb.con.quit()