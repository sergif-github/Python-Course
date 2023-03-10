# EXCEPTIONS
print('''EXCEPTIONS''')

print('''Errors detected during execution are called exceptions and are not unconditionally fatal''')
print('''The basic terminology and syntax used to handle errors in Python are the try and except statements''')

try:
    f = open('nonexistingfile', 'r')
    f.write('Write to non existing file')
except IOError:
    # This will only check for an IOError exception and then execute this print statement
    print("IOError Exception: Could not find file or read data")
except:
    # This will check for any exception and then execute this print statement
    print("Error Exception: Undefined error")
else:
    print("No error in try code. Content written successfully")
    f.close()
finally:
    print("Code here is always executed")


# Break and continue are executed ager the try clause is completed.


def askint():
    while True:
        try:
            val = int(input("Please enter an integer: "))
        except:
            print("Looks like you did not enter an integer!")
            continue
        else:
            print("Yep that's an integer!")
            print(val)
            break
        finally:
            print("Finally, I executed!")

askint()