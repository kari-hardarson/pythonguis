import paramiko
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('10.10.10.84', username='tern', password='ternuser')
i,o,e=ssh.exec_command('ls -l')

print "output"
print o.read()

print "error"
print e.read()

from scp import SCPClient

with SCPClient(ssh.get_transport()) as scp:
    scp.put('test.txt', 'test2.txt')
    scp.get('test2.txt')
