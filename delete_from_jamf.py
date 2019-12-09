#!/usr/local/bin/python

import requests
import time

# TODO: make api_user and api_pass refer to command line arguments so as not to hard-code them
api_user = 'api_user_here'
api_pass = 'XXXXXXXXXXXXXXXXXXX'
jss_url = 'https://your.jss.url:8443/JSSResource/computers/serialnumber/'

f = open("serials_to_delete.txt","r")
f1 = f.readlines()
for serial in f1:
    computer_url = jss_url+serial
    print(computer_url)
    s=requests.delete(computer_url, auth = (api_user,api_pass))
    print(s)
    time.sleep(1)
f.close()

# TODO: deletion receipts (probably also for anything not found)