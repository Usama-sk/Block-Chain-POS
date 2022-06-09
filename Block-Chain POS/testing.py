from signal import signal
from Transaction import Transaction
from Wallet import Wallet

if __name__ == '__main__':

    sender= 'sender'
    receiver ='receiver'
    amount = 1
    type = 'TRANSFER'

    transaction = Transaction(sender,receiver,amount,type)
    print("transaction",transaction.toJson())


    wallet = Wallet()
    signature = wallet.sign(transaction.toJson())
    print("signature",signature)
    transaction.sign(signature)
    print('sign transaction' , transaction.toJson())


    signatureValid = Wallet.signatureValid(transaction.payload(),signature,
        wallet.publicKeyString())
    print('wallet' , wallet.publicKeyString() )
    print('payloadtransaction' ,transaction.payload())
    print('sign valid' ,signatureValid)
    

