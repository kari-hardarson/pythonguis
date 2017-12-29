import paramiko
from scp import SCPClient

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('10.10.10.171', username='tern', password='ternuser')

if False:
    i,o,e=ssh.exec_command('ls -l')

    print "output"
    print o.read()

    print "error"
    print e.read()

with SCPClient(ssh.get_transport()) as scp:
    scp.get('test.xml',"foo.xml")
    import xml.etree.ElementTree as ET
    tree = ET.parse('foo.xml')
    rootnode=tree.getroot()
    tree.findall("./cplCorrelationReceiveMethod[@method]")[0].set("kari","gogo")
    for path in     ["./cplTrackUdpReceiverRdps/[@address]",
                    "./correlationUdpReceiverRdps/[@address]",
                    "./cplTrackUdpReceiverArtas/[@address]",
                    "./correlationUdpReceiverArtas/[@address]",
                    "./edgeSimulatorClockReceiver/[@address]",
                    "./flightInfoSource/[@method]"]:
        tree.findall(path)[0].set("kari","fofo")              

    tree.write('foo2.xml')
    scp.put('foo.xml', 'test.xml')
