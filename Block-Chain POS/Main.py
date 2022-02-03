from numpy import block
from Transaction import Transaction
from Wallet import Wallet
from TransactionPool import TransactionPool
from Block import Block
from Blockchain import Blockchain
from BlockchainUtils import BlockchainUtils
import pprint

if __name__ == '__main__':

    blockchain = Blockchain()
    pool = TransactionPool()
    alice = Wallet()
    bob = Wallet()
    exchange = Wallet()
    forger = Wallet()

    exchangeTransaction = exchange.createTransaction(alice.publicKeyString(),10 , "EXCHANGE")
    if not pool.transactionExists(exchangeTransaction):
        pool.addTransaction(exchangeTransaction)
    
    coveredTransaction = blockchain.getCoveredTransaction(pool.transactions)
    lashHash = BlockchainUtils.hash(blockchain.blocks[-1].payload()).hexdigest()
    blockCount = blockchain.blocks[-1].blockCount +1
    blockOne = Block(coveredTransaction, lashHash,forger.publicKeyString(),blockCount)
    blockchain.addBlock(blockOne)

    transaction = alice.createTransaction(bob.publicKeyString(),5 , "TRANSFER")

    if not pool.transactionExists(transaction):
        pool.addTransaction(transaction)
    
    coveredTransaction = blockchain.getCoveredTransaction(pool.transactions)
    lashHash = BlockchainUtils.hash(blockchain.blocks[-1].payload()).hexdigest()
    blockCount = blockchain.blocks[-1].blockCount +1
    blockTwo = Block(coveredTransaction, lashHash,forger.publicKeyString(),blockCount)
    blockchain.addBlock(blockTwo)

    pprint.pprint(blockchain.toJson())
    
 




    # sender = 'sender'
    # receiver = 'receiver'
    # amount = 1
    # type = 'TRANSFER'

    # wallet = Wallet()
    # fraudulentWallet = Wallet()
    # pool = TransactionPool()

    # transaction = wallet.createTransaction(fraudulentWallet.publicKeyString(), amount, type)
    # #pprint.pprint(transaction.toJson())
    # #print(pool.transactionExists(transaction))

    # if pool.transactionExists(transaction) == False:
    #     pool.addTransaction(transaction)

    
    # blockchain = Blockchain()

    # lasthash = BlockchainUtils.hash(
    #       blockchain.blocks[-1].payload()).hexdigest()
    # blockCount =blockchain.blocks[-1].blockCount +1
    # block = wallet.createBlock(pool.transactions,lasthash,blockCount)
    # if not blockchain.LastBlockHashValid(block):
    #     print("LastBlockHash is not Valid")
    # if not blockchain.blockCountValid(block):
    #      print("BlockCount is not Valid")
    # if blockchain.blockCountValid(block) and blockchain.lastBlockHashValid(block):
    #     blockchain.addblock(block)
 
    # #blockchain.addblock(block)

    # pprint.pprint(blockchain.toJson())