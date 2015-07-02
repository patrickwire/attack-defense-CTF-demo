__author__ = 'floatec'

import requests
import sys
import re



HTTPORT=":80"
BASEDIR="/"
def trololol_put(ip,flag):
    print ip
    print flag
    s=requests.session()
    payload = {'name': flag, 'text': 'randomfoo'}
    url="http://" + ip + HTTPORT + BASEDIR
    print url
    res = s.post(url, data=payload)
    of = open(flag+'.data', 'w')
    print res.text[-10:]
    of.write(res.text[-10:])
    of.close()

if __name__ == "__main__":
    ip = sys.argv[1]
    flag = sys.argv[2]
    trololol_put(ip,flag)


