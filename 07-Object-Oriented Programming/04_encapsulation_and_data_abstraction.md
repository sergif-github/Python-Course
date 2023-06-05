## Module 7: Object-Oriented Programming

### Part 4: Encapsulation and Data Abstraction

Encapsulation and data abstraction are fundamental concepts in object-oriented programming. They help in organizing and 
managing complex code by hiding implementation details and providing a clear interface for interacting with objects. Let's explore 
these concepts in more detail:

#### 4.1 Encapsulation

Encapsulation is the practice of bundling data and the methods that operate on that data together within a class. It allows
us to encapsulate the implementation details of an object and expose a clean interface for interacting with it. 
Encapsulation provides several benefits, including:

- **Data Protection**: Encapsulation protects data from being accessed or modified directly from outside the class, ensuring 
data integrity and consistency.
- **Code Organization**: Encapsulation allows us to group related data and methods together, making code more modular and maintainable.
- **Information Hiding**: Encapsulation hides the internal implementation details of an object, preventing direct access 
to sensitive data and providing abstraction.

#### 4.2 Data Abstraction

Data abstraction refers to the process of representing essential features of an object while hiding unnecessary details.
It allows us to focus on the high-level behavior and functionality of an object without worrying about its internal complexities. 
Data abstraction is achieved through the use of classes, where the internal implementation details are hidden and only relevant 
information is exposed through well-defined interfaces.

#### 4.3 Access Modifiers

Access modifiers in Python, such as public, private, and protected, help in enforcing encapsulation and controlling access 
to class members. Although Python does not have strict access modifiers like some other programming languages, we can achieve
similar behavior using naming conventions and conventions.

- **Public Members**: Public members are accessible from anywhere within the program. By convention, public members are 
typically named without any preceding underscores.
- **Private Members**: Private members are intended to be accessed only within the class itself. By convention, private 
members are typically named with a single preceding underscore, indicating that they should not be accessed from outside the class.
- **Protected Members**: Protected members are similar to private members, but they can also be accessed by subclasses. 
By convention, protected members are typically named with a single trailing underscore.

#### 4.4 Summary

In this part, you learned about encapsulation and data abstraction in object-oriented programming. Encapsulation allows us to bundle
data and methods together, protecting data, organizing code, and hiding implementation details. Data abstraction focuses on the essential
features of an object while hiding unnecessary details. Access modifiers help enforce encapsulation and control access to class members.
