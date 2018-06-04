attack & defanse CTF demo
==========================
this project contains a minimalistic attack and defanse CTF setup with exectlly one service

Vulnbox
-------------------------

To setup the Vulnbox just setup an linux VM with an LAMPP stack and place the index.php in the root directory.

add the ffollowing table to the MYSQL database:
```sql
CREATE TABLE "support"."support" (
"id" text,
"Name" TEXT,
"Message" TEXT
);
```


the Service has 2 vulnabilties. One is a secret backdoor in line 51 to show that some services have unused functionality. The fix for this ist just to remove the functionallity. the next one is the missing prepared statments in line 65. This vulnability realy need to be fixed.

Gameserver
---------------------------

The gameserver has multiple components. the first thing you shuld do is add all IPs of the vulnboxes to your teams.list. Atenttion! since this si just for demonstration please only insert IPs from up and running vulnboxes!

the submitterserver.py is the component that recives the flags. you just have to start it and it should do all the magic for you. the server should run on port 9999.

the scoreboard.py delivers via nc the current status of the game. you just have to start it and it should do all the magic for you. the server should run on port 9990.

the gameserver.py is for delivering flags. each time you call it it will place and recive a flag for all teams. This is done not completlly automaticlly to make the explenation more understandable. It is easier if everybody knows when the flegs are finally placed on the system.

to restart the CTF youst delete all *.off, *.def, *.flags files;

Exploits
-------------------------
in the exploits folder you find 2 exploit files. One is an empty one that ahs just implemented the communication with the submitserver. the otherone has also logic implemented to get flags from the other teams. Don't vorget to change the IPs of your team and the other team you want to attack.

Aditionalls Scripts
---------------------------
the scoreboard.sh script is a small bash script that calls the scoreboard every 5 sec.


recommended setup
--------------------------

one way to set this all up is the following:
* setup 3 virtualbox machines with ubuntu server on it.
* move the gameserver scripts to your 1st VM.
* install requests via pip on your 1st VM
* install an LAMPP stack on your 2nd and 3rd VM
* move the index.php  on your 2nd and 3rd VM
* set the network to host only network(don't forget that you can now only acces other VMs and your host in this mode, but not the internet. If you like to have internet just add another network device in your virtual machine with NAT)
* assign the ips 192.168.59.103(1st VM), 192.168.59.104(2nd VM) and 192.168.59.103(3rd VM)
* you should be ready to go now
