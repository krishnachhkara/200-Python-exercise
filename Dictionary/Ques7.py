"""Given the code below, use the correct code on line 3 in order
to delete the key-value pair associated with key 3. This time,
use a method as a solution for this exercise!
crypto = {1: "Bitcoin", 2: "Ethereum", 3: "Litecoin", 4: "Stellar",
5: "XRP"}
print(crypto)"""


crypto = {1: "Bitcoin", 2: "Ethereum", 3: "Litecoin", 4: "Stellar",
5: "XRP"}

crypto.pop(3)#pop is used to remove and push is used to add
print(crypto)