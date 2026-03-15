"""Given the code below, use the correct code on line 3 to delete the
key-value pair associated with key 3. Do not use a method as a
solution for this exercise!
crypto = {1: "Bitcoin", 2: "Ethereum", 3: "Litecoin", 4: "Stellar", 5:
"XRP"}
print(crypto)"""


crypto = {1: "Bitcoin", 2: "Ethereum", 3: "Litecoin", 4: "Stellar", 5:
"XRP"}

del crypto[3]#note del is a keyword not a method
print(crypto)