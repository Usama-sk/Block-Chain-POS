from base64 import encode
from email import message
from SocketCommunication import SocketCommunicaiton
from Wallet import Wallet
from TransactionPool import TransactionPool
from Blockchain import Blockchain
from NodeAPI import NodeAPI
from Message import Message
from BlockchainUtils import BlockchainUtils

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
        self.p2p.startSocketCommunication(self)
    
    def startAPI(self , apiPort):
        self.api = NodeAPI()
        self.api.injectNode(self)
        self.api.start(apiPort)

    def handletransaction(self, transaction):
        data = transaction.payload()
        signature = transaction.signature
        signerPublickey = transaction.senderPublicKey
        signatureValid = Wallet.signatureValid(data , signature , signerPublickey)
        transactionExists = self.transactionPool.transactionExists(transaction)
        if not transactionExists and signatureValid:
            self.transactionPool.addTransaction(transaction)
            message = Message(self.p2p.socketConnector,'TRANSACTION', transaction)

            encodedMessge = BlockchainUtils.encode(message)
            self.p2p.broadcast(encodedMessge)
























        