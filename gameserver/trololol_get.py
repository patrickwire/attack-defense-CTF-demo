__author__ = 'floatec'

import requests
import sys
import re



HTTPORT=":80"
BASEDIR="/"
def trololol_get(ip,flag):
    s=requests.session()
    s = requests.session()
    file = open(flag+'.data', 'r')
    token = file.read(10)
    payload = {'id': token}
    res = s.post("http://" + ip + HTTPORT + BASEDIR, data=payload)
    if(flag in res.text):
        print "worked";
        return True;
    return False;

if __name__ == "__main__":
    ip = sys.argv[1]
    flag = sys.argv[2]
    trololol_get(ip,flag)