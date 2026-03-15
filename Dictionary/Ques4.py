"""Given the code below, use the correct code on line 3 in order to
add a new key-value pair to the dictionary: 6: "Monero"
crypto = {1: "Bitcoin", 2: "Ethereum", 3: "Litecoin", 4: "Stellar", 5:
"XRP"}
print(crypto[6])"""

crypto = {1: "Bitcoin", 2: "Ethereum", 3: "Litecoin", 4: "Stellar", 5:
"XRP"}

crypto.update({6:"Monero"})#update is used to add new key-value pair in dict

print(crypto)