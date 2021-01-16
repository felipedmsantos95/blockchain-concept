from blockchain import BlockChain
import pprint

blockchain = BlockChain()

t1 = blockchain.newTransaction("Felipe", "Valney", '5 BTC')
t2 = blockchain.newTransaction("Joaum", "Evoney", '1 BTC')
t3 = blockchain.newTransaction("Felipe", "Citolin", '5 BTC')
blockchain.newBlock(5421)

t4 = blockchain.newTransaction("Mike Baguncinha", "Ruan", '1 BTC')
t5 = blockchain.newTransaction("Gilbertino", "Bob", '2.5 BTC')
t6 = blockchain.newTransaction("Fulano", "Robervaldo", '0.5 BTC')
blockchain.newBlock(4827)

print("Genesis Chain:")
pprint.pprint(blockchain.chain)