# Module 11: Advanced Concepts

## Part 1: Decorators (Function Decorators and Class Decorators)

Decorators are a powerful feature in Python that allow you to modify the behavior of functions or classes without directly changing
their source code. They provide a way to wrap or modify functions or classes dynamically at runtime.

### 1.1 Function Decorators

Function decorators are functions that take another function as input and extend or modify its behavior. They are denoted by the `@decorator_name`
syntax placed above the function definition.

Here's an example of a simple function decorator that logs the execution time of a function:

```python
import time

def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Function {func.__name__} executed in {execution_time} seconds")
        return result
    return wrapper

@timer_decorator
def calculate_sum(a, b):
    time.sleep(1)
    return a + b

print(calculate_sum(5, 10))  # Output: 15
```

In this example, we define a timer_decorator function that takes a function as input and returns a wrapper function. 
The wrapper function records the start and end time of the function execution, calculates the execution time, and prints it out. 
We then apply the timer_decorator to the calculate_sum function using the @ syntax, which means that whenever calculate_sum is called, 
it will be wrapped by the timer_decorator and the execution time will be printed.

### 1.2 Class Decorators

Similar to function decorators, class decorators modify the behavior of classes. They are denoted by the @decorator_name syntax 
placed above the class definition.

Here's an example of a class decorator that adds a count attribute to a class, which keeps track of the number of instances created:

```python
def count_instances(cls):
    class NewClass(cls):
        count = 0

        def __new__(cls, *args, **kwargs):
            instance = super().__new__(cls)
            cls.count += 1
            return instance

    return NewClass

@count_instances
class MyClass:
    pass

print(MyClass.count)  # Output: 0
my_obj1 = MyClass()
print(MyClass.count)  # Output: 1
my_obj2 = MyClass()
print(MyClass.count)  # Output: 2
```

In this example, we define a count_instances class decorator that returns a new class (NewClass) derived from the input class (cls). 
The NewClass adds a count attribute and overrides the __new__() method to increment the count whenever a new instance is created. 
We then apply the count_instances decorator to the MyClass class using the @ syntax. When we create instances of MyClass, 
the count attribute is incremented accordingly.

### 1.3 Summary

Decorators are a versatile feature in Python, allowing you to add functionality, modify behavior, or perform preprocessing/postprocessing 
tasks without modifying the original function or class code. They are widely used in various Python frameworks and libraries to enhance 
functionality or provide additional features.