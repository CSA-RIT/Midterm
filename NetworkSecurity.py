#    This program is free software: you can redistribute it and/or modify
#     it under the terms of the GNU General Public License as published by
#     the Free Software Foundation, either version 3 of the License, or
#     (at your option) any later version.
#
#     This program is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU General Public License for more details.
#
#     You should have received a copy of the GNU General Public License
#     along with this program.  If not, see <http://www.gnu.org/licenses/>.

import socket
global connectlist
global portlist
global host
global x
x = 0
host = ['172.17.2.100', '172.17.2.101', '172.17.2.102', '172.17.2.103', '172.17.2.104', '172.17.2.105', '172.17.2.106', '172.17.2.107', '172.17.2.108', '172.17.2.109', '172.17.2.110', '172.17.2.111', '172.17.2.112', '172.17.2.113', '172.17.2.114', '172.17.2.115', '172.17.2.116', '172.17.2.117', '172.17.2.118', '172.17.2.119', '172.17.2.120', '172.17.2.121', '172.17.2.122', '172.17.2.123', '172.17.2.124', '172.17.2.125', '172.17.2.126', '172.17.2.127', '172.17.2.128', '172.17.2.129', '172.17.2.130', '172.17.2.131', '172.17.2.132', '172.17.2.133', '172.17.2.134', '172.17.2.135', '172.17.2.136', '172.17.2.137', '172.17.2.138', '172.17.2.139', '172.17.2.140', '172.17.2.141', '172.17.2.142', '172.17.2.143', '172.17.2.144', '172.17.2.145', '172.17.2.146', '172.17.2.147', '172.17.2.148', '172.17.2.149', '172.17.2.150', '172.17.2.151', '172.17.2.152', '172.17.2.153', '172.17.2.154', '172.17.2.155', '172.17.2.156', '172.17.2.157', '172.17.2.158', '172.17.2.159', '172.17.2.160', '172.17.2.161', '172.17.2.162', '172.17.2.163', '172.17.2.164', '172.17.2.165', '172.17.2.166', '172.17.2.167', '172.17.2.168', '172.17.2.169', '172.17.2.170', '172.17.2.171', '172.17.2.172', '172.17.2.173', '172.17.2.174', '172.17.2.175', '172.17.2.176', '172.17.2.177', '172.17.2.178', '172.17.2.179', '172.17.2.180', '172.17.2.181', '172.17.2.182', '172.17.2.183', '172.17.2.184', '172.17.2.185', '172.17.2.186', '172.17.2.187', '172.17.2.188', '172.17.2.189', '172.17.2.190', '172.17.2.191', '172.17.2.192', '172.17.2.193', '172.17.2.194', '172.17.2.195', '172.17.2.196', '172.17.2.197', '172.17.2.198', '172.17.2.199', '172.17.2.200', '172.17.2.201', '172.17.2.202', '172.17.2.203', '172.17.2.204', '172.17.2.205', '172.17.2.206', '172.17.2.207', '172.17.2.208', '172.17.2.209', '172.17.2.210', '172.17.2.211', '172.17.2.212', '172.17.2.213', '172.17.2.214', '172.17.2.215', '172.17.2.216', '172.17.2.217', '172.17.2.218', '172.17.2.219', '172.17.2.220', '172.17.2.221', '172.17.2.222', '172.17.2.223', '172.17.2.224', '172.17.2.225', '172.17.2.226', '172.17.2.227', '172.17.2.228', '172.17.2.229', '172.17.2.230', '172.17.2.231', '172.17.2.232', '172.17.2.233', '172.17.2.234', '172.17.2.235', '172.17.2.236', '172.17.2.237', '172.17.2.238', '172.17.2.239', '172.17.2.240', '172.17.2.241', '172.17.2.242', '172.17.2.243', '172.17.2.244', '172.17.2.245', '172.17.2.246', '172.17.2.247', '172.17.2.248', '172.17.2.249', '172.17.2.250', '172.17.2.251', '172.17.2.252', '172.17.2.253', '172.17.2.254', '172.17.2.255']                                          #Testing given IP with ports below
portlist = [20, 22, 80]
connectlist = []
timeout = 1
def runagain():
    global x
    global hostnum
    global connectlist
    global host
    global portlist
    print(connectlist)

    file = open("NetworkSecurity.csv", "a")
    host = str(host)
    file.write("IP: " + host[0])
    connectlist = str(connectlist)
    file.write(connectlist + "\n")
    portlist = [20, 22, 80]
    host = list(host)
    connectlist = []
    x += 1
    main()

def main():                                                     #Creating the main function to test the ports
    global host
    global x
    print(host[x])
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(timeout)
    if host == '172.17.2.255':
        portlist == []
    else:
        while portlist:                                             #While the port list still has values in it, this loop will continue to run
            try:                                                    #If the port does connect, adds it to a connected list and removes them from the port list and moves onto the next port
                print(portlist[0])
                s.connect((host[0], portlist[0]))
                print("Connected \n")
                connectlist.append(portlist[0])
                del portlist[0]
                s.close()
                main()
            except(ConnectionRefusedError, IndexError, OSError):    #If the ports do not connect, removes them from the port list and moves onto the next port
                del portlist[0]
                print("Failed \n")
        runagain()

#main()                                                          #Runs the main function