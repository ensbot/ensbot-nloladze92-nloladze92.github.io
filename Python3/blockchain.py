blockchain = []


def get_last_blockchain_value():
    return blockchain[-1]


def add_value(transaction_amount, last_transaction):
    blockchain.append([last_transaction(), transaction_amount])
    print(blockchain)

add_value(2, [1])
add_value(6, get_last_blockchain_value())
add_value(8, get_last_blockchain_value())

print(blockchain)
