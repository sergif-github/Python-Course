# Module 11: Advanced Concepts

## Part 4: Recursion

Recursion is a powerful programming technique where a function calls itself to solve a problem by breaking it down into smaller subproblems.
It is based on the principle of divide and conquer.

When a function calls itself within its body, it is called a recursive call. The recursive call typically solves a smaller version of the 
original problem until a base case is reached. The base case is the condition that stops the recursive calls and returns a value.

Recursion can be used to solve problems that have a recursive structure or can be solved by breaking them down into smaller subproblems. 
Some examples of problems that can be solved using recursion include factorial calculation, Fibonacci sequence generation, and tree traversal.

### 4.1 Typical recursion problems 

Recursion is commonly used to solve a variety of problems in programming. Some typical recursion problems include:

- **Factorial**: The factorial of a non-negative integer n, denoted as n!, is the product of all positive integers less than or equal to n.
- **Binary Search**: A divide and conquer algorithm for searching elements in a sorted array.
- **Tower of Hanoi**: A puzzle that involves moving disks from one peg to another using three pegs.
- **Depth-First Search**: A graph traversal algorithm that explores as far as possible along each branch before backtracking.
- **Merge Sort**: A sorting algorithm that divides the input array into smaller subarrays, sorts them, and then merges them back together.
- **Permutations and Combinations**: Problems involving generating all possible arrangements or selections of elements.
- **Backtracking**: A general algorithmic technique for finding solutions by trying all possible options and undoing incorrect choices.


#### 4.1.1 Factorial

The factorial function recursively calls itself, reducing the problem into smaller subproblems until the base case is reached (n == 0),
where it returns the value 1. The recursive calls are then multiplied together to calculate the factorial of n.

```python
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
```

Example usage:
  
```python
  print(factorial(5))  # Output: 120
  print(factorial(0))  # Output: 1
```

#### 4.1.2 Binary Search

Binary search is a searching algorithm that finds the position of a target value within a sorted array. It works by repeatedly 
dividing the search space in half until the target value is found or determined to be not present.

```python
def binary_search(arr, target, low, high):
    if low > high:
        return -1
    else:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            return binary_search(arr, target, mid + 1, high)
        else:
            return binary_search(arr, target, low, mid - 1)
```

Example usage:

```python
arr = [1, 3, 5, 7, 9, 11, 13]
target = 7
result = binary_search(arr, target, 0, len(arr) - 1)
print(result)  # Output: 3
```

#### 4.1.3 Tower of Hanoi

The Tower of Hanoi is a mathematical puzzle that consists of three pegs and a number of disks of different sizes. The objective is to move 
the entire stack of disks from one peg to another, following the rules that only one disk can be moved at a time and a larger disk 
cannot be placed on top of a smaller disk.

```python
def tower_of_hanoi(n, source, destination, auxiliary):
    if n > 0:
        tower_of_hanoi(n - 1, source, auxiliary, destination)
        print(f"Move disk {n} from {source} to {destination}")
        tower_of_hanoi(n - 1, auxiliary, destination, source)
```

Example usage:

```python
tower_of_hanoi(3, 'A', 'C', 'B')
```
Output:
```
Move disk 1 from A to C
Move disk 2 from A to B
Move disk 1 from C to B
Move disk 3 from A to C
Move disk 1 from B to A
Move disk 2 from B to C
Move disk 1 from A to C
```

#### 4.1.4 Depth-First Search (DFS)

Depth-First Search is a graph traversal algorithm that explores as far as possible along each branch before backtracking. It can be implemented recursively.

```python
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start)
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
```

Example usage:

```python
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

dfs(graph, 'A')
```

Output:
```
A
B
D
E
C
F
```

#### 4.1.5 Merge Sort

Merge Sort is a sorting algorithm that follows the divide-and-conquer approach. It recursively divides the input array into two halves, 
sorts them separately, and then merges the sorted halves.

```python
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result
```

Example usage:

```python
arr = [9, 5, 1, 3, 7, 2, 8, 6, 4]
sorted_arr = merge_sort(arr)
print(sorted_arr)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

#### 4.1.6 Permutations and Combinations

Permutations and combinations are mathematical concepts used to count the number of possible arrangements or selections from a given set of elements.
They can be computed recursively.

```python
import itertools

# Permutations
items = ['A', 'B', 'C']
permutations = list(itertools.permutations(items))
print(permutations)  # Output: [('A', 'B', 'C'), ('A', 'C', 'B'), ('B', 'A', 'C'), ('B', 'C', 'A'), ('C', 'A', 'B'), ('C', 'B', 'A')]

# Combinations
combinations = list(itertools.combinations(items, 2))
print(combinations)  # Output: [('A', 'B'), ('A', 'C'), ('B', 'C')]
```

#### 4.1.7 Backtracking

Backtracking is an advanced algorithmic technique that involves exploring all possible solutions by incrementally building candidates and abandoning a candidate
as soon as it is determined to be invalid. It is often used for solving problems such as finding all possible permutations, combinations, or solving puzzles.

The implementation of backtracking varies depending on the specific problem being solved.

### 4.2 Summary 

Recursion can be a powerful tool for solving complex problems, but it should be used with caution. Recursive functions can consume
a significant amount of memory and may result in stack overflow errors if not properly implemented or if the base case is not reached.