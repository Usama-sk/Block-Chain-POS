from Block import Block
from AccountModel import AccountModel
from BlockchainUtils import BlockchainUtils
class Blockchain:

    def __init__(self):
        self.blocks = [Block.genesis()]
        self.accountModel = AccountModel()


    def addblock(self,block):
        self.blocks.append(block)

    def toJson(self):
        data ={}
        jsonBlocks =[]
        for block in self.blocks:
            jsonBlocks.append(block.toJson())
        data["blocks"] = jsonBlocks
        return data

    def blockCountValid(self,block):
        if self.blocks[-1].blockCount == block.blockCount -1:
            return True
        else:
            return False

    def lastBlockHashValid(self, block):
        lastBlockchainBlockhash = BlockchainUtils.hash(
            self.blocks[-1].payload()).hexdigest()
        if lastBlockchainBlockhash == block.lastHash:
            return True
        else:
            return False

    def getCoveredTransaction(self, transaction):
        coveredTransaction = []
        for transaction in transaction:
            coveredTransaction.append(transaction)
        else:
            print("Transaction is not covered by sender")
        return coveredTransaction

    def transactionCovered(self, transaction):
        senderBalance = self.accountModel.getBalance(transaction.senderPublicKey)
        if senderBalance >= transaction.amount:
            return True
        else:
            return False