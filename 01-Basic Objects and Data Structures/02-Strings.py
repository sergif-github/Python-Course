#   Strings can be prepended to an integer value to indicate a base other than 10 (0+lower/upper case letter)
#   Binary base 2
print(0b10)
print(0B10)
#O  ctal base 8
print(0o10)
print(0O10)
#   Hexadecimal base 16
print(0x10)
print(0X10)









#Boolean
a = True
print(a)
print(not(a))

#String
a = "First string"
b = ' second string'
print(a)
print(b)
# Concatenacion con ,
print(a,"concatenated with",b)
# Concatenacion con +
print(a+" concated with "+b)
print('This string contains a single quote \' character.')
print("This string contains a double quote \" character.")
print("This string contains a backslash \\ character.")
print('''This string has a single (') and a double (") quote.''')

#Composite data types
#   bytearray() Creates and returns an object of the bytearray class
#   bytes() 	Creates and returns a bytes object (similar to bytearray, but immutable)
#   dict() 	    Creates a dict object
#   frozenset() Creates a frozenset object
#   list() 	    Creates a list object
#   object() 	Creates a new featureless object
#   set() 	    Creates a set object
#   tuple() 	Creates a tuple object

#Classes, Attributes and Inheritance
#   classmethod() 	Returns a class method for a function
#   delattr() 	    Deletes an attribute from an object
#   getattr() 	    Returns the value of a named attribute of an object
#   hasattr() 	    Returns True if an object has a given attribute
#   isinstance() 	Determines whether an object is an instance of a given class
#   issubclass() 	Determines whether a class is a subclass of a given class
#   property()  	Returns a property value of a class
#   setattr() 	    Sets the value of a named attribute of an object
#   super() 	    Returns a proxy object that delegates method calls to a parent or sibling class

# Input / output
#   format() 	Converts a value to a formatted representation
#   input() 	Reads input from the console
#   open() 	    Opens a file and returns a file object
#   print() 	Prints to a text stream or the console

#Build-in functions
#   abs() 	    Returns absolute value of a number
#   divmod() 	Returns quotient and remainder of integer division
#   max() 	    Returns the largest of the given arguments or items in an iterable
#   min() 	    Returns the smallest of the given arguments or items in an iterable
#   pow() 	    Raises a number to a power
#   round() 	Rounds a floating-point value
#   sum() 	    Sums the items of an iterable

#Type Conversion
#   ascii() 	Returns a string containing a printable representation of an object
#   bin() 	    Converts an integer to a binary string
#   bool() 	    Converts an argument to a Boolean value
#   chr() 	    Returns string representation of character given by integer argument
#   complex() 	Returns a complex number constructed from arguments
#   float() 	Returns a floating-point object constructed from a number or string
#   hex() 	    Converts an integer to a hexadecimal string
#   int() 	    Returns an integer object constructed from a number or string
#   oct() 	    Converts an integer to an octal string
#   ord() 	    Returns integer representation of a character
#   repr() 	    Returns a string containing a printable representation of an object
#   str() 	    Returns a string version of an object
#   type() 	    Returns the type of an object or creates a new type object

#Iterables and iterators
#   all() 	    Returns True if all elements of an iterable are true
#   any() 	    Returns True if any elements of an iterable are true
#   enumerate() Returns a list of tuples containing indices and values from an iterable
#   filter() 	Filters elements from an iterable
#   iter() 	    Returns an iterator object
#   len() 	    Returns the length of an object
#   map() 	    Applies a function to every item of an iterable
#   next() 	    Retrieves the next item from an iterator
#   range() 	Generates a range of integer values
#   reversed() 	Returns a reverse iterator
#   slice() 	Returns a slice object
#   sorted() 	Returns a sorted list from an iterable
#   zip() 	    Creates an iterator that aggregates elements from iterables


#Variables, References, and Scope
#   dir() 	Returns a list of names in current local scope or a list of object attributes
#   globals() 	Returns a dictionary representing the current global symbol table
#   id() 	Returns the identity of an object
#   locals() 	Updates and returns a dictionary representing current local symbol table
#   vars() 	Returns __dict__ attribute for a module, class, or object

#Miscellaneous
#   callable()   	Returns True if object appears callable
#   compile()    	Compiles source into a code or AST object
#   eval()  	    Evaluates a Python expression
#   exec() 	        Implements dynamic execution of Python code
#   hash() 	        Returns the hash value of an object
#   help()      	Invokes the built-in help system
#   memoryview() 	Returns a memory view object
#   staticmethod() 	Returns a static method for a function
#   __import__() 	Invoked by the import statement




#Sequence
#Integer list
a = [1,2,3,4,5,6]
print(a)
#String list
b = ["hello","john","reese"]
print(b)
#List with different object types
c = ["hey","you",1,2,3,"go"]
print(c)
#Tuple (immutable list)
#Integer tuple
a = (1,2,3,4)
print(a)
#Tuple with different object types
b=("hello", 1,2,3,"go")
print(b)
# Range
a = range(10)
b = range(1,10,2)
print(a)
print(b)

#Dictionary
a = {1:"first name",2:"last name", "age":33}
# Print value having key=1
print(a[1])
# Print value having key="age"
print(a["age"])

#Set
x = {"apple", "banana", "cherry"}
#Frozen set
x = frozenset({"apple", "banana", "cherry"})

#Bytes
x = b"Hello"
#Byte array
x = bytearray(5)
#Memory view
x = memoryview(bytes(5))
# None
x = None
