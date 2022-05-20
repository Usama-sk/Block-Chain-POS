from ProofOfStake import ProofOfStake
from Lot import Lot
import string
import random


def getRandomString(length):
    letters = string.ascii_lowercase
    resultString = ''.join(random.choice(letters) for i in range(length))
    return resultString


if __name__ == '__main__':
    pos = ProofOfStake()
    pos.update('bob', 30)
    pos.update('alice', 20)
    pos.update('Jack', 50)

    bobWins = 0
    aliceWins = 0
    JackWins =0 
    

    for i in range(100):
        #forger = pos.forger(getRandomString(i))
        print(getRandomString(i))
    #     if forger == 'bob':
    #         bobWins += 1
    #     elif forger == 'alice':
    #         aliceWins += 1
    #     elif forger == 'Jack':
    #         JackWins += 1    

    # print('Bob won: ' + str(bobWins) + ' times')
    # print('Alice won: ' + str(aliceWins) + ' times')
    # print('Jack won: ' + str(JackWins) + ' times')
