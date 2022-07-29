# Week 1 - Data Types

## Why do I need to know this?

Programming is a way to allow us as humans to manipulate information (data) on a scale much larger than we would otherwise be able to handle. Speaking anecdotally, on a good day my brain is able to handle one mathematical operation per second. I can remember a few things at once, and a few more things if I spend a while memorizing them. On the other hand, my laptop can handle millions of mathematical operations per second, and can "memorize" the contents of a spreadsheet fast enough that to me it feels instantaneous. When we use Python, we are accessing the amped up computational power provided by our computers to enable us to focus on thinking critically, and letting our computer handle the rest.

How do computers handle data? At the most basic level, it all gets digested into the same form: 1s and 0s. Were we to attempt a very complete treatment of information and computation, we would need to start there. Suffice it to say that computers need all information to be concrete, and that information that cannot be quantified or written in a fixed form is no good.

Instead of starting with binary values (the 1s and 0s above), we have the privilege of experiencing our interactions with computers through a high-level programming language: Python. High-level is an indication that the programming language is closer to a human-readable form than a computer-readable form. While we are working furiously to do our work writing in Python, the computer is translating everything that we say (in Python) to machine-speak. High-level code is slower to run than low-level (easier for machines to translate) code, but we accept that tradeoff in order to minimize the time and effort we spend in writing our code.

Writing Python code is MUCH easier than writing code in just about any other language. Trust me.

## Then how do I start?

The first thing that we need to understand when we start to interact with Python is the language's ability to represent different kinds of information. The types of information that can be stored, and the ways in which we can store them, inform the choices that we will make as we begin to programmatically handle the information that is available to us. Think of each method of storing information as storage bins like you might find in a kitchen: one bin is intended to hold sugar, another flour, and another rice. Sure, you could insist on putting rice in the sugar bin, but the next chef to use the kitchen might not appreciate your choice. In programming, we should look for the appropriate storage bin for the information that we are dealing with in any specific context

In programming, we label the different storage bins **data types**.

A data type is an **object** (we will discuss this more later) that is designed to handle a specific kind of information. Let's take a look at a few different types:

## Variables

In Python, we can work with data as if the Python interpreter (the thing that runs our code) were a fancy calculator, and we can just type all the information we need into the interpreter each time we run code. This is not feasible, however, for larger projects. In those cases, we store information in what are called **variables**.

Any data type can be stored as a variable. The names we give these variables are nearly infinite. There are a few rules and guidelines (rules will be bolded) on how we should name them, though:
- **Names cannot start with numbers**
- Names should be lower case
- **Names can include letters, numbers, and underscores**
- Names should be descriptive
- Names should not be reserved words

We store information as a variable in the following way:


```python
mySentence = "This is my first variable!"
```

We have now indicated to Python that it should remember (until further notice or the end of our program) that `mySentence` is a variable containing the value `"This is my first variable!"`. We can ask Python to provide this variable for us as we continue to create code. Outside of exercises, we will not store information as variables during this class period.

## Numbers

There are several different data types to handle numbers. Let's talk about **integers** and **floating-point numbers**. One really cool thing about Python is that it tries to do the work of switching between integer and floating point numbers for us as we do different calculations requiring one or the other. Let's explore briefly how each one works.

### Integers

**Integers** represent whole numbers, and _cannot_ represent any number with a decimal. We can perform simple operations using our arithmetic operators (+,-,\*,\/).


```python
2 + 2
```







```python
87 - 10
```







```python
5 / 1
```







```python
8 * 3
```






It is interesting to note that division resulted in a floating-point number. This allows us to divide integers, even when the result will not be an integer itself, and adds convenience to our mathematical functions. Python also allows us to mandate that the result of division be an integer by using the \/\/ operator. Note the different outputs below:


```python
# True divison operator
5 / 2
```







```python
# Floor division operator
5 // 2
```






We can also perform exponentiation by using the \*\* operator:


```python
5 ** 2
```






Finally, we can attempt to force values to become integers by using the `int()` command, though not all values can be made into integers:


```python
int(37.5)
```







```python
int(True)
```







```python
int(False)
```







```python
int("text")
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    <ipython-input-14-f3a57c1fa0db> in <module>
    ----> 1 int("text")
    

    ValueError: invalid literal for int() with base 10: 'text'


### Floating-Point Numbers

Floating point numbers are typically called **floats**, and allow us to make use of decimal numbers in order to increase the precision of our computations. Floats are probably the most common type of number you will work with, since most mathematical operations cannot be guaranteed to result in integers. Floats can use all of the same arithmetic operators as integers, and can be used in combination with integers when using those operators:


```python
2 + 2.5
```







```python
87.0 - 100.5
```







```python
10 / 3.5
```







```python
5.3 // 1.2
```







```python
9.99 * 5
```







```python
3.1415 ** 2
```






We can convert numbers and other values to floats by using the `float()` function to **coerce** the value to become a float-type object:


```python
float(1)
```







```python
float(False)
```







```python
float("text")
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    <ipython-input-23-7f533111535f> in <module>
    ----> 1 float("text")
    

    ValueError: could not convert string to float: 'text'


**Solve it**

Use python to calculate the volume of a sphere with radius 8. Remember that the volume of a sphere can be calculated by using the formula $$\frac{4}{3} \pi \cdot r^3 $$ and $\pi$ can be approximated as 3.141593.

Store the solution as a variable named `vol`.


## Boolean Values

A boolean object can take one of two values: true or false. This allows us to represent binary cases of truth, and to provide "on/off" switches in many different contexts. It is important to note that most objects in Python can be reduced to boolean values:


```python
bool(1)
```







```python
bool(0)
```







```python
bool("text")
```







```python
bool("")
```







```python
bool(None)
```






Boolean values are typically used to evaluate logical statements as either true or false, and are often experienced in the context of comparisons of equality or magnitude. In order to make these comparisons, we introduce new operators to our vocabulary: \>, \<, \=\=, \!\=, \&, \| are the most common, although many others exist.


```python
# Testing for Equality of values
"text" == "Text"
```






Note: strings are case sensitive when testing equality!


```python
300 == 45+255
```







```python
# Testing Inequalities
10 < 100
```







```python
10 > 100
```







```python
# We can also test for "less than or equal to" conditions:
10 <= 11
```







```python
11 <= 11
```







```python
# Inequality

42 != "the meaning of life, the universe, and everything"
```







```python
# Match multiple conditions

(42 == 10 + 32) & ("other text" != "other text") # False because one condition is not met
```







```python
(42 == 10 + 32) & ("text" != "other text")
```







```python
# Match one or more conditions

(42 == 10 + 32) | ("other text" != "other text") # False because one condition is not met
```







```python
(42 == 10 + 32) | ("text" != "other text")
```






**Solve it**

Write a logical expression to determine if the volume of the sphere with radius 8 is greater than the volume of the cube with edge length 12.

Store the solution as a variable named `sphereOrCube`.



**Solve it**

Write a logical expression to determine if the string "hei" is the same as the string "Hei"

Store the solution as a variable named `twinStrings`.





    False



## Strings

Strings are the data type in Python that is used to store text data, or data that does not fit into other categories and can be best represented as text in some form. This might be text values proxying for job types, it might be sentences written in a document, or it might be a single character, like "e". Strings are immensely valuable for creating dense data, and have many built-in features (we call them **methods**) to improve our ability to handle strings. First, we create a string by putting some characters inside of quotation marks. 

### Choosing Quotation Marks

The quotation marks indicating the start and end of strings can be \" or \'. It is worth choosing carefully, however, because the quotation marks we use to denote a string limit the characters that we can place inside. If I use \", then double quotes cannot be used within my string (while single quotes can!). Conversely, using \' to start and end a string means that we cannot use single quotes (often used to mark apostrophes within contractions in the English language) inside of our string.


```python
"this is a string"
```







```python
"this is a string with a 'quote' inside of it"
```







```python
'also a string'
```







```python
# a broken string where single quotes are used to mark the string and also within the string itself

'a broken string y'all'
```


      File "<ipython-input-52-5213d5ca4357>", line 3
        'a broken string y'all'
                             ^
    SyntaxError: invalid syntax



Strings can typically only be used on a single line, so that I cannot do the following:


```python
"my string starts here

and ends here"
```


      File "<ipython-input-54-77ff0ba3a188>", line 1
        "my string starts here
                              ^
    SyntaxError: EOL while scanning string literal



Special quotation marks can be used to create multiline strings. We use a triple quote system for this, where we mark the start or end of the string with three quotes (can be single or double):


```python
"""my string starts here

and ends here"""
```






Our string now contains some **escape characters** (\\n) that mark where one line ends and the next begins, allowing us to handle text that spans multiple lines. We can even use this to store information like SQL queries that have been formatted for readability!


```python
'''
SELECT
    *
FROM
    database
WHERE
    column > 0
'''
```






### Operating on Strings

Strings can also be modified using operators and **methods**. We are already familiar with operators, and the applicable operators for strings are \+ and \*. Methods are **functions**, or pre-existing code that is associated with a specific type of object. First, the operators:


```python
"Add this string" + " " + "to another"
```







```python
"Repeat me!" * 3
```






Methods are called by name, rather than through an operator. Below are some useful methods for strings. Please note that there are MANY others (see [https://docs.python.org/3/library/stdtypes.html#string-methods](https://docs.python.org/3/library/stdtypes.html#string-methods) for more information)


```python
# Replacing characters within a string

"Bananas".replace("a", "o")
```







```python
# Converting a string to lower case

"ANGRY WORDS".lower()
```







```python
# Break a string apart based on a designated character

"Make me into many strings".split(" ")
```







```python
"    too much whitespace!   ".strip()
```






**Solve it**

Complete the following sentence by using the `replace` method to replace each "\_\_x\_\_" string with a fitting word. Feel free to be silly!

If you want to have some fun, choose words before reading the sentence. You will need (in order):
- Adjective
- Adjective
- Noun
- Noun
- Name of an Animal
- Name of a Game

Store the resulting sentence as a variable named `myMadLib`.


```python
myMadLib = """
A vacation is when you take a trip to some __1__ place 
with your __2__ family. Usually you go to some place that 
is near a(n) __3__ or up on a(n) __4__. A good vacation 
place is one where you can ride __5__ or play __6__.
"""
```

## Lists

Lists are the first of several data types that allow us to organize and store many different values within them. A list, as its name suggests, is an object in which a _list_ of values are stored. Each value can then be accessed by its position within the list.

**REALLY IMPORTANT**: Positions in Python (and almost all programming languages) begin counting at 0, so that the first thing in a list is the 0th thing in the list. To remember this, remember that the first element in a list is ZERO elements removed from the start. We are counting how far from the start of the list we are, and the distance between the first element in a list and itself is 0! 

So how do we make a list? with \[ \] characters marking the start and end of the list, respectively, and with commas (,) in between the elements.


```python
# Handwrite a list

[ 0, 1, 2, 3, 4 ]
```







```python
# Use list comprehensions to make a list

[x for x in range(10)]
```







```python
# Make a list from a string

"Make me into many strings".split(" ")
```






### What's in a list?

Anything! Lists can consist of numbers, strings, boolean values, or other lists, and more! They can contain these elements in any order or combination.


```python
["a number", 3, ["another list", "with three strings", "inside the first one!"]]
```






### Finding elements of a list

Within a list, we can use **slicing** to find specific elements or to reference a specific position within a list. First, let's make a list to play with by **storing** a list. We can **store** a list (or any other object) in memory by assigning it a name using the \= symbol. After we have given an object a name, we can refer to that object by its name whenever we want to make use of the object. There are some simple rules for naming things in Python:

- Variable names must consist of letters, numbers, and underscores only. 
- Periods CANNOT be part of variable names (helpful advice for any recovering R users out there...)
- Variable names typically begin with lower case letters, and CANNOT begin with numbers.
- If you want to use multiple words in a variable name, separate the words with underscores (\_) or by capitalizing all but the first word (called **camel casing**)
- While you can use any word you want for a variable's name, you should avoid [reserve words](https://stackoverflow.com/questions/22864221/is-the-list-of-python-reserved-words-and-builtins-available-in-a-library) wherever possible.


```python
firstList = [x for x in range(10)]
```

Now that we have created and stored a list, let's **slice** it up! When **slicing**, we will use the variable name followed by square brackets (\[ and \]) with values in between them to denote what we want to extract from the list. To get the first element in our stored list, we can use the following code:


```python
firstList[0]
```






Remember, lists are **zero-indexed** (the first thing is the 0th thing)! We can also grab more than one element at a time. Our list currently has 10 elements (you can see the whole list by removing the slicing notation from the line above and running the line again), but we might want to extract the first 5.


```python
firstList[0:5]
```






When we use notation like `[0:5]`, we are explaining to python that we want all elements beginning with the 0th element, but whose position is less than 5. This will retrieve elements 0, 1, 2, 3, and 4, as you can see from our output. We can also write with fewer characters, and use equivalent notation like `[:5]`.

**Question**: If `[:5]` gets everything from the start of the list until the 5th element, what do you think that `[5:]` would provide?


```python
firstList[5:]
```






That's right! `[5:]` will extract the elements from the 6th position (6-1=5) to the end of the list. This comes in REALLY handy when we may not know ahead of time how many elements are in a list, but we still need to tell Python what to do. We can even do some fancy footwork, and have our slicing syntax help us grab every other element from the list, rather than all the elements!


```python
firstList[::2] # or firstList[0::2] or firstList[0:10:2] -- All three commands are equivalent for our list
```






Pretty awesome, right?

### List operators and methods

Lists can use the operators \+ and \*, similar to strings. The \+ operator can be used to **concatenate** two lists together, and the \* operator can be used to repeat a list, just like with strings:


```python
firstList + ['textGoesHere', 'moreTextHere']
```







```python
firstList*2
```






Lists have many useful methods to supplement their functionality. We can use methods to sort lists, add elements, remove elements, find unique values, and much more. For a list of the built-in methods, see [https://docs.python.org/3/tutorial/datastructures.html#more-on-lists](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists).


```python
# Add an element to the end of a list - WARNING!! THIS WILL CHANGE YOUR STORED LIST!

firstList.append(11)
```


```python
# Remove an element from the end of a list - WARNING!! THIS WILL CHANGE YOUR STORED LIST!

firstList.pop()
```







```python
# Sort a list - WARNING!! THIS WILL CHANGE YOUR STORED LIST!

firstList.sort()
```


```python
# Sort a list - WARNING!! THIS WILL CHANGE YOUR STORED LIST!

firstList.reverse()
```


```python
# Find the length of a list (or of strings, or other data types of arbitrary length)

len(firstList)
```






**Solve it**

Write a list containing all numbers up to 50, where each odd number is negative, and each even number is positive. *Hint: the [modulo operator](https://www.educative.io/edpresso/what-is-a-modulo-operator-in-python) will be really helpful!*

Store the resulting list as a variable named `oddsOrEvens`.


## Dictionaries



Dictionaries are powerful objects that do many of the same things as lists, but also include their own nice set of features, making them easier to deal with than lists in many contexts. Like lists, dictionaries can store any number of elements of more or less any type. You can store numbers, strings, lists, and dictionaries within a dictionary (among many other things).

Remember that a list is created to be used in order (using the position of their elements as the way to reference the information stored within the list). Dictionaries have a different structure. Every element of a dictionary is stored in what is called a **key-value pair**. 

**Key-value pair** refers to the fact that every element in a dictionary is assigned a name (a **key**) which is then associated with the **value** to be stored within the dictionary. When we want to find a specific element within a dictionary, we access it by providing the **key** that pairs with the value that we are interested in.

Let's create a dictionary called `studentRecord`, and put some information about an imaginary student inside of it. We will store the student's name, age, and GPA.


```python
studentRecord = {
    'name' : 'Dusty White',
    'age' : 32,
    'GPA' : 3.45
}
```

When we want to reference a single value from our dictionary, we can do so by providing the key that corresponds to the value we would like to extract within square brackets (\[ \]).


```python
studentRecord['age']
```






Let's update this record to contain a list of courses taken by the student:


```python
studentRecord['courseHistory'] = ["Econ", "Math", "Chem"]
```

Now, when we look at the entire dictionary, we will see the following:


```python
studentRecord
```






If we want to reference the second course taken by the student, we can use multiple levels of indexing. First, we reference the key associated with the course list, and then we reference the position of the second course within the list:


```python
studentRecord['courseHistory'][1]
```






Notice how we can treat the `"courseHistory"` value in our dictionary as if it were a list, because it is actually a list stored within the dictionary. Whenever an object is stored as part of another object, when we reference the internal object, we can treat it just like we would have treated it even if it were not part of something else! This makes dictionaries and lists into VERY powerful tools, that can organize and store large amounts of related information for future retrieval!

### Dictionary Methods

Dictionaries, due to their structure, are typically not operated on directly using operators (like we have done with other object types). The most important methods associated with dictionaries are related to retrieving the keys of the dictionary, the values of the dictionary, and extracting key-value pairs:


```python
# Extract keys only

studentRecord.keys()
```







```python
# Extract items only

studentRecord.values()
```







```python
# Extract key-value pairs

studentRecord.items()
```






**Solve it**

Create a dictionary to store information about a purchase at a clothing store that contains the following keys and values:
- A "name" key that corresponds to the name of the buyer
- An "items" key that corresponds to a **list** of items purchased
- A "discount" key that corresponds to a **boolean** value indicating whether or not the buyer received a discount on the purchase
- A "price" key that corresponds to the price that the buyer paid for the purchase as a whole.

Store the resulting dictionary as a variable named `receipt`.



## Up Next: Loops and Functions

At this point, we know enough about objects in Python to start getting to work! Next week, we will work on using the different objects that we have experienced so far to start building more powerful functionality by incorporating loops and functions into our programming vocabulary!
