from blockchain import BlockChain
import pprint
import os
import random

blockchain = BlockChain()


####################################### INTERACTIVE MENU #########################################

def addTransaction():
    sender = input("Type sender name: ")
    recipient = input("Type recipient name: ")
    value = float(input("Value of transaction: "))
    value = str(value) + " BTC"
    blockchain.newTransaction(sender, recipient, value)
   
def menu():
    print("#############################\n")
    print("BLOCKCHAIN TRANSACTIONS\n")
    print("#############################\n")

    print("CHOOSE AN OPTION:\n")
    print("1 - ADD TRANSACTION\n2 - VIEW CURRENT TRANSACIONS\n3 - VALIDATE BLOCK WITH CURRENT TRANSACTIONS\n4 - VIEW CHAIN\nOTHER VALUE - QUIT")

    option = (input("\n-> "))
    return option

def viewScreen(data):
    pprint.pprint(data)
    back = input('\nPress ENTER to back to menu...')


quit = False

while(not quit):
    option = menu()
    
    if(option == '1'):
        addTransaction()
    elif(option == '2'):
        os.system('cls' if os.name == 'nt' else 'clear')
        viewScreen(blockchain.pendingTransactions)
    elif(option == '3'):
        os.system('cls' if os.name == 'nt' else 'clear')
        
        if(not blockchain.pendingTransactions):
            viewScreen('This block is empty! You can try add a transaction before this action...')
        else:
            proof = random.randint(0, 9999)
            blockchain.newBlock(proof)
            viewScreen('New block hashed to chain!')

    elif(option == '4'):
        os.system('cls' if os.name == 'nt' else 'clear')
        viewScreen(blockchain.chain)
    else:
        quit = True
    
    os.system('cls' if os.name == 'nt' else 'clear')
    

    
