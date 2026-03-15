""" Given the code below, use the correct code on line 3 in order to
get a list of tuples, where each tuple represents a key-value pair in the
dictionary.
crypto = {1: "Bitcoin", 2: "Ethereum", 3: "Litecoin", 4: "Stellar", 5:
"XRP"}
result =
print(list(result))"""


crypto = {1: "Bitcoin", 2: "Ethereum", 3: "Litecoin", 4: "Stellar", 5:
"XRP"}

result = crypto.items()#.items give tuple of key value pair 

print(list(result))