s = "Hello world"

print("Changing case")
print("My string", s)
print("s.capitalize(): ", s.capitalize())
print("s.upper(): ", s.upper())
print("s.lower(): ", s.lower())

print("\nLocation and counting")
print("Count returns the number of occurrences, without overlap")
print("s.count('o'):", s.count('o'))
print("Find returns the starting index position of the first occurence")
print("s.find('o'):", s.find('o'))

print("\nIs check")
print("isalnum() return True if all characters in s are alphanumeric")
print("s.isalnum():", s.isalnum())
print("isalpha() return True if all characters in s are alphabetic")
print("s.isalpha():", s.isalpha())
print("islower() return True if all cased characters are lowercase and there is at least one cased character in s.")
print("s.islower():", s.islower())
print("isspace() return True if all characters in s are whitespace.")
print("s.isspace():", s.isspace())
print("istitle() return True if s is a title cased string and there is at least one character in s.")
print("s.istitle():", s.istitle())
print("isupper() return True if all cased characters are uppercase and there is at least one cased character in s.")
print("s.isupper():", s.isupper())
print("endswith() which is essentially the same as a boolean check on s[-1]")
print("s.endswith('o'):", s.endswith('o'))

print("\nBuilt-in Reg. Expressions")
print("Strings have some built-in methods that can resemble regular expression operations.")
print("split() function split the string at a certain element and return a list of the results")
print("s.split('e'):", s.split('e'))
print("partition() return a tuple that include the first occurrence of the separator between first and the end half.")
print("s.partition('l'):", s.partition('l'))

print("\nFormatting")
print("The center() method allows you to place your string 'centered' between a provided string with a certain length.")
print("s.center(20,'z')", s.center(20, 'z'))

print("The expandtabs() method will expand tab notations into spaces:")
print("'hello\thi'.expandtabs()", 'hello\thi'.expandtabs())

