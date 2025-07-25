Welcome to my blog, here is my little compilation of what I did at Holberton School Toulouse.

# Understanding Mutable and Immutable Objects in Python

![Python Logo](https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg)

When learning Python, understanding how the language handles objects is essential. A key concept is the difference between **mutable** and **immutable** objects. This distinction affects how variables behave, especially when passed into functions. In this blog post, I’ll summarize what I’ve learned through a project that covers identity, mutability, and how Python handles function arguments—with examples.

---

## Object Identity and Type

Every object in Python has a unique **identity** and a **type**.

- `id(obj)` gives the object's identity (its memory address).
- `type(obj)` returns the object’s type.

```python
x = 5
print(id(x))       # e.g., 9785536
print(type(x))     # <class 'int'>

y = [1, 2, 3]
print(id(y))       # different from x
print(type(y))     # <class 'list'>
Two variables can reference the same object:

python
Copier
Modifier
a = [1, 2]
b = a
print(id(a) == id(b))  # True
Changes to b affect a because they share the same memory address.

## Mutable Objects
Mutable objects can be changed after creation. Common examples include:

list

dict

set

python
Copier
Modifier
numbers = [1, 2, 3]
numbers.append(4)
print(numbers)  # [1, 2, 3, 4]
These types can be modified without creating a new object.

🔒 Immutable Objects
Immutable objects cannot be changed once created. Examples:

int

float

str

tuple

python
Copier
Modifier
x = 10
x += 5
print(x)  # 15
Here, x += 5 creates a new object with value 15. The original 10 remains unchanged.

##? Why Is This Important?
Python handles mutable and immutable types differently:

Immutable objects are safe from accidental changes.

Mutable objects allow in-place modifications, which can lead to side effects.

Example:

python
Copier
Modifier
def add_item(lst):
    lst.append(100)

my_list = [1, 2, 3]
add_item(my_list)
print(my_list)  # [1, 2, 3, 100]
Because lists are mutable, the function modifies the original list.

## Function Argument Behavior
In Python, references to objects are passed to functions—not copies.

Mutable objects can be modified in a function.

Immutable objects cannot be changed directly inside a function.

Examples:

python
Copier
Modifier
def modify_int(n):
    n += 10

x = 5
modify_int(x)
print(x)  # Still 5 (int is immutable)

def modify_list(l):
    l.append(99)

my_list = [1, 2]
modify_list(my_list)
print(my_list)  # [1, 2, 99] (list is mutable)
Understanding this helps avoid unintended side effects when writing functions.

# Advanced Task: Web App & Data Types
In the advanced project tasks, I built a Flask application that interacts with JSON and CSV data sources. This helped me apply the theory in a real-world context:

Loading and displaying data based on type (csv, json)

Filtering data by ID using URL parameters

Seeing how Python behaves differently depending on the data structure used

It reinforced my understanding of how object behavior and data types affect how information flows through an application.

## Conclusion ##
Understanding mutable and immutable objects is crucial when coding in Python. It improves code quality, avoids bugs, and makes functions behave more predictably. This project deepened my knowledge and gave me practical insight into how Python’s memory model and data handling really work.

“The difference between a bug and a feature is often just one mutable object.“
