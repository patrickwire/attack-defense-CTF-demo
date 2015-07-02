#!/usr/bin/env python 
import SocketServer
import os

class MyTCPHandler(SocketServer.BaseRequestHandler):
    """
    The RequestHandler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
       fo = open("teams.list", "r")
       self.request.send("team     |off|def\n")
       teams=[]
       for team in fo.readlines():
           teams.append(team[:-1])
       print teams
       for team in teams:
           off=0
           deff=0
           if os.path.isfile(team+".def"):
               ff = open(team+".def", "r")
               deff=ff.readline().count('+');
               ff.close();
           if os.path.isfile(team+".off"):
               ff = open(team+".off", "r")
               off=ff.readline().count('+');
               ff.close();
           self.request.send(team+"|"+str(off)+"|"+str(deff)+"\n")
           

if __name__ == "__main__":
    HOST, PORT = "0.0.0.0", 9990

    # Create the server, binding to localhost on port 9999
    server = SocketServer.TCPServer((HOST, PORT), MyTCPHandler)

    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    server.serve_forever()