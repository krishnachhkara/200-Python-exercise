"""Given the code below, use the correct method on line 3 in order to
get a list of all the values in the dictionary.
crypto = {1: "Bitcoin", 2: "Ethereum", 3: "Litecoin", 4: "Stellar", 5:
"XRP"}
val =
print(list(val))"""

crypto = {1: "Bitcoin", 2: "Ethereum", 3: "Litecoin", 4: "Stellar", 5:
"XRP"}

val = crypto.values()

print(list(val))