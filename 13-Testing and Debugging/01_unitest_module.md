# Module 13: Testing and Debugging

## Part 1 Unit Testing with the unittest Module

Unit testing is a software testing approach where individual components or units of code are tested to ensure their functionality in isolation.

### 1.1 Unitest module

Python provides the unittest module, which is a built-in testing framework that allows us to write and run unit tests for our code.
Unit testing with the unittest module helps ensure that our code behaves as expected in different scenarios. By writing comprehensive tests, 
we can catch bugs early, prevent regressions, and build robust and reliable code. The unittest module provides various assertion methods, 
such as assertEqual(), assertTrue(), assertFalse(), and many more, to perform different types of checks during testing.

To perform unit testing with the unittest module, follow these steps:

#### Import the necessary modules and classes:
```python
import unittest
```

#### Define a test class that inherits from unittest.TestCase:
```python
class MyTestCase(unittest.TestCase):
    pass
```

#### Write test methods within the test class. Each test method should start with the word "test":
```python
def test_addition(self):
    result = 2 + 2
    self.assertEqual(result, 4)
```

#### Use assertion methods from the unittest.TestCase class to check the expected results:
```python
self.assertEqual(result, expected_result)
self.assertTrue(condition)
self.assertFalse(condition)
```

#### (Optional) Use the setUp() and tearDown() methods to set up any necessary resources before running each test and clean up afterward:
```python
def setUp(self):
    # Set up resources

def tearDown(self):
    # Clean up resources
```

#### (Optional) Create a test suite to group related test cases:
```python
def suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(MyTestCase('test_addition'))
    return test_suite
```

##### (Optional) Use the unittest.TextTestRunner class to run the tests and display the results:
```python
if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
```

Here's an example that demonstrates the usage of the unittest module:

```python
import unittest

class MyTestCase(unittest.TestCase):
    def test_addition(self):
        result = 2 + 2
        self.assertEqual(result, 4)

    def test_subtraction(self):
        result = 5 - 3
        self.assertEqual(result, 2)

if __name__ == '__main__':
    unittest.main()
```

In this example, we define a test class MyTestCase that inherits from unittest.TestCase. Inside the test class, we define two test methods: 
test_addition and test_subtraction. Each test method performs a specific calculation and uses an assertion method (self.assertEqual())
to check the expected result.

To run the tests, we use unittest.main() at the bottom of the script. This will discover and execute all the test methods defined in the test class.

### 1.2 Summary

We explored unit testing with the unittest module, which is Python's built-in testing framework. We learned how to define test classes,
write test methods, and use assertion methods to verify the expected behavior of our code.

Unit testing plays a crucial role in software development by helping us identify and fix issues early in the development process. 
It allows us to validate the correctness of our code, improve code quality, and build more reliable and maintainable software.

Remember to write comprehensive test cases that cover different scenarios and edge cases. Regularly running unit tests as part of the development
workflow helps ensure that code changes do not introduce new bugs or regressions.