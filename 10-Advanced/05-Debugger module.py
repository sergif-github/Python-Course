# DEBUGGER
print('''DEBUGGER''')

import pdb

print("pdb.set_trace() allow us to pause the code at the point of the trace and check if anything is wrong.")
x = [1,3,4]
y = 2
z = 3
result = y + z
print(result)
pdb.set_trace()
result2 = y+x
print(result2)
