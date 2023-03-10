import re

print("Regular Expressions (regex for short) allows a user to search for strings using almost any sort of rule.")

text = "This is my 16089356 text. (You can try to filter it)."

print("Find if text is in ('text' in text):", ('text' in text))
match = re.search('text', text)
print("Find if text is in (re.search(pattern,text)): From idx", match.start(), "to", match.end())

print("Find if text is in multiple times(re.finditer(pattern,text)): ")
for match in re.finditer('text', text):
    print(match.span())

print("\nPatterns")
print("Search two digits (\d\d):", re.search(r'\d\d', text).group())
print("Search four alphanumerics (\w\w\w\w):", re.search(r'\w\w\w\w', text).group())
print("Search for whitespace + two digits alphanumerics digits (\s\d\d):", re.search(r'\s\d\d', text).group())
print("Search for whitespace + non digit (\s\D):", re.search(r'\s\D', text).group())
print("Search for a non alphanumeric (\W):", re.search(r'\W', text).group())
print("Search for non whitespaces  (\S\S):", re.search(r'\S\S', text).group())

print("\nQuantifiers")
print("Search one digit one or more times (\d+):", re.search(r'\d+', text).group())
print("Search exactly four digits (\d{4}}):", re.search(r'\d{4}', text).group())
print("Search digits that occur 5 to 7 times (\d{5,7}}):", re.search(r'\d{5,7}', text).group())
print("Search digits that occur 5 or more time (\d{5,}):", re.search(r'\d{5,}', text).group())
print("Search one digit that occur zero or more times (\d\*):", re.search(r'\d\\*', text).group())
print("Search 'fil' that occur once or none (fil?):", re.search(r'fil?', text).group())

print("\nGroups")
print("We can group different regular expressions between parentesis into a pattern")
phone_pattern = re.compile(r'(\d{3})-(\d{3})-(\d{3})')
results = re.search(phone_pattern, "945-126-832")
print("All phone:", results.group())
print("First phone pattern:", results.group(1))
print("Second phone pattern:", results.group(2))
print("Third phone pattern:", results.group(3))

print("\nAdditional")
print("Or operator 945|126:", re.search(r"945|126", "945-126-832").group())
print("Wildcard operator r\"945...\":", re.findall(r"945...", "945-126-832"))
print("Wildcard operator r\"\S+\":", re.findall(r"\S+", "945-126-832"))
print("Starts with operator r\"^\d\":", re.findall(r"^\d", "945-126-832"))
print("Ends with operator r\"\d$\":", re.findall(r"\d$", "945-126-832"))
print("Exclusion r\"[^-]\":", re.findall(r"[^-]", "945-126-832"))


