"""Given the code below, use the correct function on line 3 in
order to get the smallest key in the dictionary.
crypto = {1: "Bitcoin", 2: "Ethereum", 3: "Litecoin", 4: "Stellar",
5: "XRP"}
key =
print(key)"""

crypto = {1: "Bitcoin", 2: "Ethereum", 3: "Litecoin", 4: "Stellar",
5: "XRP"}

key = min(crypto)

print(key)