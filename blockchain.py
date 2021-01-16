import hashlib
import json
from time import time

class BlockChain(object):
    def __init__(self):
        self.chain = []
        self.pendingTransactions = []

        #This was the Satoshi's message in the very first block ever mined
        self.newBlock(previousHash = "The Times 03/Jan/2009 Chancellor on brink of second bailout for banks.", proof=100)

    #Create a new block of transactions in a JSON, Reset the list of pending transactions and apend the new block to the chain
    def newBlock(self, proof, previousHash=None):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.pendingTransactions,
            'proof': proof,
            'previous_hash': previousHash or self.hash(self.chain[-1]),
        }

        self.pendingTransactions = []
        self.chain.append(block)

        return block

    
    #Search the blockchain for the most recent block
    @property
    def lastBlock(self):
        return self.chain[-1]

    
    #Add a new transaction to a block

    def newTransaction(self, sender, recipient, amount):
        transaction = {
            'sender': sender,
            'recipient': recipient,
            'amount': amount
        }

        self.pendingTransactions.append(transaction)
        return self.lastBlock['index'] + 1

    
    # Receive one block. Turn it into a string, turn that into Unicode (for hashing). Hash with SHA256 encryption, 
    # then translate the Unicode into a hexidecimal string.
    def hash(self, block):
        stringObject = json.dumps(block, sort_keys=True)
        blockString = stringObject.encode()

        rawHash = hashlib.sha256(blockString)
        hexHash = rawHash.hexdigest()

        return hexHash
