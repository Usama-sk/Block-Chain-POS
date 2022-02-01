from Transaction import Transaction
from Wallet import Wallet
from TransactionPool import TransactionPool
from Block import Block
import pprint

if __name__ == '__main__':

    sender = 'sender'
    receiver = 'receiver'
    amount = 1
    type = 'TRANSFER'

    wallet = Wallet()
    fraudulentWallet = Wallet()
    pool = TransactionPool()

    transaction = wallet.createTransaction(fraudulentWallet.publicKeyString(), amount, type)
    pprint.pprint(transaction.toJson())
    print(pool.transactionExists(transaction))

    if pool.transactionExists(transaction) == False:
        pool.addTransaction(transaction)

    block = wallet.createBlock(pool.transactions, 'lastHash', 1)
    pprint.pprint(block.toJson())

    signatureValid = Wallet.signatureValid(
        block.payload(), block.signature, wallet.publicKeyString())
    print(signatureValid)
