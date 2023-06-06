# Module 1: Variables and Data Types

# Part 8: Solutions

# Exercise 1
# Write a Python program that assigns a value of 5 to a variable `x` and prints its value.
print("Exercise 1")
x = 5
print(x)


# Exercise 2
# Write a Python program that assigns the values 10, 20, and 30 to variables `a`, `b`, and `c` respectively, all in a single line.
# Print the values of `a`, `b`, and `c`.
print("\nExercise 2")
a, b, c = 10, 20, 30
print(a)
print(b)
print(c)


# Exercise 3
# Write a Python program that takes two numbers as input from the user and calculates their sum. Print the result.
print("\nExercise 3")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
sum_result = num1 + num2
print("The sum of", num1, "and", num2, "is", sum_result)


# Exercise 4
# Write a Python program that takes two numbers as input from the user and calculates their difference. Print the result.
print("\nExercise 4")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
diff_result = num1 - num2
print("The difference between", num1, "and", num2, "is", diff_result)


# Exercise 5
# Write a Python program that takes two numbers as input from the user and calculates their product. Print the result.
print("\nExercise 5")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
product_result = num1 * num2
print("The product of", num1, "and", num2, "is", product_result)


# Exercise 6
# Write a Python program that takes two numbers as input from the user and calculates their division. Print the result.
print("\nExercise 6")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
division_result = num1 / num2
print("The division of", num1, "and", num2, "is", division_result)


# Exercise 7
# Write a Python program that prompts the user to enter their name and stores it in a variable called `name`. Print the value of `name`.
print("\nExercise 7")
name = input("Enter your name: ")
print(name)


# Exercise 8
# Write a Python program that prompts the user to enter their first name and last name separately. Concatenate the two strings
# and print the full name.
print("\nExercise 8")
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
full_name = first_name + " " + last_name
print("Full name:", full_name)


# Exercise 9
# Write a Python program that prompts the user to enter a sentence and calculates the length of the sentence. Print the length.
print("\nExercise 9")
sentence = input("Enter a sentence: ")
length = len(sentence)
print("Length:", length)


# Exercise 10
# Write a Python program that prompts the user to enter a sentence and a word to search. Count the number of occurrences
# of the word in the sentence and print the count.
print("\nExercise 10")
sentence = input("Enter a sentence: ")
word = input("Enter a word to search: ")
count = sentence.count(word)
print("Number of occurrences:", count)


# Exercise 11
# Write a Python program that prompts the user to enter a word and stores it in a variable called `word`. Access the first character
# of the word and print it.
print("\nExercise 11")
word = input("Enter a word: ")
first_character = word[0]
print("First character:", first_character)


# Exercise 12
# Write a Python program that prompts the user to enter a sentence and stores it in a variable called `sentence`. Use string slicing
# to print the first three characters of the sentence.
print("\nExercise 12")
sentence = input("Enter a sentence: ")
first_three_characters = sentence[:3]
print("First three characters:", first_three_characters)


# Exercise 13
# Write a Python program that prompts the user to enter a word. Use string slicing to extract the first three characters,
# the last three characters, and a substring starting from the fourth character up to the end of the word. Print the extracted substrings.
print("\nExercise 13")
word = input("Enter a word: ")
first_three = word[:3]
last_three = word[-3:]
substring = word[3:]
print("First three characters:", first_three)
print("Last three characters:", last_three)
print("Substring from the fourth character:", substring)


# Exercise 14
# Write a Python program that prompts the user to enter a word. Reverse the word using string slicing and print the reversed word.
print("\nExercise 14")
word = input("Enter a word: ")
reversed_word = word[::-1]
print("Reversed word:", reversed_word)


# Exercise 15
# Write a Python program that prompts the user to enter a word and stores it in a variable called `word`. Use the `upper()` method
# to convert the word to uppercase and print the result.
print("\nExercise 15")
word = input("Enter a word: ")
uppercased_word = word.upper()
print("Uppercased word:", uppercased_word)


# Exercise 16
# Write a Python program that prompts the user to enter a sentence. Convert the sentence to lowercase and print the result.
print("\nExercise 16")
sentence = input("Enter a sentence: ")
uppercase_sentence = sentence.lower()
print("Uppercase sentence:", uppercase_sentence)


# Exercise 17
# Write a Python program that prompts the user to enter a sentence. Split the sentence into a list of words using the `split()` method.
# Print the list of words.
print("\nExercise 17")
sentence = input("Enter a sentence: ")
words = sentence.split()
print("List of words:", words)


# Exercise 18
# Write a Python program that defines two boolean variables `is_raining` and `is_sunny`. Assign appropriate values to these variables
# based on the weather conditions. Print the values of the variables.
print("\nExercise 18")
is_raining = True
is_sunny = False
print("Is it raining?", is_raining)
print("Is it sunny?", is_sunny)


# Exercise 19
# Write a Python program that prompts the user to enter their age. Compare their age to a predefined adult age (e.g., 18) using
# the greater than operator (`>`). Print whether the user is an adult or not based on the comparison result.
print("\nExercise 19")
age = int(input("Enter your age: "))
adult_age = 18
is_adult = age > adult_age
print("Is the user an adult?", is_adult)


# Exercise 20
# Write a Python program that prompts the user to enter a number. Check if the number is a positive number greater than 10 using boolean
# comparison (`>`) and logical operators (`and`). Print the result of the check.
print("\nExercise 20")
number = int(input("Enter a number: "))
is_positive_greater_than_10 = number > 10 and number > 0
print("Is the number a positive number greater than 10?", is_positive_greater_than_10)


# Exercise 21
# Write a Python program that prompts the user to enter a number. Check if the number is divisible by both 2 and 3 using
# the logical AND operator (`and`). Print the result of the check.
print("\nExercise 21")
number = int(input("Enter a number: "))
is_divisible = number % 2 == 0 and number % 3 == 0
print("Is the number divisible by both 2 and 3?", is_divisible)


# Exercise 22
# Write a Python program that defines three boolean variables: `is_student`, `has_homework`, and `is_weekend`. Assign appropriate values
# to these variables. Write a conditional statement using logical operators (`and`, `or`) to determine if the student has to do homework. Print the result.
print("\nExercise 22")
is_student = True
has_homework = True
is_weekend = False
should_do_homework = is_student and has_homework and not is_weekend
print("Should the student do homework?", should_do_homework)


# Exercise 23
# Write a Python program that prompts the user to enter an integer. Convert the integer to a string using the `str()` function and assign it to a variable.
# Print the type of the variable.
print("\nExercise 23")
integer_input = int(input("Enter an integer: "))
converted_string = str(integer_input)
print("Converted string:", converted_string)
print("Type of converted string:", type(converted_string))


# Exercise 24
# Write a Python program that prompts the user to enter a string containing a number. Convert the string to an integer using the `int()` function
# and assign it to a variable. Print the type of the variable.
print("\nExercise 24")
string_input = input("Enter a string containing a number: ")
converted_integer = int(string_input)
print("Converted integer:", converted_integer)
print("Type of converted integer:", type(converted_integer))


# Exercise 25
# Write a Python program that defines a float number. Convert the float number to an integer using the `int()` function and assign it to a variable.
# Print the type of the variable.
print("\nExercise 25")
float_number = 3.14
converted_integer = int(float_number)
print("Converted integer:", converted_integer)
print("Type of converted integer:", type(converted_integer))


# Exercise 26
# Create an empty list called my_list. Add the numbers 1, 2, 3, and 4 to the list. Remove the number 3 from the list.
# Print the final contents of the list.
print("\nExercise 26")
my_list = []
my_list.extend([1, 2, 3, 4])
my_list.remove(3)
print(my_list)


# Exercise 27
# Create a tuple called my_tuple with the values 'apple', 'banana', 'cherry', and 'date'. Access the second element of the tuple and print it.
print("\nExercise 27")
my_tuple = ('apple', 'banana', 'cherry', 'date')
print(my_tuple[1])


# Exercise 28
# Create two sets: set1 with the values 1, 2, 3, and 4, and set2 with the values 3, 4, 5, and 6. Print the union of set1 and set2.
# Print the intersection of set1 and set2.
print("\nExercise 28")
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
print(set1.union(set2))
print(set1.intersection(set2))


# Exercise 29
# Create a dictionary called my_dict with the keys 'name', 'age', and 'city' and their corresponding values.Print the value associated
# with the key 'age'. Add a new key 'country' with the value 'USA' to the dictionary. Print the updated dictionary.
print("\nExercise 29")
my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}
print(my_dict['age'])
my_dict['country'] = 'USA'
print(my_dict)


# Exercise 30 Create a dictionary called student_scores with the keys 'Alice', 'Bob', and 'Charlie' and their corresponding values
# as the scores (out of 100). Calculate the average score of the students and store it in a variable called average_score. Print the average score.
print("\nExercise 30")
student_scores = {'Alice': 85, 'Bob': 92, 'Charlie': 78}
total_score = sum(student_scores.values())
num_students = len(student_scores)
average_score = total_score / num_students
print(average_score)