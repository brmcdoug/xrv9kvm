#!/usr/bin/env python
# The 'start_node.py' script calls this script to launch the router qemu instance
# This script will also bring up the router VM's veth interfaces, which start_node.py has attached to OVS

import subprocess
import sys

cmdargs = str(sys.argv)

cmd1 = ['qemu-system-x86_64', '-enable-kvm', '-smbios', 'type=1,manufacturer=cisco,product=CiscoIOSXRv9000,uuid=d8d586bb-95e7-4a28-bc05-eca03d99b029', \
'-cpu', 'host', '-drive', 'file=/opt/images/%s,if=virtio,media=disk,index=1' %(sys.argv[1]), \
'-smp', 'cores=2,threads=1,sockets=1', '-display', 'none', '-daemonize', '-m', '14336', '-rtc', 'base=utc', \
'-serial', 'telnet::20%s0,server,nowait' %(sys.argv[2]), '-serial', 'telnet::20%s1,server,nowait' %(sys.argv[2]), \
'-serial', 'telnet::20%s2,server,nowait' %(sys.argv[2]), '-serial', 'telnet::20%s3,server,nowait' %(sys.argv[2]), \
'-netdev', 'tap,id=mgt0,script=no,downscript=no,ifname=rtr%smgt0,' %(sys.argv[2]), \
'-netdev', 'tap,id=mgt1,script=no,downscript=no,ifname=rtr%smgt1,' %(sys.argv[2]), \
'-device', 'virtio-net-pci,netdev=mgt1,mac=52:00:00:ee:01:%s' %(sys.argv[2]), \
'-netdev', 'tap,id=mgt2,script=no,downscript=no,ifname=rtr%smgt2,' %(sys.argv[2]), \
'-device', 'virtio-net-pci,netdev=mgt2,mac=52:00:00:ee:02:%s' %(sys.argv[2]), \
'-device', 'virtio-net-pci,netdev=mgt0,mac=52:00:00:ee:00:%s' %(sys.argv[2]), \
'-netdev', 'tap,id=xr0,script=no,downscript=no,ifname=rtr%sxr0,' %(sys.argv[2]), \
'-device', 'virtio-net-pci,netdev=xr0,mac=52:00:00:ff:00:%s' %(sys.argv[2]), \
'-netdev', 'tap,id=xr1,script=no,downscript=no,ifname=rtr%sxr1,' %(sys.argv[2]), \
'-device', 'virtio-net-pci,netdev=xr1,mac=52:00:00:ff:01:%s' %(sys.argv[2]), \
'-netdev', 'tap,id=xr2,script=no,downscript=no,ifname=rtr%sxr2,' %(sys.argv[2]), \
'-device', 'virtio-net-pci,netdev=xr2,mac=52:00:00:ff:02:%s' %(sys.argv[2]), \
'-netdev', 'tap,id=xr3,script=no,downscript=no,ifname=rtr%sxr3,' %(sys.argv[2]), \
'-device', 'virtio-net-pci,netdev=xr3,mac=52:00:00:ff:03:%s' %(sys.argv[2]), \
'-netdev', 'tap,id=xr4,script=no,downscript=no,ifname=rtr%sxr4,' %(sys.argv[2]), \
'-device', 'virtio-net-pci,netdev=xr4,mac=52:00:00:ff:04:%s' %(sys.argv[2]), \
'-netdev', 'tap,id=xr5,script=no,downscript=no,ifname=rtr%sxr5,' %(sys.argv[2]), \
'-device', 'virtio-net-pci,netdev=xr5,mac=52:00:00:ff:05:%s' %(sys.argv[2]), \
'-netdev', 'tap,id=xr6,script=no,downscript=no,ifname=rtr%sxr6,' %(sys.argv[2]), \
'-device', 'virtio-net-pci,netdev=xr6,mac=52:00:00:ff:06:%s' %(sys.argv[2]), \
'-netdev', 'tap,id=xr7,script=no,downscript=no,ifname=rtr%sxr7,' %(sys.argv[2]), \
'-device', 'virtio-net-pci,netdev=xr7,mac=52:00:00:ff:07:%s' %(sys.argv[2]), \
'-netdev', 'tap,id=xr8,script=no,downscript=no,ifname=rtr%sxr8,' %(sys.argv[2]), \
'-device', 'virtio-net-pci,netdev=xr8,mac=52:00:00:ff:08:%s' %(sys.argv[2]), \
'-netdev', 'tap,id=xr9,script=no,downscript=no,ifname=rtr%sxr9,' %(sys.argv[2]), \
'-device', 'virtio-net-pci,netdev=xr9,mac=52:00:00:ff:09:%s' %(sys.argv[2]), \
'-pidfile', '/opt/jalapeno-lab/util/pid/%s.pid' %(sys.argv[3])]

subprocess.call(cmd1)

subprocess.call(['ifconfig', 'rtr%smgt1' %(sys.argv[2]), 'up'])
subprocess.call(['ifconfig', 'rtr%sxr0' %(sys.argv[2]), 'up'])
subprocess.call(['ifconfig', 'rtr%sxr1' %(sys.argv[2]), 'up'])
subprocess.call(['ifconfig', 'rtr%sxr2' %(sys.argv[2]), 'up'])
subprocess.call(['ifconfig', 'rtr%sxr3' %(sys.argv[2]), 'up'])
subprocess.call(['ifconfig', 'rtr%sxr4' %(sys.argv[2]), 'up'])
subprocess.call(['ifconfig', 'rtr%sxr5' %(sys.argv[2]), 'up'])
subprocess.call(['ifconfig', 'rtr%sxr6' %(sys.argv[2]), 'up'])
subprocess.call(['ifconfig', 'rtr%sxr7' %(sys.argv[2]), 'up'])
subprocess.call(['ifconfig', 'rtr%sxr8' %(sys.argv[2]), 'up'])
subprocess.call(['ifconfig', 'rtr%sxr9' %(sys.argv[2]), 'up'])
