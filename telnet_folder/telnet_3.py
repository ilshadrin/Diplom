from Exscript import  Account
from Exscript.protocols import SSH2


acc = Account('admin', 'admin')
con = SSH2()
con.connect('10.10.10.2')
con.login(acc)
con.execute('terminal length 0')
con.execute('sh clo')
con.send('exit')
output = con.response


print (output)