# Module 0: Introduction to Python

## Part 2: Running Python Programs

In this section, you will learn different ways to run Python programs and execute your Python code. 
We will explore various methods and tools that allow you to execute Python scripts and interact with your programs.
By the end of this section, you will have a solid understanding of the different methods available to execute Python code,
from the interactive mode to running scripts and utilizing IDEs or online interpreters. You will be able to choose the appropriate method based on your specific needs and preferences.

### 2.1. Running Python in Interactive Mode

Python provides an interactive mode, commonly referred to as a Python shell or REPL (Read-Eval-Print Loop), 
which allows you to execute Python code line by line and see the immediate results. This mode is useful for testing code
snippets, experimenting with language features, and performing quick calculations.

#### 2.1.1 Launching the Python Shell

To launch the Python shell, open a command prompt or terminal and enter the python command. 
This will start the Python interpreter and display a prompt indicating that you can enter Python code. 
Depending on your system, you may need to use python3 instead of python to launch the Python 3 interpreter.
`python`
`python3`

#### 2.1.2 Executing Python Statements Interactively

Once the Python shell is launched, you can start entering Python statements and expressions, and the interpreter will 
execute them immediately. For example, you can try entering simple mathematical expressions:

```python
>>> 2 + 3
5
```

```python
>>> 10 / 2
5.0
```

You can also define variables, create functions, and execute more complex code:
```python
>>> x = 5
>>> y = 2 * x + 3
>>> y
13
```
```python
>>> def square(n):
...     return n ** 2
...
>>> square(4)
16
```

#### 2.1.3 Exiting the Python Shell

To exit the Python shell, you can use the exit() function or press the appropriate key combination for your operating 
system (such as Ctrl+Z or Ctrl+D).
```python
>>> exit()
```
```python
>>> quit()
```

By running Python in interactive mode, you have a convenient way to test code, experiment with different ideas, 
and get immediate feedback. It's a valuable tool for learning and exploring Python's features and capabilities

### 2.2. Running Python Scripts

Python scripts are saved as text files with the .py extension and can be executed using various methods. 
Running Python scripts allows you to execute a series of Python statements or functions stored in a file.

#### 2.2.1 Creating a Python Script
To create a Python script, you can use any text editor or integrated development environment (IDE) of your choice. 
Open a new file and save it with a .py extension. For example, you can create a file named my_script.py.

#### 2.2.2 Executing Python Scripts from the Command Line
Once you have created your Python script, you can execute it from the command line by invoking the Python interpreter 
followed by the name of the script file. Open a command prompt or terminal, navigate to the directory where your script
is located, and use the following command:
```shell
python my_script.py
```

The Python interpreter will read the contents of the script file, execute the statements sequentially, and display the output 
or perform any desired actions.

#### 2.2.3 Passing Command-Line Arguments to a Python Script
You can also pass command-line arguments to your Python script when executing it. Command-line arguments allow you to provide
inputs or options to your script dynamically. To access the command-line arguments within your script, you can use the sys module,
specifically the sys.argv list.

For example, consider a script named greet.py that takes a name as a command-line argument and prints a personalized greeting:
```python
import sys
name = sys.argv[1]
print(f"Hello, {name}!")
```

To execute this script and pass the name "John" as an argument, use the following command:
```shell
python greet.py John
```

The script will output:
Hello, John!

By running Python scripts, you can automate tasks, build applications, and create reusable code. It provides a way to execute
a sequence of Python statements stored in a file and enables the development of more complex and extensive Python programs.

### 2.3. Integrated Development Environments (IDEs)

Integrated Development Environments (IDEs) provide a comprehensive environment for writing, editing, and running Python code.
IDEs offer features such as code completion, debugging tools, and project management capabilities, making them popular among 
developers for efficient and productive coding.

#### 2.3.1 Visual Studio Code (VS Code)
Visual Studio Code, commonly referred to as VS Code, is a popular open-source code editor developed by Microsoft. 
It offers a wide range of extensions and a vibrant community, making it a powerful choice for Python development.

To set up VS Code for Python development:
1. Install VS Code from the official website (https://code.visualstudio.com/).
2. Install the "Python" extension by Microsoft from the Visual Studio Code marketplace.
3. Create a new Python file with the .py extension or open an existing one.
4. Begin writing Python code, and utilize the features provided by VS Code, such as IntelliSense (code completion), 
code navigation, and integrated terminal.

#### 2.3.2 PyCharm
PyCharm is a professional Python IDE developed by JetBrains. It offers a rich set of features specifically designed for Python development,
including intelligent code completion, debugging tools, and support for various frameworks.

To get started with PyCharm:
1. Download and install PyCharm Community Edition (free) or PyCharm Professional Edition (commercial) from the JetBrains website (https://www.jetbrains.com/pycharm/).
2. Create a new Python project or open an existing one.
3. Write your Python code in PyCharm's code editor, and take advantage of features like code refactoring, built-in testing,
4. and version control integration.

#### 2.3.3 Atom
Atom is a customizable and hackable text editor developed by GitHub. It offers a vast ecosystem of packages and themes, 
making it a popular choice for Python developers who prefer flexibility and extensibility.

To use Atom for Python development:
1. Install Atom from the official website (https://atom.io/).
2. Install Python-related packages such as atom-python-run or ide-python for enhanced Python development features.
3. Open or create a Python file, and start coding in Atom's text editor.
4. Customize Atom with themes, syntax highlighting, and additional packages to suit your preferences.

These are just a few examples of the many IDEs available for Python development. Each IDE has its own set of features and workflows,
so feel free to explore and choose the one that best fits your needs and preferences.

By using an IDE, you can streamline your Python development process, benefit from advanced code editing capabilities, 
and boost your productivity as a Python programmer.

### 2.4. Jupyter Notebooks

Jupyter Notebooks provide an interactive computing environment that combines code, text, and visualizations. 
It allows you to create and share documents that contain live code, equations, visualizations, and narrative text, 
making it an excellent tool for data analysis, data visualization, and prototyping.

Installing Jupyter Notebooks
To use Jupyter Notebooks, you need to have Python installed on your system. You can install Jupyter Notebooks using the 
Python package manager, pip. Open your command prompt or terminal and run the following command:
```shell
$ pip install jupyter
```

Once the installation is complete, you're ready to start using Jupyter Notebooks.

Launching Jupyter Notebooks
To launch Jupyter Notebooks, open a command prompt or terminal and navigate to the directory where you want 
to create or access your notebooks. Then, run the following command:
```shell
$ jupyter notebook
```

This command will start the Jupyter server and open a web browser with the Jupyter Notebook interface. 
From there, you can create new notebooks or open existing ones.

Working with Jupyter Notebooks
Jupyter Notebooks are organized into cells, which can contain either code or markdown. You can enter and execute Python code in code cells, 
and the results will be displayed below the cell. Markdown cells allow you to add explanatory text, headings, images, and formatted content.

To execute a code cell, you can press Shift+Enter or click the "Run" button in the Jupyter Notebook toolbar. 
The output of the code will be displayed below the cell.

Jupyter Notebooks also support a wide range of features and extensions, including interactive widgets, mathematical equations,
and the ability to include images and plots directly within the notebook.

Saving and Sharing Notebooks
Jupyter Notebooks are automatically saved with the .ipynb extension. You can save your work by clicking the "Save" button or 
using the Ctrl+S or Cmd+S keyboard shortcuts.

To share your notebooks with others, you can save them and send the .ipynb file. Additionally, you can convert notebooks to 
other formats, such as HTML or PDF, for easy sharing and viewing.

JupyterLab
In addition to Jupyter Notebooks, there is another interface called JupyterLab. JupyterLab provides a more integrated and 
flexible environment for interactive computing. It supports multiple documents, drag-and-drop capabilities, and a modular structure for organizing your work.

To launch JupyterLab, open a command prompt or terminal and run the following command:
```shell
$ jupyter lab
```

This will start the JupyterLab server and open a web browser with the JupyterLab interface.

Jupyter Notebooks and JupyterLab are powerful tools for interactive Python programming, data analysis, and data visualization.
They provide a flexible and collaborative environment for working with code, data, and documentation, making them popular among researchers, data scientists, and educators.

### 2.5. Online Python Interpreters

Online Python interpreters provide a convenient way to write, execute, and test Python code directly in your web browser 
without requiring any local installation or setup. They are useful for quick prototyping, learning Python concepts, 
or sharing code snippets with others.

#### 2.5.1 Replit
Replit is an online development environment that supports multiple programming languages, including Python. 
It provides a full-featured code editor, a Python interpreter, and the ability to create and run Python programs within your browser.

To use Replit for Python programming:

Visit the Replit website (https://replit.com/) and create an account (if necessary).
Choose "New Repl" to create a new Python project.
Write your Python code in the Replit code editor.
Click the "Run" button to execute your code and see the output in the console.
Replit also offers collaborative features, allowing you to share your code with others and work on projects together in real-time.

#### 2.5.2 PythonAnywhere
PythonAnywhere is a web-based Python development and hosting environment. It provides a Python interpreter, a code editor, 
and features like scheduling tasks and hosting web applications.

To use PythonAnywhere:

Visit the PythonAnywhere website (https://www.pythonanywhere.com/) and sign up for an account.
Once logged in, you can access the PythonAnywhere console, which provides an interactive Python interpreter.
Write and execute Python code directly in the console, or use the built-in code editor to create and run Python scripts.
PythonAnywhere also allows you to host and deploy web applications written in Python, making it a versatile platform for Python development.

#### 2.5.3 Google Colab
Google Colab is a cloud-based Jupyter notebook environment provided by Google. It offers a Python interpreter, code cells,
and powerful collaboration features. It is particularly well-suited for data analysis, machine learning, and deep learning tasks.

To use Google Colab:

Open your web browser and visit the Google Colab website (https://colab.research.google.com/).
Sign in with your Google account (if necessary).
Create a new Colab notebook or open an existing one.
Write and execute Python code in the code cells provided.
Google Colab also allows you to import and analyze data, install additional libraries, and leverage the power of Google's cloud infrastructure.
Google Colab notebooks can be easily shared and collaborated on with others, making it a popular choice among data scientists and researchers.

These online Python interpreters provide a convenient and accessible way to write and execute Python code directly in your web browser.
They are especially useful when you don't have access to a local development environment or want to quickly test Python code without any setup.
