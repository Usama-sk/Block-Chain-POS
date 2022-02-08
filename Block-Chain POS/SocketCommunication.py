from p2pnetwork.node import Node
from BlockchainUtils import BlockchainUtils
from PeerDiscoveryHandler import PeerDiscoveryHandler
from SocketConnector import SocketConnector
import json
class SocketCommunicaiton(Node):

    def __init__(self, ip , port):
        super(SocketCommunicaiton,self).__init__(ip,port,None)
        self.peers =[]
        self.peerDiscoveryHandler = PeerDiscoveryHandler(self)
        self.socketConnector = SocketConnector(ip , port)
    def connectToFirstNode(self):
        if self.socketConnector.port != 10001:
            self.connect_with_node('localhost',10001)
    
    def startSocketCommunication(self,node):
        self.node = node
        self.start()
        self.peerDiscoveryHandler.start()
        self.connectToFirstNode()

    def inbound_node_connected(self, conneted_node):
        self.peerDiscoveryHandler.handshake(conneted_node)
    
    def outbound_node_connected(self, conneted_node):
        self.peerDiscoveryHandler.handshake(conneted_node)
    def node_message(self, connected_node, message):
        message = BlockchainUtils.decode(json.dumps(message))
        if message.messageType == "DISCOVERY":
            self.peerDiscoveryHandler.handleMessage(message)
        elif message.messageType == "TRANSACTION":
            transaction = message.data
            self.node.handleTransaction(transaction)


    def send(self, receiver, message):
        self.send_to_node(receiver,message)
    
    def broadcast(self, message):
        self.send_to_nodes(message)
