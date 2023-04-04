# DICTIONARIES
print('''DICTIONARIES''')
print('''Dictionaries are paired sequences with associated keys and values''')

a = {"key1": "value1", "key2": "value2"}
b = {"key1": [1, 2, 3], "key2": [11, 12, 13]}
print("My dict a: ", a)
print("My dict b: ", b, "\n")


print("Dict indexing")
print('''Use dict_variable[key] to acces specific value associated with key''')
print("This is my dict a: ", a)
print("My dict  a and key1 associated value: ", a["key1"])
print("This is my dict b: ", b)
print("My dict b and key1 associated value: ", b["key1"])
print("My dict b and key1 associated index 0 value: ", b["key1"][0])
b["key1"][0] -= 1
print("My dict b and key1 associated index 0 value -1: ", b["key1"][0])
a["new key"] = "new value"
print("My dict a after adding a new key-value with a[\"newkey\"] = \"new value\": ", a)
c = {'key1': {'nestkey': {'subnestkey': 'value'}}}
print("My dict c that has 2 nested dictionaries: ", c["key1"], "\n")


print("Dict methods")
print('''Use dict_variable.keys() to get a list of all keys''')
print("My dict a keys: ", a.keys())
print('''Use dict_variable.values() to get a list of all values''')
print("My dict a values: ", a.values())
print('''Use dict_variable.items() to get tuples of all items''')
print("My dict a values: ", a.items())
