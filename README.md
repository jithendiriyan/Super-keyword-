# Python `super()` Keyword Example

This Python script demonstrates the use of the `super()` keyword for invoking methods of the parent class in a class hierarchy.

## Classes

### Class A

- Description: Defines class A with a constructor that prints "A" and a display method.
- Methods:
    - `__init__()`: Initializes the class and prints "A".
    - `display()`: Prints "You are in A".

### Class B

- Description: Defines class B, which inherits from class A, with a constructor that calls the constructor of class A using `super()`, prints "B", and a display method.
- Methods:
    - `__init__()`: Initializes the class, calls the constructor of class A using `super()`, and prints "B".
    - `display()`: Prints "You are in B".

### Class C

- Description: Defines class C, which inherits from both class A and class B, with a constructor that calls the constructor of class B using `super()` and prints "C".
- Methods:
    - `__init__()`: Initializes the class, calls the constructor of class B using `super()`, and prints "C".
    - `display()`: Prints "You are in C".

## Output

The expected output of creating an instance of class C is:

A
C