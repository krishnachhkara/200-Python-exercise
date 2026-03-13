""" Given the code below, use the correct code on line 3 in order to
return the value associated with key 4. This time, use a method as a
solution for this exercise!
crypto = {1: "Bitcoin", 2: "Ethereum", 3: "Litecoin", 4: "Stellar", 5:
"XRP"}
value =
print(value)"""

crypto = {1: "Bitcoin", 2: "Ethereum", 3: "Litecoin", 4: "Stellar", 5:
"XRP"}
value = crypto.get(4)#using get method
print(value)