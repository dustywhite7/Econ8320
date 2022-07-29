# Classes (not the school kind)

###### Inspired by notes from BYU's ACME Program: [Link](http://www.acme.byu.edu/wp-content/uploads/2016/08/OOP.pdf)


## What are Classes?

**Classes** are a critical element of object-oriented programming. Basically everything that you work with in Python belongs to a class. A class is **type** of object that we are working with. In order to work with numbers, we have to understand that they have specific functionality. You might remember from week 1 when we introduced the basic types of information in Python that we talked about the different functions available to us with numbers, strings, or any other type. 

Hidden in the background of this conversation was the fact that Python has a defined understanding of numbers, for example. Each number that we can work with belongs to a **class** of objects (either `int` or `float`) that defines the way that numbers are supposed to work. Information about the data contained by that specific number object and functions that apply specifically to that object are associated with the object through its **class inheritance**. This inheritance allows one class to build off of another, and we will see this in action throughout this course.

Perhaps the single greatest advantage a class provides is to allow us to generate multiple related objects, and to manipulate them quickly and efficiently. Let's start making classes to understand a bit more

## Creating classes

Let's imagine we work at a cafeteria, and that we want to represent a sandwich as code. There are certain things we would want to know about every sandwich:
1) Whose is it?
2) What toppings will we put on our sandwich?
3) What kind of bread will we use?

How can we start designing our sandwich code?


```python
class Sandwich(object):
    def __init__(self, owner, bread='white'):
        self.owner = owner
        self.bread = bread
        self.toppings = []
```

When we create a class, the FIRST functionality that we need to create is to describe how to initialize an object of that class (in this case, a ```Sandwich```). We do this by using the ```__init__()``` method (methods are functions assigned to a class object)
- We tell our object what arguments to expect, and store these values as **attributes** of our object

An **attribute** is a piece of information that is directly attached to an **instance of a class**. It tells us some of the characteristics of that object. An **instance** of a class is just one object that inherits attributes and functionality from a specific class. For example, `int` is the class of integer objects and `7` is an **instance** of the `int` class.

Note that, although some built-in classes do not follow this rule, when we define a class, it is best practice to give it a name with a capitalized first letter, to distinguish it from a function. Traditionally, functions (and variables) are given names that start with lower-case letters.

### Inheritance

A class can **inherit** from another class. When we wrote `class Sandwich(object):`, the `object` class is the class from which our new `Sandwich` class will inherit. This is the most generic inheritance that we can give. Basically, we are saying that `Sandwich` will be a class, but will not inherit anything but the most rudimentary building blocks of an object. We could also specify that a class will inherit from any other existing class, if that would help us to build the functionality that we need.

### `__init__`

As we create our class, we need to start by defining the function `__init__` (two underscores on each side). This function tells our class how to make use of any external information provided as we create a new instance of our class. Just like a function, `__init__` takes arguments. These arguments always begin with `self`. `self` is the argument that tells our function that it is attached to a class, and that it should ensure that it has access to that class. In short, we are giving our function permission to modify our object.

Any other arguments are provided after self, and can bring useful information for describing a specific instance of the class. In our case these are `owner` and `bread`, so that we can indicate who owns the sandwich and what kind of bread it was made on. We can also see that `bread` has a default argument: `bread='white'` tells Python that the default bread type is `white`, and that if the user does not specify a type of bread, we can work with `white` bread in this instance. No default is provided for `owner`, though. The user MUST specify the owner, or encounter an error.

Inside of the `__init__` function, we assign arguments to **attributes** using the `.` syntax. We are creating information that is tied to our class instance. For example, each sandwich instance will have an attribute `.owner`, which will contain information about who the owner of the sandwich is, as well as a `.bread` attribute taking in information about which bread was used. We can also create other attributes. In this case, we create a `.toppings` attribute associated with an empty list that will be filled in as we add toppings to the sandwich.


### Creating an instance of a class

Let's make an instance of our `Sandwich` class.


```python
mine = Sandwich('Dusty')
print(mine)
```

We created a delicious sandwich class, but we can't print anything about it! This is because we have created a class that stores some information about our instance, but does not have any functionality to accompany that storage. Now we need to write **methods** to make use of the information contained by our instance of `Sandwich`. A **method** is simply a function that is attached to a class object. We define these functions inside of the class definition, so that they are indented within the block of code that constitutes the class itself.


### Magic Methods (MANY more [here](https://www.python-course.eu/python3_magic_methods.php))

Some of the first methods we should define are **magic methods**, or methods using common operators. Magic methods must be defined to take advantage of operators like the `+` or addition operator, and all other logical and mathematical operators. These operators generally take two arguments: `self` and `other`. The `self` argument is the object references **in front of** the operator, and `other` denotes the object that follows the operator. If we write `3 + 5`, then `self` is `3` and `other` is `5`. Here are a few of the most common magic methods:


| Operator | Method                                |
|----------|---------------------------------------|
| +        | object.\_\_add\_\_(self, other)           |
| -        | object.\_\_sub\_\_(self, other)           |
| *        | object.\_\_mul\_\_(self, other)           |
| //       | object.\_\_floordiv\_\_(self, other)      |
| /        | object.\_\_truediv\_\_(self, other)       |
| **       | object.\_\_pow\_\_(self, other[, modulo]) |
| print()  | object.\_\_repr\_\_(self)                 |


Not all of the magic methods will make sense for all classes. Some that make sense (in my sandwich head) are adding, subtracting, equality, inequality, and printing out some representation of our sandwich. Not all of the magic methods will make sense for all classes. 

#### Magic Methods - Adding


```python
class Sandwich(object):
    def __init__(self, owner, bread='white'):
        self.owner = owner
        self.bread = bread
        self.toppings = []
    def __add__(self, topping):
        return self.toppings.append(topping)
```

Here, we add the magic method for addition to our class, and state that the ```+``` operator should append the argument `topping` that follows it to our list of toppings, then return that updated list.

#### Magic Methods - Subtracting


```python
class Sandwich(object):
    def __init__(self, owner, bread='white'):
        self.owner = owner
        self.bread = bread
        self.toppings = []
        
    # NEW CODE HERE
    def __add__(self, topping):
        return self.toppings.append(topping)
    def __sub__(self, topping):
        if topping in self.toppings:
            return self.toppings.remove(topping)
        else:
            print("Topping not present, and can't be removed.")
```

Subtracting is trickier, but we need to declare that the ```-``` operator should check for a topping in our list, and remove it if present. We then use the `.remove` method that is associated with all `list` objects to remove all toppings with the value given to the `topping` argument.

#### Magic Methods - (In)Equality


```python
class Sandwich(object):
    def __init__(self, owner, bread='white'):
        self.owner = owner
        self.bread = bread
        self.toppings = []
    def __add__(self, topping):
        return self.toppings.append(topping)
    def __sub__(self, topping):
        if topping in self.toppings:
            return self.toppings.remove(topping)
        else:
            print("Topping not present, and can't be removed.")
            
    # NEW CODE HERE
    def __eq__(self, other):
        if (self.bread==other.bread) and 
          (sorted(self.toppings) == sorted(other.toppings)):
            return True
        else:
            return False
    def __ne__(self, other):
        return not (self == other)
```

Note that we have to declare both ``==`` and ``!=`` through their magic methods. Also, it is worth mentioning that we use the name of the magic method from the table above, and not the symbol itself in order to define the method associated with these symbols for our class objects. Thus, `+` is defined as `__add__`, `-` as `__sub__`, and `==` and `!=` are `__eq__` and `__ne__`, respectively.


#### Magic Methods - Strings

Finally, we need to describe a way in which our class can be represented as a string. This will help us to not have to see anything that looks like

```
<__main__.Sandwich object at 0x7f7a445d3080>
```

when we try to print our variable. This might be useful to someone, but that someone is not me (and probably isn't you, either!). We can define this representation using the `__repr__` magic method. This will be applied whenever we simply type the name of the class instance into a cell and run it, or when we use the `print()` function to print out our class instance.


```python
class Sandwich(object):
    def __init__(self, owner, bread='white'):
        self.owner = owner
        self.bread = bread
        self.toppings = []
    def __add__(self, topping):
        return self.toppings.append(topping)
    def __sub__(self, topping):
        if topping in self.toppings:
            return self.toppings.remove(topping)
        else:
            print("Topping not present, and can't be removed.")
    def __eq__(self, other):
        if (self.bread==other.bread) and (sorted(self.toppings) == sorted(other.toppings)):
            return True
        else:
            return False
    def __ne__(self, other):
        return not (self == other)
    def __repr__(self):
        alltops = "Toppings:\t"
        for i in self.toppings:
            alltops += " %s" % i
        return "Owner:\t\t "+ str(self.owner) +"\n" + alltops + "\nBread:\t\t " + self.bread
```

Now we can print our sandwich!

### More Methods (Muggle Methods?)

We can also create methods that are based on the unique functionality of our class of objects. These methods won't be associated with predetermined symbols, and will look much more like our functions from last lesson. Since we are [pretending to be] working at a store, we might care about pricing a given sandwich.
- Let's call the method ``get_price``, and have it take two arguments (`self` and a `discount`) with `discount` having a default value of ``0``, and store ``price`` as an attribute of our sandwich object
- Each topping costs $1
- Specialty bread (not white bread) is $2, white bread is provided at no cost

One way to create this functionality is as follows:


```python
class Sandwich(object):
    def __init__(self, owner, bread='white'):
        self.owner = owner
        self.bread = bread
        self.toppings = []
    def __add__(self, topping):
        return self.toppings.append(topping)
    def __sub__(self, topping):
        if topping in self.toppings:
            return self.toppings.remove(topping)
        else:
            print("Topping not present, and can't be removed.")
    def __eq__(self, other):
        if (self.bread==other.bread) and (sorted(self.toppings) == sorted(other.toppings)):
            return True
        else:
            return False
    def __ne__(self, other):
        return not (self == other)
    def __repr__(self):
        alltops = "Toppings:\t"
        for i in self.toppings:
            alltops += " %s" % i
        return "Owner:\t\t "+ str(self.owner) +"\n" + alltops + "\nBread:\t\t " + self.bread
    
    # NEW CODE HERE
    def get_price(self, discount=0.0):
        self.price = 0
        for i in self.toppings:
            self.price += 1
        if self.bread != 'white':
            self.price += 2
        if discount > 0:
            self.price *= (1-discount)
        return self.price
```

Now, we can use our new method by simply calling the method attached to a `Sandwich` object, like this:




```python
mySand = Sandwich('Dusty')
mySand + 'chicken'
mySand + 'lettuce'
mySand + 'avocados'

mySand.get_price(discount=0.1) # apply a 10% discount
```






Thus, the sandwich we just made would have a price of \$2.70! 

## Documentation
 
 When creating a class, a function, or a method, we should always be sure to **document** that object! Documentation will save us, not to mention other future users of our code, from having to read the code line-by-line in order to understand how the code functions. We as authors can then remember how to use it after long breaks, and we can share our code with others looking to perform similar tasks.

The best way to document classes and functions in Python is by modifying the *docstring* of that class or function. A docstring is the original use case for the triple quotes that we occasionally use to denote multi-line strings. We can put these strings just inside of a class or function in order to document the functionality of that class or function. Let's look at some possible docstrings for the `Sandwich` class we have created in this lesson:


```python
class Sandwich(object):
    """A class defining a sandwich. Toppings can be added
    and removed, and the owner and bread type can be 
    declared upon initiation.

    Attributes:
    owner (str): the person puchasing the sandwich
    bread (str): the type of bread to be used
    toppings (list): a list of the toppings (str) that
      are to be put on the sandwich
    price (float): the price of the sandwich
    """
    
    def __init__(self, owner, bread='white'):
        self.owner = owner
        self.bread = bread
        self.toppings = []
    
    def __add__(self, topping):
        return self.toppings.append(topping)
    
    def __sub__(self, topping):
        if topping in self.toppings:
            return self.toppings.remove(topping)
        else:
            print("Topping not present, and can't be removed.")
    
    def __eq__(self, other):
        if (self.bread==other.bread) and (sorted(self.toppings) == sorted(other.toppings)):
            return True
        else:
            return False
    
    def __ne__(self, other):
        return not (self == other)
    
    def __repr__(self):
        alltops = "Toppings:\t"
        for i in self.toppings:
            alltops += " %s" % i
        return "Owner:\t\t "+ str(self.owner) +"\n" + alltops + "\nBread:\t\t " + self.bread
    
    def get_price(self, discount=0.0):
        """A function to calculate the price of the sandwich.
        Each topping costs $1, and bread that is not 'white'
        costs $2. Discounts should be applied as the amount
        to be deducted.

        Inputs:
          discount (float): amount to be discounted from 
            total price

        Returns:
          A Sandwich object with a price attribute
        """
        self.price = 0
        for i in self.toppings:
            self.price += 1
        if self.bread != 'white':
            self.price += 2
        if discount > 0:
            self.price *= (1-discount)
        return self.price
```

This enables us to use the `help()` function to learn more about our object, and for others who have imported it to do the same!


```python
help(Sandwich)
```

At this point, we are ready to start using our `Sandwich` class objects!

## Extra Practice (totally optional)


Create your own ``ComplexNumber`` class!
1. Complex numbers have a real and an imaginary part. The ``__init__()`` method should therefore accept two numbers. Store the first as self.real and the second as self.imag.
2. Implement a ``conjugate()`` method that returns the object's complex conjugate (as a new ``ComplexNumber`` object). Recall that $x = a + bi \implies \bar{x} = a - bi$, where $\bar{x}$ is the complex conjugate of $x$.
3. Add the following magic methods to your `ComplexNumber` class:
 	- ``__abs__()`` determines the output of the builtin ``abs()`` function (absolute value). Implement ``__abs__()`` so that it returns the magnitude of the complex number. Recall that $|a + bi| = \sqrt{a^2 + b^2}$.
 	- Implement ``__lt__()`` and ``__gt__()`` so that ``ComplexNumber`` objects can be compared by their magnitudes. That is, $(a + bi) < (c + di)$ if and only if $|a + bi| < |c + di|$, and so on.
4. Add the following magic methods to your `ComplexNumber` class:
   - Implement ``__eq__()`` and ``__ne__()`` so that two ``ComplexNumber`` objects are equal if and only if they have the same real and imaginary parts.
 	-  Implement ``__add__()``, ``__sub__()``, ``__mul__()``, and ``__div__()`` appropriately. Each of these should return a new ``ComplexNumber`` object.

ANSWER:

```python
import math

class ComplexNumber(object):
  def __init__(self, real, imag):
    self.real = real
    self.imag = imag
  
  def conjugate(self):
    return ComplexNumber(self.real, -1*self.imag)

  def __abs__(self):
    return math.sqrt(self.real**2 + self.imag**2)

  def __lt__(self, other):
    if self.__abs__()<other.__abs__():
      return True
    else:
      return False
  
  def __gt__(self, other):
    if self.__abs__()>other.__abs__():
      return True
    else:
      return False

  def __eq__(self, other):
    if self.real==other.real and self.imag==other.imag:
      return True
    else:
      return False
  
  def __ne__(self, other):
    return not self==other

  def __add__(self, other):
    return ComplexNumber(self.real + other.real, self.imag + other.imag)

  def __sub__(self, other):
    return ComplexNumber(self.real - other.real, self.imag - other.imag)

  def __mul__(self, other):
    return ComplexNumber(
      self.real*self.other - self.imag*other.imag,
      self.real*other.imag + self.imag*other.real
      )

  def __div__(self, other):
    return ComplexNumber(
      (self.real*other.real + self.imag*other.imag)/(other.real**2 + other.imag**2),
      (self.imag*other.real - self.real*other.imag)/(other.real**2 + other.imag**2)
    )
```

**Solve it:**

Classes provide a great way to bundle information and functions. We will create a class called "StudentRecord" to record student academic information:

1. The class should contain attributes for recording
    - "firstName", "lastName" to store First and Last names separately
    - "dob" to store the student's Date of Birth
    - "hsName", "hsCity", "hsState" to store High School name, city, and state information
    - "degree" to store student's chosen Degree program
    - "address" to store a string of the student's Address
    - "transcript" to store a student's Grade history. This should be of a type that allows the storage of the course name "course", grade in the course "grade", the number of credits assigned to the course "credits", and the semester and year taken ("semester" and "year").
2. The class should accept information for all variables listed above upon creation.
3. The class should include the following methods: 
    - "cumGPA" to return a float value of cumulative GPA
    - "semGPA" to return a float value of semester GPA
    - "credits" to count the number of credits a student has accumulated, and return that number as a float
    - "newCourse" to add a course to the grade history
    - "scholarship" to determine scholarship eligibility based on the following cumulative GPA cutoffs:
        - 3.9 for a full-ride,
        - 3.63 for a half-tuition scholarship, and
        - 3.3 for a 1/4 tuition scholarship.
        - All GPA’s below the minimum scholarship cutoff receive no reward.
        - The method should return a string of
            - "Full-ride"
            - "Half-tuition"
            - "Quarter-tuition"
            - "Not Eligible"
 

Hint: You might want to create a separate class to handle courses that can be added to the transcript!

Insert code to be graded into the cell below $\downarrow \downarrow \downarrow$

