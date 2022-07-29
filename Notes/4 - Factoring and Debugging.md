## Factoring & Debugging


## What is programming?

This might seem like a weird place to start a conversation about debugging code, but it is important to get a bit philosophical about code before we get too far into the process of writing code. At this point, we know enough to start the conversation. Coding really isn't what we think it is. It's much simpler (and yet more complex) than we realize. Conceptually, though, we get to focus on the simple part. Code is a way of formalizing the logical rules for a given process. There is nothing that we can program that a human *couldn't* do. It's just that many of these tasks can be done more quickly by computers.

Advantages of computers:
- They don't get sick of paying attention to minute details
- They don't care if it takes a long time
- They can do computation much more quickly than people
- They follow directions exactly

Disatvantages of computers:
- They follow directions exactly
- They can't handle ambuguity without guidance

Ok, back to programming... what is code for? We write code to provide clear instructions to a computer about how to complete a given task. In other words, programming/coding is just problem solving in a formal context. We use a specific toolkit (in our case, writing Python code), and combine that toolkit with logic to create code. This code then enables our computer to follow instructions to complete a specified process.

Critically, if our logic is faulty, then our code will inevitably be faulty as well. When writing code, we have to be very careful to think through the rules of logic, and the order in which operations will occur. We know that the computer will follow our directions **literally and exactly**, so that errors in ordering, errors in reference to variables or functions, etc., or simply errors in grammar will cause problems as our computer attempts to follow bad directions.

## Factoring Code

### How do we solve a problem with code?

As we continue to think about the best way to write code, we can consider the patters of behavior and thinking that enable us to facilitate good code writing. One of the most important procedural tools that we can develop is called **Functional Decomposition**. Functional decomposition is also known as **Factoring**. Whatever we call it, factoring is the process through which we break a problem down (decompose it) into its smallest functional elements before we write any code.

When we break our code down into very small elements, we gain the advantage of being able to see what our code needs to do more clearly. Even better, the smaller we break our code down, the simpler the tasks become, so that we can start to see a pathway from the start of our code, through simple tasks, to the end of our code.

In a real-life analogy, factoring is equivalent to writing instructions like Lego instructions. When you use the instructions that come with a Lego set, each step is very small, and is described very precisely (through visuals instead of code). Then, as we complete very small tasks (one brick here, one brick there) we eventually arrive at a complete product that tends to be very nuanced, and often has quite exciting functionality, but was built from the same basic pieces as every other Lego set. Our goal is the same. We want to break our project down into very simple steps, then reconstruct those steps one at a time. Eventually, we have reconstructed the end goal, and are able to see that our use of very simple code provides a very exciting solution to a complex problem!

### Advantages of Factoring

Before we get into any examples, here are some reasons to factor each program that you write:
1. Your code will be easier to read. When you write your code in small pieces, you can comment about the functionality of each piece, and your users will be able to follow along with you as they read your code.
2. You will know what you need to do. Factored code takes small steps, so it is much easier to know what next step you need to take as you work through your problem. Once you complete one step on your roadmap, it is time to work on the next piece.
3. Your code will be **reusable** to a greater extent. As we will see below, factoring leads us to use many small functions to create larger functions. Because we wrote our code as functions, much of our code will be reusable for similar cases. That means less coding in the future!
4. It will be easier to **debug** and run **unit tests**. When we want to test our code, we will be able to do so more easily because we can test each small segment of our code to determine if it functions as intended.

### Time to Factor!

Let's work through a problem and explore how factoring can help us. To date, many of our problems have been relatively small-scale and simple, so factoring will be a much larger benefit as our code gains size and scope than it would have been in many previous assignments. For this lesson, let's use the "Extra practice" assignment from last week, and create a class to handle complex numbers:

Create your own ``ComplexNumber`` class!
1. Complex numbers have a real and an imaginary part. The ``__init__()`` method should therefore accept two numbers. Store the first as self.real and the second as self.imag.
2. Implement a ``conjugate()`` method that returns the object's complex conjugate (as a new ``ComplexNumber`` object). Recall that $x = a + bi \implies \bar{x} = a - bi$, where $\bar{x}$ is the complex conjugate of $x$.
3. Add the following magic methods to your `ComplexNumber` class:
 	- ``__abs__()`` determines the output of the builtin ``abs()`` function (absolute value). Implement ``__abs__()`` so that it returns the magnitude of the complex number. Recall that $|a + bi| = \sqrt{a^2 + b^2}$.
 	- Implement ``__lt__()`` and ``__gt__()`` so that ``ComplexNumber`` objects can be compared by their magnitudes. That is, $(a + bi) < (c + di)$ if and only if $|a + bi| < |c + di|$, and so on.
4. Add the following magic methods to your `ComplexNumber` class:
   - Implement ``__eq__()`` and ``__ne__()`` so that two ``ComplexNumber`` objects are equal if and only if they have the same real and imaginary parts.
 	-  Implement ``__add__()``, ``__sub__()``, ``__mul__()``, and ``__div__()`` appropriately. Each of these should return a new ``ComplexNumber`` object.
    
In this case, our instructions are the first step on the path to functional decomposition (factoring): each point of the instructions describes a different task. We can summarize them, though, to gain a bit more insight into the process of what we need to do:
1. Define a class object, and an initialization method
2. Define a `conjugate` method following the instructions given
3. Define the absolute value of a complex number
4. Define less than comparison for complex numbers
5. Define greater than comparison for complex numbers
6. Define equality for complex numbers
7. Define inequality for complex numbers
8. Define addition
9. Define subtraction
10. Define multiplication
11. Define division

Obviously, we were able to break our instructions into even finer-grained steps. From here, we can explore the process to complete each of these steps in order to solve our problem.

#### Step 1

We just learned this last week! Let's make ourselves a nice simple `class` declaration. Two substeps to this process that we should consider:
- The real component of the complex number should be stored as an attribute
- The imaginary component of the complex number should also be stored as an attribute

We know how to do this! 


```python
class ComplexNumber(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imag = imaginary
```

Now we have a starting point for the rest of the functionality we want to build.

#### Step 2

We need to create a conjugate method. This isn't described as a magic method, so we just define a plain old method on the class. The complex conjugate should just return a complex number where the imaginary component is multiplied by negative one. Let's give that a shot.


```python
class ComplexNumber(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imag = imaginary
        
    def conjugate(self):
        return ComplexNumber(self.real, -1*self.imag)
```

Let's see if we get back what we thought we would:


```python
first = ComplexNumber(2, 1)
conj = first.conjugate()
print(conj.real, conj.imag)
```

    2 -1


Awesome! We are doing well so far!

#### Step 3

Now we need to calculate the absolute value of the complex number. This is just an application of the pythagorean theorem, so it should be pretty easy to implement.


```python
class ComplexNumber(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imag = imaginary
        
    def conjugate(self):
        return ComplexNumber(self.real, -1*self.imag)
    
    def __abs__(self):
        return (self.real**2 + self.imag**2)**0.5
```

I'll leave it to you to test whether or not our complex number called `first` has the expected value of $\sqrt{5}$. Be sure to look at the explanation on how to use the absolute value method!

#### Steps 4 and 5

Now that we have a method defining the absolute value of a complex number, we can determine if a complex number is greater or smaller than another complex number. We simply compare absolute values! If the absolute value of one number is greater than that of the other, then that complex number is greater. If a complex number has a smaller absolute value, then it is "less than" the other complex number. To keep our code simple, we are going to assume for now that the `other` object is also a complex number.


```python
class ComplexNumber(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imag = imaginary
        
    def conjugate(self):
        return ComplexNumber(self.real, -1*self.imag)
    
    def __abs__(self):
        return (self.real**2 + self.imag**2)**0.5
    
    def __lt__(self, other):
        if abs(self)<abs(other):
            return True
        else:
            return False
        
    def __gt__(self, other):
        if abs(self)>abs(other):
            return True
        else:
            return False
```

We are on a roll! Try it out and make sure it works!

#### Steps 6 and 7

These steps usually go together, because being equal tends to be the exact opposite of not being equal. Equality is when one complex number has the SAME real and imaginary components (not measured by absolute value this time!). So our subtasks this time are simply to check the equality of the `real` and `imag` attributes of our `self` and `other` objects. Inequality is everything that is not equal.


```python
class ComplexNumber(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imag = imaginary
        
    def conjugate(self):
        return ComplexNumber(self.real, -1*self.imag)
    
    def __abs__(self):
        return (self.real**2 + self.imag**2)**0.5
    
    def __lt__(self, other):
        if abs(self)<abs(other):
            return True
        else:
            return False
        
    def __gt__(self, other):
        if abs(self)>abs(other):
            return True
        else:
            return False
        
    def __eq__(self, other):
        if (self.real==other.real) & (self.imag==other.imag):
            return True
        else:
            return False
        
    def __ne__(self, other):
        return not self==other
```

There we go! We have made some great progress by breaking down our code into small pieces, and biting off one task at a time. We haven't done tasks 8 through 11 (yet!), so take this chance to write your own code for the operation functions (addition, subtraction, multiplication, and division). Especially on the multiplication and division methods, you'll want to further factor the tasks to simplify the work you need to do.

## Debugging

**Debugging** is, like the name suggests, the process of removing bugs from a program or script. The term has its origins in the physical removal of bugs from giant vaccuum-tube computers in the early/mid 20th century, which makes it kind of memorable. In modern computer science and programming, though, the name refers to the process of removing errors and unintended behavior from our programs. The process of debugging often takes the form of questions like these:
- Why do we get the error that we get?
- How is data moving through our code?
- What needs to be fixed?

As we will soon see, debugging is a critical part of the programming process. No less important are **unit tests**, although they are less well-known beyond programming.


### What is Unit Testing?

**Unit Testing** is the process of feeding many different (and possibly wrong) types of information to our code in order to determine how the code will work under less-than-ideal circumstances. For example, what would have happened to our `ComplexNumber` class and its functions if we had passed unexpected information into the class? What if we passed strings as the real and imaginary components? What if we tried to compare a complex number to an integer?
- What happens if our input is incorrectly formatted?
- What if the data is the wrong **type**?
- What if ...

As we test our code, we are limited by our ability to imagine the unexpected, but are able to understand how unexpected behavior affects our code. We can then protect our code against that unexpected behavior.


### Why Should I Debug and Unit Test?

- **Debugging** is critical, since our code will not work if it contains bugs. At the very least, it will not work as we expect it to
- **Unit Testing** is how we understand where our code fails to prepare for any possible case that could occur
	- We need this if we want to prevent "Garbage In, Garbage Out" problems in the future


### Debugging in Notebooks

In order to get started debugging, use the `%debug` magic function (functions built into Jupyter notebooks to make programming easier) to enter debug mode in the notebook. You should use this when you experience an error in a cell in order to explore around the error! Note that the debugger will open an INPUT field, and that this will prevent any other code from running until you exit the debugger.

Important commands in the debugger are listed in the table below:

| Command | Action |
| --- | --- |
| `q` | quit the debugger |
| `n` | advance to the next line of code in debugger |
| `c` | advance to the next break point in debugger |


```python
mycn = ComplexNumber(2,"Hi!")
othercn = ComplexNumber(3, 1)
mycn > othercn
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-14-955760b29fa9> in <module>
          1 mycn = ComplexNumber(2,"Hi!")
          2 othercn = ComplexNumber(3, 1)
    ----> 3 mycn > othercn
    

    <ipython-input-6-82ee93da270e> in __gt__(self, other)
         17 
         18     def __gt__(self, other):
    ---> 19         if abs(self)>abs(other):
         20             return True
         21         else:


    <ipython-input-6-82ee93da270e> in __abs__(self)
          8 
          9     def __abs__(self):
    ---> 10         return (self.real**2 + self.imag**2)**0.5
         11 
         12     def __lt__(self, other):


    TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'


When we try to compare these two "complex numbers", it is obvious that one is valid and the other is invalid. Trying to compare these numbers using the greater than function leads to an error. Now, we can use debug to see where our code is failing.


```python
%debug
```

    > [0;32m<ipython-input-6-82ee93da270e>[0m(10)[0;36m__abs__[0;34m()[0m
    [0;32m      8 [0;31m[0;34m[0m[0m
    [0m[0;32m      9 [0;31m    [0;32mdef[0m [0m__abs__[0m[0;34m([0m[0mself[0m[0;34m)[0m[0;34m:[0m[0;34m[0m[0;34m[0m[0m
    [0m[0;32m---> 10 [0;31m        [0;32mreturn[0m [0;34m([0m[0mself[0m[0;34m.[0m[0mreal[0m[0;34m**[0m[0;36m2[0m [0;34m+[0m [0mself[0m[0;34m.[0m[0mimag[0m[0;34m**[0m[0;36m2[0m[0;34m)[0m[0;34m**[0m[0;36m0.5[0m[0;34m[0m[0;34m[0m[0m
    [0m[0;32m     11 [0;31m[0;34m[0m[0m
    [0m[0;32m     12 [0;31m    [0;32mdef[0m [0m__lt__[0m[0;34m([0m[0mself[0m[0;34m,[0m [0mother[0m[0;34m)[0m[0;34m:[0m[0;34m[0m[0;34m[0m[0m
    [0m
    ipdb> q


Above, you can see that when I ran the debug magic function, the error happened on the line where we square the real and imaginary components of each number. Obviously, this doesn't work with strings. We can update our code to protect against this kind of behavior using some simple code additions: the `raise` keyword. This keyword allows us to create errors, preventing unexpected behavior.


```python
class ComplexNumber(object):
    def __init__(self, real, imaginary):
        if (isinstance(real, float) | isinstance(real, int)):
            self.real = real
        else:
            raise RuntimeError("The real component of your ComplexNumber is not a number.")
        if (isinstance(imaginary, float) | isinstance(imaginary, int)):
            self.imag = imaginary
        else:
            raise RuntimeError("The imaginary component of your ComplexNumber is not a number.")
        
    def conjugate(self):
        return ComplexNumber(self.real, -1*self.imag)
    
    def __abs__(self):
        return (self.real**2 + self.imag**2)**0.5
    
    def __lt__(self, other):
        if abs(self)<abs(other):
            return True
        else:
            return False
        
    def __gt__(self, other):
        if abs(self)>abs(other):
            return True
        else:
            return False
        
    def __eq__(self, other):
        if (self.real==other.real) & (self.imag==other.imag):
            return True
        else:
            return False
        
    def __ne__(self, other):
        return not self==other
```

Now when we try to create the same `ComplexNumber` objects that we created before, we get an error preventing us from misusing the class


```python
mycn = ComplexNumber(2,"Hi!")
```


    ---------------------------------------------------------------------------

    RuntimeError                              Traceback (most recent call last)

    <ipython-input-19-d68d560c3efd> in <module>
    ----> 1 mycn = ComplexNumber(2,"Hi!")
    

    <ipython-input-18-ee5d67d46317> in __init__(self, real, imaginary)
          8             self.imag = imaginary
          9         else:
    ---> 10             raise RuntimeError("The imaginary component of your ComplexNumber is not a number.")
         11 
         12     def conjugate(self):


    RuntimeError: The imaginary component of your ComplexNumber is not a number.


With our `raise` code included, the `ComplexNumber` class no longer permits anything but `int` or `float` types to become the real and imaginary components of our complex number! This means that, from now on, we can really assume that we are working with this kind of information!

### Use the history!

In a notebook context, there is a constant risk that we might run code out of order (it's really easy to do and you have probably already done it by accident). Use `_ih` to access a list of recently run cells:


```python
_ih[-5:] # Access the last 5 cells that have been run
```




    ['class ComplexNumber(object):\n    def __init__(self, real, imaginary):\n        if (isinstance(real, float) | isinstance(real, int)):\n            self.real = real\n        else:\n            raise RuntimeError("The real component of your ComplexNumber is not a number.")\n        if (isinstance(imaginary, float) | isinstance(imaginary, int)):\n            self.imag = imaginary\n        else:\n            raise RuntimeError("The real component of your ComplexNumber is not a number.")\n        \n    def conjugate(self):\n        return ComplexNumber(self.real, -1*self.imag)\n    \n    def __abs__(self):\n        return (self.real**2 + self.imag**2)**0.5\n    \n    def __lt__(self, other):\n        if abs(self)<abs(other):\n            return True\n        else:\n            return False\n        \n    def __gt__(self, other):\n        if abs(self)>abs(other):\n            return True\n        else:\n            return False\n        \n    def __eq__(self, other):\n        if (self.real==other.real) & (self.imag==other.imag):\n            return True\n        else:\n            return False\n        \n    def __ne__(self, other):\n        return not self==other',
     'mycn = ComplexNumber(2,"Hi!")',
     'class ComplexNumber(object):\n    def __init__(self, real, imaginary):\n        if (isinstance(real, float) | isinstance(real, int)):\n            self.real = real\n        else:\n            raise RuntimeError("The real component of your ComplexNumber is not a number.")\n        if (isinstance(imaginary, float) | isinstance(imaginary, int)):\n            self.imag = imaginary\n        else:\n            raise RuntimeError("The imaginary component of your ComplexNumber is not a number.")\n        \n    def conjugate(self):\n        return ComplexNumber(self.real, -1*self.imag)\n    \n    def __abs__(self):\n        return (self.real**2 + self.imag**2)**0.5\n    \n    def __lt__(self, other):\n        if abs(self)<abs(other):\n            return True\n        else:\n            return False\n        \n    def __gt__(self, other):\n        if abs(self)>abs(other):\n            return True\n        else:\n            return False\n        \n    def __eq__(self, other):\n        if (self.real==other.real) & (self.imag==other.imag):\n            return True\n        else:\n            return False\n        \n    def __ne__(self, other):\n        return not self==other',
     'mycn = ComplexNumber(2,"Hi!")',
     '_ih[-5:] # Access the last 5 cells that have been run']



Depending on what you have run as the last five commands, your results may be messy (mine was full of code for running and re-running the `class` definitions for `ComplexNumber`. This can be a valuable check, though, when you want to make sure that the code was run in the way that you expected!

### Debugging in Notebooks
You can also set debugging traces in your code. These traces allow you to set specific points in your code at which you want to jump to a debugger. This way, you don't have to wait for an error, but can follow the flow of your code even if no error occurs. This will be particularly valuable when you are working on the homework assignment! 


```python
from IPython.core.debugger import set_trace

# Chunk of your code goes here
set_trace()
# Rest of your code here
```

The trace will kick your program to a debugger at the point in which the trace is inserted into your code. You can then use the debugger commands to move around! While in the debugger, you can print the value of variables, run functions, and generally do whatever else you normally do in Python, so it is a really handy way to see what is going on inside your code.

### Doing Unit Tests

Let's try another way of testing if our code will behave properly by implementing a unit test. In order to perform unit tests, we need to create a class object that **inherits** from the `unittest.TestCase` class. We will use a unit test to make sure that two unequal complex numbers are in fact treated as unequal:


```python
import unittest

class TestComNum(unittest.TestCase):
    
    def test_ne(self):
        self.assertNotEqual(ComplexNumber(4,3), ComplexNumber(4,-3))
        

unittest.main(argv=[''], verbosity=2, exit=False)
```

    test_ne (__main__.TestComNum) ... ok
    
    ----------------------------------------------------------------------
    Ran 1 test in 0.005s
    
    OK





    <unittest.main.TestProgram at 0x7fa1f0339518>



We first import the `unittest` library, which is part of the Python standard library. In other words, it should always be installed if Python is installed.

Next, we create a testing class object that inherits from `unittest.TestCase`. Inside that class, we do NOT have to create an `__init__` method, because we are inheriting from a class that already contains one! We simply define a method with a useful name to help us remember what it is testing. In this case, `test_ne` helps me remember that I am testing the `__ne__` magic method.

Inside the method, we use `assert` commands to test whether or not some expected outcome occurs. We use `self.assertNotEqual`, because the two things we are comparing should NOT be equal.

The final line (outside of our class object) is to execute the unit test. Our output tells us that we ran a test and the outcome was "OK" (meaning we got what we expected). We don't have to just test if things are not equal, though. We can use many different `assert` statements to test various conditions:

| Method	| Checks that |
| --- | --- | 
|assertEqual(a, b) | a == b |
|assertNotEqual(a, b) | a != b |
|assertTrue(x) | bool(x) is True |
| assertFalse(x)| bool(x) is False |
|assertIs(a, b) |a is b |
|assertIsNot(a, b) | a is not b|
|assertIsNone(x) | x is None |
| assertIsNotNone(x)|x is not None|
|assertIn(a, b) | a in b |
| assertNotIn(a, b) | a not in b |
| assertIsInstance(a, b) | isinstance(a, b) |
|assertNotIsInstance(a, b) | not isinstnace(a, b) |
| assertRaises(exc, fun, args, * kwds)| fun(* args, * * kwds) raises exc |
|assertAlmostEqual(a, b)|round(a-b, 7) == 0|
|assertNotAlmostEqual(a, b)|round(a-b, 7) != 0|
|assertGreater(a, b) |a > b |
|assertGreaterEqual(a, b) | a >= b |
| assertLess(a, b) | a < b|
|assertLessEqual(a, b)| a <= b|
| assertRegexpMatches(s, r) | r.search(s) |
| assertNotRegexpMatches(a, b) | not r.search(s) |
| assertItemsEqual(a, b) | sorted(a) == sorted(b) #Works with unhashable objects |
| assertDictContainsSubset(a, b) | All the key/value pairs in a exist in b |

## Using Try, Except

The last tools we want to use in this lesson are the `try` and `except` keywords. They are used similar to `if` and `else`, but are able to capture errors! If we expect that our code will fail in some cases and will create an error, we can write a code block that will catch that error, use the information provided, and proceed to perform a different task.

For example, in a recent project of mine, some addresses came complete with city, state, and zip code, and other addresses did not. If I want to use this information to build a complete address, then I could write a `try` block. Inside this block is all of the code that I want to use **if there are no errors**, or assuming that my data is valid and contains all necessary information. Then, in an `except` block, I could write code that would use Google Maps to search for the address, collect the city, state, and zip code, and **then** complete the task.

A `try`/`except` block looks like this:


```python
try:
  myCode()
except:
  alternativeCode()
  # We could also raise an error if we want
  # TypeError, KeyError, etc.
```

For more types of errors, see [this list](https://www.programiz.com/python-programming/exceptions)

This kind of code block allows us to create code that **might actually fail**, but that we want to run wherever possible, while being notified when it does not succeed.

Given the tools in this lesson, we should be able to create complex code by solving small, tractable problems. We should also be able to diagnose and find mistakes in our code, so that we are able to resolve unexpected problems, and observe how data moves through our code.

## Solve it!

Your job is to debug the code provided in the template. In order to receive full credit, the code must run successfully, and provide the correct output (required output will be described in the test cases).

You should probably do this assignment in an IDE like Spyder, since it will make debugging significantly easier. If you choose to complete the assignment on Mimir, you will almost certainly need to make use of the Python Debugger library (here is a link to a guide) through the Mimir IDE (not through the notebook environment). You can also attempt to use the notebook environment, where your best guide will be the Variable Explorer plugin.

You will also likely need to use StackOverflow to look up various error messages that you receive, as well.

