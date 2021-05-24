# xrv9kvm
A little tool for building xrv9k virtual router topologies on the cheap

1. HW Requirements: 
    * ubuntu 20.04 or 18.04, minimum 16 vCPU, 96GB memory, 200GB disk
    * The datasheet says to deploy xrv9k with 4 vCPU and 16G of memory per VM.  I've run them very stably with 2 vCPU and 14G of memory.

2. Required packages:
    * openssh-server qemu qemu-kvm libvirt-bin
    * optional: virt-manager

3. clone this repository:
```
git clone https://github.com/brmcdoug/xrv9kvm.git
```

4. mkdir /opt/images/
5. download xrv9k tarball from CCO (the non-RR one is fine) and move it into /opt/images
6. untar and create kvm .img files from the qcow2.  Examples:
```
qemu-img create -b  xrv9k-fullk9-x-7.3.1.qcow2 -f qcow2 r01.img
qemu-img create -b  xrv9k-fullk9-x-7.3.1.qcow2 -f qcow2 r02.img
qemu-img create -b  xrv9k-fullk9-x-7.3.1.qcow2 -f qcow2 r17.img
etc.
```
7. create or edit the example "start_node.py" file which maps your router VM interfaces to OVS bridge and vlan instances (see example diagram)
8. create OVS bridges and linux IP addrs
```
sudo ./ovs_plumbing.sh
```
9. start nodes

```
sudo ./start_node.py r01
sudo ./start_node.py r02
sudo ./start_node.py r17
etc.
```
10. Access router VM's console port and see if they're booting (fingers crossed)

```
r01:
telnet 0 20010

r02:
telnet 0 20020

r17:
telnet 0 20170

etc.
```

11. They take a long time to boot
12. More than enough time to make a fresh pot of coffee
13. 
