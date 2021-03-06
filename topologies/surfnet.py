#!/usr/bin/python

from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSController
from mininet.node import CPULimitedHost, Host, Node
from mininet.node import OVSKernelSwitch, UserSwitch
from mininet.node import IVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.link import TCLink, Intf
from subprocess import call


def myNetwork():
    net = Mininet(topo=None,
                  build=False,
                  ipBase='10.0.0.0/8')

    info('*** Adding controller\n')
    c0 = net.addController(name='c0',
                           controller=RemoteController,
                           ip='127.0.0.1',
                           protocol='tcp',
                           port=6633)

    info('*** Add switches\n')
    s1 = net.addSwitch('s1', cls=OVSKernelSwitch, protocols='OpenFlow13')
    s2 = net.addSwitch('s2', cls=OVSKernelSwitch, protocols='OpenFlow13')
    s3 = net.addSwitch('s3', cls=OVSKernelSwitch, protocols='OpenFlow13')
    s4 = net.addSwitch('s4', cls=OVSKernelSwitch, protocols='OpenFlow13')
    s5 = net.addSwitch('s5', cls=OVSKernelSwitch, protocols='OpenFlow13')
    s6 = net.addSwitch('s6', cls=OVSKernelSwitch, protocols='OpenFlow13')
    s7 = net.addSwitch('s7', cls=OVSKernelSwitch, protocols='OpenFlow13')
    s8 = net.addSwitch('s8', cls=OVSKernelSwitch, protocols='OpenFlow13')
    s9 = net.addSwitch('s9', cls=OVSKernelSwitch, protocols='OpenFlow13')
    s10 = net.addSwitch('s10', cls=OVSKernelSwitch, protocols='OpenFlow13')
    s11 = net.addSwitch('s11', cls=OVSKernelSwitch, protocols='OpenFlow13')
    s12 = net.addSwitch('s12', cls=OVSKernelSwitch, protocols='OpenFlow13')
    s13 = net.addSwitch('s13', cls=OVSKernelSwitch, protocols='OpenFlow13')
    s14 = net.addSwitch('s14', cls=OVSKernelSwitch, protocols='OpenFlow13')
    s15 = net.addSwitch('s15', cls=OVSKernelSwitch, protocols='OpenFlow13')
    s16 = net.addSwitch('s16', cls=OVSKernelSwitch, protocols='OpenFlow13')
    s17 = net.addSwitch('s17', cls=OVSKernelSwitch, protocols='OpenFlow13')
    s18 = net.addSwitch('s18', cls=OVSKernelSwitch, protocols='OpenFlow13')
    s19 = net.addSwitch('s19', cls=OVSKernelSwitch, protocols='OpenFlow13')
    s20 = net.addSwitch('s20', cls=OVSKernelSwitch, protocols='OpenFlow13')
    s21 = net.addSwitch('s21', cls=OVSKernelSwitch, protocols='OpenFlow13')
    s22 = net.addSwitch('s22', cls=OVSKernelSwitch, protocols='OpenFlow13')
    s23 = net.addSwitch('s23', cls=OVSKernelSwitch, protocols='OpenFlow13')
    s24 = net.addSwitch('s24', cls=OVSKernelSwitch, protocols='OpenFlow13')
    s25 = net.addSwitch('s25', cls=OVSKernelSwitch, protocols='OpenFlow13')
    s26 = net.addSwitch('s26', cls=OVSKernelSwitch, protocols='OpenFlow13')
    s27 = net.addSwitch('s27', cls=OVSKernelSwitch, protocols='OpenFlow13')
    s28 = net.addSwitch('s28', cls=OVSKernelSwitch, protocols='OpenFlow13')
    s29 = net.addSwitch('s29', cls=OVSKernelSwitch, protocols='OpenFlow13')
    s30 = net.addSwitch('s30', cls=OVSKernelSwitch, protocols='OpenFlow13')
    s31 = net.addSwitch('s31', cls=OVSKernelSwitch, protocols='OpenFlow13')
    s32 = net.addSwitch('s32', cls=OVSKernelSwitch, protocols='OpenFlow13')
    s33 = net.addSwitch('s33', cls=OVSKernelSwitch, protocols='OpenFlow13')
    s34 = net.addSwitch('s34', cls=OVSKernelSwitch, protocols='OpenFlow13')
    s35 = net.addSwitch('s35', cls=OVSKernelSwitch, protocols='OpenFlow13')
    s36 = net.addSwitch('s36', cls=OVSKernelSwitch, protocols='OpenFlow13')
    s37 = net.addSwitch('s37', cls=OVSKernelSwitch, protocols='OpenFlow13')
    s38 = net.addSwitch('s38', cls=OVSKernelSwitch, protocols='OpenFlow13')
    s39 = net.addSwitch('s39', cls=OVSKernelSwitch, protocols='OpenFlow13')
    s40 = net.addSwitch('s40', cls=OVSKernelSwitch, protocols='OpenFlow13')
    s41 = net.addSwitch('s41', cls=OVSKernelSwitch, protocols='OpenFlow13')
    s42 = net.addSwitch('s42', cls=OVSKernelSwitch, protocols='OpenFlow13')
    s43 = net.addSwitch('s43', cls=OVSKernelSwitch, protocols='OpenFlow13')
    s44 = net.addSwitch('s44', cls=OVSKernelSwitch, protocols='OpenFlow13')
    s45 = net.addSwitch('s45', cls=OVSKernelSwitch, protocols='OpenFlow13')
    s46 = net.addSwitch('s46', cls=OVSKernelSwitch, protocols='OpenFlow13')
    s47 = net.addSwitch('s47', cls=OVSKernelSwitch, protocols='OpenFlow13')
    s48 = net.addSwitch('s48', cls=OVSKernelSwitch, protocols='OpenFlow13')
    s49 = net.addSwitch('s49', cls=OVSKernelSwitch, protocols='OpenFlow13')
    s50 = net.addSwitch('s50', cls=OVSKernelSwitch, protocols='OpenFlow13')

    s1.cmd('ovs-vsctl set bridge s1 stp-enable=true')
    s2.cmd('ovs-vsctl set bridge s2 stp-enable=true')
    s3.cmd('ovs-vsctl set bridge s3 stp-enable=true')
    s4.cmd('ovs-vsctl set bridge s4 stp-enable=true')
    s5.cmd('ovs-vsctl set bridge s5 stp-enable=true')
    s6.cmd('ovs-vsctl set bridge s6 stp-enable=true')
    s7.cmd('ovs-vsctl set bridge s7 stp-enable=true')
    s8.cmd('ovs-vsctl set bridge s8 stp-enable=true')
    s9.cmd('ovs-vsctl set bridge s9 stp-enable=true')
    s10.cmd('ovs-vsctl set bridge s10 stp-enable=true')
    s11.cmd('ovs-vsctl set bridge s11 stp-enable=true')
    s12.cmd('ovs-vsctl set bridge s12 stp-enable=true')
    s13.cmd('ovs-vsctl set bridge s13 stp-enable=true')
    s14.cmd('ovs-vsctl set bridge s14 stp-enable=true')
    s15.cmd('ovs-vsctl set bridge s15 stp-enable=true')
    s16.cmd('ovs-vsctl set bridge s16 stp-enable=true')
    s17.cmd('ovs-vsctl set bridge s17 stp-enable=true')
    s18.cmd('ovs-vsctl set bridge s18 stp-enable=true')
    s19.cmd('ovs-vsctl set bridge s19 stp-enable=true')
    s20.cmd('ovs-vsctl set bridge s20 stp-enable=true')
    s21.cmd('ovs-vsctl set bridge s21 stp-enable=true')
    s22.cmd('ovs-vsctl set bridge s22 stp-enable=true')
    s23.cmd('ovs-vsctl set bridge s23 stp-enable=true')
    s24.cmd('ovs-vsctl set bridge s24 stp-enable=true')
    s25.cmd('ovs-vsctl set bridge s25 stp-enable=true')
    s26.cmd('ovs-vsctl set bridge s26 stp-enable=true')
    s27.cmd('ovs-vsctl set bridge s27 stp-enable=true')
    s28.cmd('ovs-vsctl set bridge s28 stp-enable=true')
    s29.cmd('ovs-vsctl set bridge s29 stp-enable=true')
    s30.cmd('ovs-vsctl set bridge s30 stp-enable=true')
    s31.cmd('ovs-vsctl set bridge s31 stp-enable=true')
    s32.cmd('ovs-vsctl set bridge s32 stp-enable=true')
    s33.cmd('ovs-vsctl set bridge s33 stp-enable=true')
    s34.cmd('ovs-vsctl set bridge s34 stp-enable=true')
    s35.cmd('ovs-vsctl set bridge s35 stp-enable=true')
    s36.cmd('ovs-vsctl set bridge s36 stp-enable=true')
    s37.cmd('ovs-vsctl set bridge s37 stp-enable=true')
    s38.cmd('ovs-vsctl set bridge s38 stp-enable=true')
    s39.cmd('ovs-vsctl set bridge s39 stp-enable=true')
    s40.cmd('ovs-vsctl set bridge s40 stp-enable=true')
    s41.cmd('ovs-vsctl set bridge s41 stp-enable=true')
    s42.cmd('ovs-vsctl set bridge s42 stp-enable=true')
    s43.cmd('ovs-vsctl set bridge s43 stp-enable=true')
    s44.cmd('ovs-vsctl set bridge s44 stp-enable=true')
    s45.cmd('ovs-vsctl set bridge s45 stp-enable=true')
    s46.cmd('ovs-vsctl set bridge s46 stp-enable=true')
    s47.cmd('ovs-vsctl set bridge s47 stp-enable=true')
    s48.cmd('ovs-vsctl set bridge s48 stp-enable=true')
    s49.cmd('ovs-vsctl set bridge s49 stp-enable=true')
    s40.cmd('ovs-vsctl set bridge s50 stp-enable=true')

    info('*** Add links\n')
    net.addLink(s1, s2)
    net.addLink(s2, s8)
    net.addLink(s3, s1)
    net.addLink(s4, s3)
    net.addLink(s5, s1)
    net.addLink(s6, s14)
    net.addLink(s6, s7)
    net.addLink(s6, s5)
    net.addLink(s9, s8)
    net.addLink(s9, s5)
    net.addLink(s10, s9)
    net.addLink(s11, s4)
    net.addLink(s11, s14)
    net.addLink(s11, s15)
    net.addLink(s12, s13)
    net.addLink(s13, s14)
    net.addLink(s13, s10)
    net.addLink(s14, s12)
    net.addLink(s14, s24)
    net.addLink(s14, s17)
    net.addLink(s15, s16)
    net.addLink(s16, s18)
    net.addLink(s16, s17)
    net.addLink(s18, s19)
    net.addLink(s19, s20)
    net.addLink(s19, s17)
    net.addLink(s20, s26)
    net.addLink(s21, s25)
    net.addLink(s21, s27)
    net.addLink(s22, s23)
    net.addLink(s22, s24)
    net.addLink(s22, s14)
    net.addLink(s22, s38)
    net.addLink(s22, s39)
    net.addLink(s23, s14)
    net.addLink(s25, s22)
    net.addLink(s26, s21)
    net.addLink(s26, s22)
    net.addLink(s27, s28)
    net.addLink(s28, s29)
    net.addLink(s29, s30)
    net.addLink(s30, s31)
    net.addLink(s31, s32)
    net.addLink(s32, s33)
    net.addLink(s33, s29)
    net.addLink(s34, s28)
    net.addLink(s35, s34)
    net.addLink(s35, s39)
    net.addLink(s35, s40)
    net.addLink(s36, s37)
    net.addLink(s36, s35)
    net.addLink(s38, s36)
    net.addLink(s40, s41)
    net.addLink(s41, s42)
    net.addLink(s42, s43)
    net.addLink(s43, s44)
    net.addLink(s44, s45)
    net.addLink(s44, s46)
    net.addLink(s44, s50)
    net.addLink(s45, s22)
    net.addLink(s46, s47)
    net.addLink(s47, s48)
    net.addLink(s48, s49)
    net.addLink(s49, s46)
    net.addLink(s49, s13)
    net.addLink(s50, s13)

    h1 = net.addHost('h1', cls=Host, ip='10.0.0.1', defaultRoute=None)
    net.addLink(h1, s3)
    h2 = net.addHost('h2', cls=Host, ip='10.0.0.2', defaultRoute=None)
    net.addLink(h2, s3)
    h3 = net.addHost('h3', cls=Host, ip='10.0.0.3', defaultRoute=None)
    net.addLink(h3, s32)

    info('*** Starting network\n')
    net.build()
    info('*** Starting controllers\n')
    for controller in net.controllers:
        controller.start()

    info('*** Starting switches\n')
    net.get('s1').start([c0])
    net.get('s2').start([c0])
    net.get('s3').start([c0])
    net.get('s4').start([c0])
    net.get('s5').start([c0])
    net.get('s6').start([c0])
    net.get('s7').start([c0])
    net.get('s8').start([c0])
    net.get('s9').start([c0])
    net.get('s10').start([c0])
    net.get('s11').start([c0])
    net.get('s12').start([c0])
    net.get('s13').start([c0])
    net.get('s14').start([c0])
    net.get('s15').start([c0])
    net.get('s16').start([c0])
    net.get('s17').start([c0])
    net.get('s18').start([c0])
    net.get('s19').start([c0])
    net.get('s20').start([c0])
    net.get('s21').start([c0])
    net.get('s22').start([c0])
    net.get('s23').start([c0])
    net.get('s24').start([c0])
    net.get('s25').start([c0])
    net.get('s26').start([c0])
    net.get('s27').start([c0])
    net.get('s28').start([c0])
    net.get('s29').start([c0])
    net.get('s30').start([c0])
    net.get('s31').start([c0])
    net.get('s32').start([c0])
    net.get('s33').start([c0])
    net.get('s34').start([c0])
    net.get('s35').start([c0])
    net.get('s36').start([c0])
    net.get('s37').start([c0])
    net.get('s38').start([c0])
    net.get('s39').start([c0])
    net.get('s40').start([c0])
    net.get('s41').start([c0])
    net.get('s42').start([c0])
    net.get('s43').start([c0])
    net.get('s44').start([c0])
    net.get('s45').start([c0])
    net.get('s46').start([c0])
    net.get('s47').start([c0])
    net.get('s48').start([c0])
    net.get('s49').start([c0])
    net.get('s50').start([c0])

    call(
        'ovs-vsctl -- --id=@MiniEditNF create NetFlow target="0.0.0.0\:3000" active-timeout=600 add_id_to_interface=true -- set Bridge s10 netflow=@MiniEditNF',
        shell=True)
    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    myNetwork()

topos = {'mytopo': (lambda: myNetwork())}
