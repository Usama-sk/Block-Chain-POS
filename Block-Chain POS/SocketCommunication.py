from email import message
from p2pnetwork.node import Node

class SocketCommunicaiton(Node):
    def __init__(self, ip , port):
        super(SocketCommunicaiton,self).__init__(ip,port,None)

    def startSocketCommunication(self):
        self.start()

    def inbound_node_connected(self, conneted_node):
        print("inbound connection")
        self.send_to_node(conneted_node, "Hi I am node your connected to")

    
    def outbound_node_connected(self, conneted_node):
        print("outbound connection")
        self.send_to_node(conneted_node,"Hi I am the node who initialized the connection")
    
    def node_message(self, connected_node, message):
        print(message)