# Module 11: Advanced Concepts

## Part 2: Iterators and Generators

In Python, iteration is a powerful concept that allows you to iterate over objects using the `for` loop.

Iterators and generators are powerful concepts in Python that allow for efficient and memory-friendly handling of large
datasets or infinite sequences of values.

### 3.1 Iterators

The iteration protocol consists of two methods: `__iter__()` and `__next__()`. By implementing these methods, you can make an object
iterable and define how it behaves during iteration.

An iterator is an object that implements the iterator protocol. It allows you to iterate over a collection of elements or values one at a time.

- The `__iter__()` method is responsible for returning an iterator object. It is called when you start iterating over an object. 
- This method initializes any necessary state and returns an iterator object.

- The `__next__()` method is called on the iterator object and is responsible for returning the next value in the iteration. 
- It should raise the `StopIteration` exception when there are no more values to be returned.

By implementing the iteration protocol, you can create custom iterable objects and define their iteration behavior. 
This allows you to control how the objects are iterated over and what values are returned during each iteration.

Understanding the iteration protocols is essential for building advanced iterable objects and working with custom iterators and generators in Python.

Here's an example of creating a custom iterator for a list of numbers:

```python
class NumberIterator:
    def __init__(self, numbers):
        self.numbers = numbers
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.numbers):
            raise StopIteration
        value = self.numbers[self.index]
        self.index += 1
        return value

numbers = [1, 2, 3, 4, 5]
iterator = NumberIterator(numbers)

for number in iterator:
    print(number)
```

In this example, we define a NumberIterator class that takes a list of numbers as input. It implements the __iter__() method,
which returns the iterator object itself, and the __next__() method, which retrieves the next value from the list. When there 
are no more values to iterate over, we raise a StopIteration exception. We can then use the NumberIterator object in a for loop to iterate over each number in the list.

### 3.2 Generators

Generators are a concise and elegant way to create iterators in Python. They are defined using the yield keyword, which allows
you to pause and resume the execution of a function, returning a value each time.

Here's an example of a generator function that generates a sequence of Fibonacci numbers:

```python
def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fibonacci = fibonacci_generator()

for _ in range(10):
    print(next(fibonacci))
```

In this example, we define a fibonacci_generator function using the yield keyword. It initializes two variables a and b to
the starting Fibonacci numbers. The function enters an infinite loop and yields the current Fibonacci number. It then updates 
the variables to the next Fibonacci numbers. We can use the generator in a for loop by calling the next() function on it, which
retrieves the next value from the generator.

Generators are memory-efficient because they generate values on-the-fly, only producing the next value when requested. This makes
them particularly useful for working with large datasets or infinite sequences.

### 3.3 Summary

In this section, we explored the concepts of iterators and generators in Python.

- Iterators allow you to iterate over a collection of elements or values one at a time. They implement the iterator protocol, 
 which consists of the `__iter__()` and `__next__()` methods. Iterators provide a memory-efficient way of handling large datasets or sequences of values.

- Generators are a concise and elegant way to create iterators. They are defined using the `yield` keyword, which allows you to pause
and resume the execution of a function, returning a value each time. Generators are particularly useful when dealing with large 
 datasets or infinite sequences, as they generate values on-the-fly.

By understanding iterators and generators, you can enhance the efficiency and flexibility of your Python code, enabling you to work
with large datasets or create custom sequence generators.
