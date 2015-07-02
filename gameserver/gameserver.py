import trololol_put
import trololol_get
import hashlib
import random
import string
import time

##
# Get random string
##
def randomString(n):
    return ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(n))


fo = open("teams.list", "r")
teams=[]
for team in fo.readlines():
    teams.append(team[:-1])
    ff = open(team[:-1]+"My.flag", "a")
    ff.close()



        
for team in teams:
    print team
    m = hashlib.md5()
    m.update(randomString(100))
    flag=m.hexdigest()
    trololol_put.trololol_put(team,flag)
    for otherteam in teams:
        if otherteam!=team:
            ff = open(otherteam+".flag", "a")
            ff.write(flag+"\n")
            ff.close()
        else:
            ff = open(otherteam+"My.flag", "a")
            ff.write(flag+"\n")
            ff.close()
time.sleep(5)
for team in teams:
    ff = open(team+"My.flag", "r")
    flag=ff.readlines()[-1:][0][:-1]
    ff.close()
    if trololol_get.trololol_get(team,flag):
        ff = open(team+".def", "a")
        ff.write("+")
        ff.close()
    else:
        ff = open(team+".def", "a")
        ff.write("-")
        f.close()
