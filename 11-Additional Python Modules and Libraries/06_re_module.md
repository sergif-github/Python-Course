# Module 12: Advanced Concepts

## Part 6: Regular Expressions (re module)

Regular expressions (regex) are powerful tools for pattern matching and text manipulation. 
The `re` module in Python provides functions and methods for working with regular expressions.

### 6.1 Creating a Regular Expression Pattern

To use regular expressions in Python, you start by creating a regular expression pattern using special syntax. 
The pattern defines a sequence of characters that need to be matched or searched for within a larger string. Here's an example:

```python
import re
pattern = r"ab+c"
```

In this example, the pattern variable is assigned the value "ab+c". This is a regular expression pattern that specifies a sequence
of characters to search for. In this case, the pattern "ab+c" represents the following:

- The character 'a' followed by the character 'b'
- The character 'b' must occur one or more times (the '+' symbol)
- Any character can appear after the sequence 'ab'

This pattern would match strings such as "abc", "abbc", "abbbc", and so on.

### 6.2 Matching Patterns

The re module provides several functions for matching patterns within strings. The most commonly used functions are re.match(), 
re.search(), and re.findall(). Here's how they work:
- re.match(pattern, string

  Attempts to match the pattern at the beginning of the string. Returns a match object if successful, or None otherwise.
- re.search(pattern, string)

    Searches the string for a match to the pattern. Returns a match object if found, or None otherwise.
- re.findall(pattern, string)

  Returns all non-overlapping matches of the pattern in the string as a list of strings.

Here's an example that demonstrates these functions:

```python
import re

pattern = r"abc"
string = "abcdefg"

match = re.match(pattern, string)
if match:
    print("Match found:", match.group())
else:
    print("No match")

match = re.search(pattern, string)
if match:
    print("Match found:", match.group())
else:
    print("No match")

matches = re.findall(pattern, string)
if matches:
    print("Matches found:", matches)
else:
    print("No matches")
```

In this example, the pattern abc is matched against the string "abcdefg". The re.match() function fails to find a match because 
the pattern is not at the beginning of the string. The re.search() function successfully finds a match, and the re.findall() function 
returns a list of all occurrences of the pattern in the string.

### 6.3 Using Regular Expression Flags

Regular expressions in Python support optional flags that modify the behavior of the pattern matching. Flags are specified as an additional
argument to the re functions. Some commonly used flags include:
- re.IGNORECASE (or re.I)

    Ignores case when matching.
- re.MULTILINE (or re.M)

    Allows matching across multiple lines.
- re.DOTALL (or re.S)

  Allows the dot . character to match any character, including newline characters.

Here's an example that demonstrates the use of flags:

```python
import re

pattern = r"abc"
string = "ABCDEF\nabcdefg"

match = re.search(pattern, string, re.IGNORECASE)
if match:
    print("Match found:", match.group())
else:
    print("No match")
```

In this example, the re.IGNORECASE flag is used to perform a case-insensitive search. As a result, the pattern abc is successfully
matched against the uppercase and lowercase occurrences in the string.

### 6.4 Summary

Regular expressions provide a flexible and powerful way to search, match, and manipulate text based on specific patterns. 
They are widely used in various applications, including text processing, data validation, and web scraping.