import getpass
import telnetlib


HOST = "10.10.10.3"
#user = input("Enter your remote account: ")
#password = getpass.getpass()

user='admin'
password='admin'

telnet = telnetlib.Telnet(HOST)

telnet.read_until(b"Username:")
telnet.write(user.encode('utf-8')+ b'\n')
#if password:
telnet.read_until(b"Password: ")
telnet.write(password.encode('utf-8')+ b'\n')


telnet.write(b'conf t\n')
telnet.write(b'interface loopback 0\n')
telnet.write(b'ip add 8.8.8.8 255.255.255.255\n')
telnet.write(b'exit\n')
telnet.write(b'exit\n')
telnet.write(b'exit\n')

telnet.read_all().decode('utf-8')

print('Done!')
telnet.write(b'sh arp\n')
telnet.write(b'sh clock\n')
telnet.write(b'sh ip int br\n')


print(telnet.read_all().decode('utf-8'))
#all_result = telnet.read_all().decode('utf-8')
print('Done!')

'''
telnet.write(b'sh arp\n')
telnet.write(b'sh clock\n')
telnet.write(b'sh ip int br\n')

telnet.write(b'exit\n')
all_result = telnet.read_all().decode('utf-8')
#all_result = telnet.read_very_eager().decode('utf-8')

print(all_result)

'''

#s=''
#s=tn.read_until('2002')
#tn.write(b"exit\n")


