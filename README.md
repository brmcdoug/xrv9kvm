# xrv9kvm
A little tool for building xrv9k virtual router topologies on the cheap

1. HW Requirements: 
    * ubuntu 20.04 or 18.04, minimum 16 vCPU, 96GB memory, 200GB disk
    * The datasheet says to deploy xrv9k with 4 vCPU and 16G of memory per VM.  I've run them very stably with 2 vCPU and 14G of memory.

2. Required packages:
    * openssh-server qemu qemu-kvm libvirt-bin
    * optional: virt-manager

3. mkdir /opt/images/
4. download xrv9k tarball from CCO (the non-RR one is fine) and move it into /opt/images
5. untar and create kvm .img files from the qcow2.  Examples:
```
qemu-img create -b  xrv9k-fullk9-x-7.3.1.qcow2 -f qcow2 r00.img
qemu-img create -b  xrv9k-fullk9-x-7.3.1.qcow2 -f qcow2 r01.img
qemu-img create -b  xrv9k-fullk9-x-7.3.1.qcow2 -f qcow2 r02.img
qemu-img create -b  xrv9k-fullk9-x-7.3.1.qcow2 -f qcow2 r03.img
```

6. clone this git repository:

git clone https://github.com/jalapeno/jalapeno-lab

7. create a "start_node.py" file which maps your router VM interfaces to OVS bridge and vlan instances
