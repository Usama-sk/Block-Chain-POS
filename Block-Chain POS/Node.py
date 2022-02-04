from SocketCommunication import SocketCommunicaiton
from Wallet import Wallet
from TransactionPool import TransactionPool
from Blockchain import Blockchain

class Node:
    
    def __init__(self, ip ,port):
        self.p2p = None
        self.ip = ip
        self.port = port
        self.transactionPool = TransactionPool()
        self.wallet = Wallet()
        self.blockchain = Blockchain()

    def startP2P(self):
        self.p2p = SocketCommunicaiton(self.ip,self.port)
        self.p2p.startSocketCommunication()