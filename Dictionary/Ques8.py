"""Given the code below, use the correct code on line 3 in order to
verify that 7 is not a key in the dictionary.
crypto = {1: "Bitcoin", 2: "Ethereum", 3: "Litecoin", 4: "Stellar", 5:
"XRP"}
check =
print(check)"""

crypto = {1: "Bitcoin", 2: "Ethereum", 3: "Litecoin", 4: "Stellar", 5:
"XRP"}
check = 7 not in crypto
print(check)