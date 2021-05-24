#!/usr/bin/env python

# This script starts routers in an virtul topology inside one or more servers.  Interface/vswitch values are hardcoded 
# into this script, so if your routers won't establish adjacencies, check for typoes (and please remember this repo's motto: "on the cheap"
# Note, this script calls util/qemu-xrv9k.py which will autopopulate parameters from start_node.py into the qemu launch VM command.

from os import getpid
from sys import argv, exit
import sys
import time
import subprocess

# example:  sudo ./start_node.py r00

#################################################################################

##### Routers 01 - 10 and router 16 run on UCS server 1

# R01 
if (sys.argv[1]) in ['r01']:
    subprocess.call(['python', 'util/qemu-xrv9k.py', 'r01.img', '01', 'r01'])
    subprocess.call(['ovs-vsctl', 'add-port', 'mgt_br', 'rtr01mgt1'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr01xr0', 'tag=102'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr01xr1', 'tag=104'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr01xr2', 'tag=105'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr01xr3', 'tag=108'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr01xr4', 'tag=110'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr01xr5', 'tag=121'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr01xr6', 'tag=124'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr01xr7', 'tag=1012'])
    subprocess.call(['ovs-vsctl', 'add-port', 'gre-br1', 'rtr01xr8', 'tag=100'])
    subprocess.call(['ovs-vsctl', 'add-port', 'gre-br1', 'rtr01xr9', 'tag=102'])

# R02
if (sys.argv[1]) in ['r02']:
    subprocess.call(['python', 'util/qemu-xrv9k.py', 'r02.img', '02', 'r02'])
    subprocess.call(['ovs-vsctl', 'add-port', 'mgt_br', 'rtr02mgt1'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr02xr0', 'tag=103'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr02xr1', 'tag=106'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr02xr2', 'tag=107'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr02xr3', 'tag=109'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr02xr4', 'tag=111'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr02xr5', 'tag=125'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr02xr6', 'tag=1012'])
    subprocess.call(['ovs-vsctl', 'add-port', 'scapy', 'rtr02xr7'])
    subprocess.call(['ovs-vsctl', 'add-port', 'gre-br1', 'rtr02xr8', 'tag=101'])
    subprocess.call(['ovs-vsctl', 'add-port', 'gre-br1', 'rtr02xr9', 'tag=103'])

# R03 
if (sys.argv[1]) in ['r03']:
    subprocess.call(['python', 'util/qemu-xrv9k.py', 'r03.img', '03', 'r03'])
    subprocess.call(['ovs-vsctl', 'add-port', 'mgt_br', 'rtr03mgt1'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr03xr0', 'tag=111'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr03xr1', 'tag=110'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr03xr2', 'tag=112'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr03xr3', 'tag=363'])

# R04 
if (sys.argv[1]) in ['r04']:
    subprocess.call(['python', 'util/qemu-xrv9k.py', 'r04.img', '04', 'r04'])
    subprocess.call(['ovs-vsctl', 'add-port', 'mgt_br', 'rtr04mgt1'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr04xr0', 'tag=112'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr04xr1', 'tag=113'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr04xr2', 'tag=74'])
    subprocess.call(['ovs-vsctl', 'add-port', 'scapy', 'rtr04xr7'])
    

# R05
if (sys.argv[1]) in ['r05']:
    subprocess.call(['python', 'util/qemu-xrv9k.py', 'r05.img', '05', 'r05'])
    subprocess.call(['ovs-vsctl', 'add-port', 'mgt_br', 'rtr05mgt1'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr05xr0', 'tag=113'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr05xr1', 'tag=114'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr05xr2', 'tag=364'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr05xr3', 'tag=365'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr05xr4', 'tag=516'])
    subprocess.call(['ovs-vsctl', 'add-port', 'scapy', 'rtr05xr7'])


# R06
if (sys.argv[1]) in ['r06']:
    subprocess.call(['python', 'util/qemu-xrv9k.py', 'r06.img', '06', 'r06'])
    subprocess.call(['ovs-vsctl', 'add-port', 'mgt_br', 'rtr06mgt1'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr06xr0', 'tag=104'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr06xr1', 'tag=106'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr06xr2', 'tag=116'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr06xr3', 'tag=117'])
    subprocess.call(['ovs-vsctl', 'add-port', 'scapy', 'rtr06xr7'])
    

# R07
if (sys.argv[1]) in ['r07']:
    subprocess.call(['python', 'util/qemu-xrv9k.py', 'r07.img', '07', 'r07'])
    subprocess.call(['ovs-vsctl', 'add-port', 'mgt_br', 'rtr07mgt1'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr07xr0', 'tag=105'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr07xr1', 'tag=107'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr07xr2', 'tag=118'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr07xr3', 'tag=119'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr07xr4', 'tag=366'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr07xr5', 'tag=367'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr07xr6', 'tag=130'])
    subprocess.call(['ovs-vsctl', 'add-port', 'scapy', 'rtr07xr7'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr07xr8', 'tag=74'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr07xr9', 'tag=999'])    


# R08
if (sys.argv[1]) in ['r08']:
    subprocess.call(['python', 'util/qemu-xrv9k.py', 'r08.img', '08', 'r08'])
    subprocess.call(['ovs-vsctl', 'add-port', 'mgt_br', 'rtr08mgt1'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr08xr0', 'tag=109'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr08xr1', 'tag=108'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr08xr2', 'tag=115'])
    subprocess.call(['ovs-vsctl', 'add-port', 'scapy', 'rtr08xr7'])


# R09
if (sys.argv[1]) in ['r09']:
    subprocess.call(['python', 'util/qemu-xrv9k.py', 'r09.img', '09', 'r09'])
    subprocess.call(['ovs-vsctl', 'add-port', 'mgt_br', 'rtr09mgt1'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr09xr0', 'tag=115'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr09xr1', 'tag=114'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr09xr2', 'tag=369'])
    subprocess.call(['ovs-vsctl', 'add-port', 'scapy', 'rtr09xr7'])

# R10
if (sys.argv[1]) in ['r10']:
    subprocess.call(['python', 'util/qemu-xrv9k.py', 'r10.img', '10', 'r10'])
    subprocess.call(['ovs-vsctl', 'add-port', 'mgt_br', 'rtr10mgt1'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr10xr0', 'tag=121'])
    subprocess.call(['ovs-vsctl', 'add-port', 'scapy', 'rtr10xr7'])

# R16
if (sys.argv[1]) in ['r16']:
    subprocess.call(['python', 'util/qemu-xrv9k.py', 'r16.img', '16', 'r16'])
    subprocess.call(['ovs-vsctl', 'add-port', 'mgt_br', 'rtr16mgt1'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr16xr0', 'tag=516'])
    subprocess.call(['ovs-vsctl', 'add-port', 'gre-br2', 'rtr16xr1', 'tag=100'])
    subprocess.call(['ovs-vsctl', 'add-port', 'gre-br3', 'rtr16xr2', 'tag=102'])
    subprocess.call(['ovs-vsctl', 'add-port', 'scapy', 'rtr16xr7'])

##### Routers 17 - 24 run on UCS server 2

# R17
if (sys.argv[1]) in ['r17']:
    subprocess.call(['python', 'util/qemu-xrv9k.py', 'r17.img', '17', 'r17'])
    subprocess.call(['ovs-vsctl', 'add-port', 'mgt_br', 'rtr17mgt1'])
    subprocess.call(['ovs-vsctl', 'add-port', 'gre-br23', 'rtr17xr0', 'tag=100'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr17xr1', 'tag=100'])
    subprocess.call(['ovs-vsctl', 'add-port', 'scapy', 'rtr17xr7'])


# R18
if (sys.argv[1]) in ['r18']:
    subprocess.call(['python', 'util/qemu-xrv9k.py', 'r18.img', '18', 'r18'])
    subprocess.call(['ovs-vsctl', 'add-port', 'mgt_br', 'rtr18mgt1'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr18xr0', 'tag=200'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr18xr1', 'tag=203'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr18xr2', 'tag=202'])
    subprocess.call(['ovs-vsctl', 'add-port', 'scapy', 'rtr18xr7'])


# R19
if (sys.argv[1]) in ['r19']:
    subprocess.call(['python', 'util/qemu-xrv9k.py', 'r19.img', '19', 'r19'])
    subprocess.call(['ovs-vsctl', 'add-port', 'mgt_br', 'rtr19mgt1'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr19xr0', 'tag=203'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr19xr1', 'tag=204'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr19xr2', 'tag=205'])
    subprocess.call(['ovs-vsctl', 'add-port', 'scapy', 'rtr19xr7'])


# R20
if (sys.argv[1]) in ['r20']:
    subprocess.call(['python', 'util/qemu-xrv9k.py', 'r20.img', '20', 'r20'])
    subprocess.call(['ovs-vsctl', 'add-port', 'mgt_br', 'rtr20mgt1'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr20xr0', 'tag=204'])
    subprocess.call(['ovs-vsctl', 'add-port', 'gre-br23', 'rtr20xr1', 'tag=103'])
    subprocess.call(['ovs-vsctl', 'add-port', 'scapy', 'rtr20xr7'])


# R21
if (sys.argv[1]) in ['r21']:
    subprocess.call(['python', 'util/qemu-xrv9k.py', 'r21.img', '21', 'r21'])
    subprocess.call(['ovs-vsctl', 'add-port', 'mgt_br', 'rtr21mgt1'])
    subprocess.call(['ovs-vsctl', 'add-port', 'gre-br23', 'rtr21xr0', 'tag=101'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr21xr1', 'tag=201'])
    subprocess.call(['ovs-vsctl', 'add-port', 'scapy', 'rtr21xr7'])


# R22
if (sys.argv[1]) in ['r22']:
    subprocess.call(['python', 'util/qemu-xrv9k.py', 'r22.img', '22', 'r22'])
    subprocess.call(['ovs-vsctl', 'add-port', 'mgt_br', 'rtr22mgt1'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr22xr0', 'tag=201'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr22xr1', 'tag=202'])
    subprocess.call(['ovs-vsctl', 'add-port', 'scapy', 'rtr22xr7'])


# R23
if (sys.argv[1]) in ['r23']:
    subprocess.call(['python', 'util/qemu-xrv9k.py', 'r23.img', '23', 'r23'])
    subprocess.call(['ovs-vsctl', 'add-port', 'mgt_br', 'rtr23mgt1'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr23xr0', 'tag=206'])
    subprocess.call(['ovs-vsctl', 'add-port', 'gre-br23', 'rtr23xr1', 'tag=104'])
    subprocess.call(['ovs-vsctl', 'add-port', 'scapy', 'rtr23xr7'])


# R24
if (sys.argv[1]) in ['r24']:
    subprocess.call(['python', 'util/qemu-xrv9k.py', 'r24.img', '24', 'r24'])
    subprocess.call(['ovs-vsctl', 'add-port', 'mgt_br', 'rtr24mgt1'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr24xr0', 'tag=206'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr24xr1', 'tag=205'])
    subprocess.call(['ovs-vsctl', 'add-port', 'scapy', 'rtr24xr7'])


############################
print "node started"
