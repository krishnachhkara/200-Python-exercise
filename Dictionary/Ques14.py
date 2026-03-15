"""Given the code below, use the correct method on line 3 in
order to return and remove an arbitrary key-value pair from the
dictionary.
crypto = {1: "Bitcoin", 2: "Ethereum", 3: "Litecoin", 4:
"Stellar", 5: "XRP"}
print(len(crypto))"""

crypto = {1: "Bitcoin", 2: "Ethereum", 3: "Litecoin", 4:
"Stellar", 5: "XRP"}

#pop is used to pop the specified item and popitem used to remove the last item like we use->

crypto.popitem()

print((crypto))