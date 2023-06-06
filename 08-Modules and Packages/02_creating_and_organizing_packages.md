# Module 8: Modules and Packages

## Part 2: Creating and Organizing Packages

In Python, packages provide a way to organize related modules together. A package is simply a directory that contains one 
or more modules and an additional `__init__.py` file. In this section, we will explore how to create and organize packages effectively.

### 2.1 Creating a Package

To create a package, you need to follow these steps:

1. Create a directory with a suitable name for your package.
2. Inside the package directory, create an `__init__.py` file. This file can be empty or can contain initialization code for the package.
3. Create one or more Python modules inside the package directory. These modules will contain the code specific to your package.

Here's an example package structure:

```
my_package/
    init.py
        module1.py
        module2.py
```

### 2.2 Importing Modules from a Package

To import modules from a package, you can use the `import` statement followed by the package name and module name. For example,
to import `module1` from the `my_package` package, you can write:

```python
import my_package.module1
```

Once imported, you can access the functions, classes, and variables defined in the module by prefixing them with the module name. 
For example, to use a function my_function() from module1, you would write:

```python
my_package.module1.my_function()
```

Alternatively, you can use the from keyword to import specific items from a module within the package. Here's an example:

```python
from my_package.module1 import my_function
```

With this import statement, you can directly use my_function() without prefixing it with the module name.

### 2.3 Organizing Subpackages

Packages can also have subpackages, which are essentially nested packages within a package. To create a subpackage, follow the same 
steps as creating a package, but place the subpackage directory inside the parent package directory. The subpackage will also require its own __init__.py file.

Here's an example package structure with a subpackage:

```markdown
my_package/
    __init__.py
    module1.py
    subpackage/
        __init__.py
        module3.py
```

To import modules from a subpackage, you can use dot notation to specify the package and subpackage names. For example, to import 
module3 from the subpackage, you can write:

```python
import my_package.subpackage.module3
```

### 2.4 Summary

Packages provide a way to organize related modules together in Python. To create a package, you need to create a directory with an
__init__.py file and one or more modules inside the package directory. You can import modules from a package using the package 
and module names, and you can organize subpackages within a package for further organization. Understanding how to create 
and organize packages will help you structure your code and make it more manageable and reusable.