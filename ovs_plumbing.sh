#/bin/sh
echo 'adding bridges'
ovs-vsctl add-br mgt_br
ovs-vsctl add-br rtr_br
ovs-vsctl add-br gre-br23

echo 'adding mgt ip address'
ip addr add 10.251.251.1/24 dev mgt_br
