import xmlrpc.client as client

s = client.ServerProxy('http://localhost:10000')

a = 5
b = 10

print(s.add(a, b))

print(s.system.listMethods())


#Check also:
#https://pypi.org/project/requests/
#https://realpython.com/python-api/