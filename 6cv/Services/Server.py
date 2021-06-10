from xmlrpc.server import SimpleXMLRPCServer


class CalcService(object):
    def add(self, a, b):
        return a + b


server_address = ('localhost', 10000)
server = SimpleXMLRPCServer(server_address)

calcService = CalcService()

server.register_instance(calcService)
server.register_introspection_functions()

print ("Starting Chat XML-RPC server, use <Ctrl-C> to stop")
server.serve_forever()


#https://docs.python.org/3/library/xmlrpc.html
