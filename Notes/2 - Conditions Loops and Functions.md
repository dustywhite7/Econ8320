# Conditions and Loops

## Why do I need to know this?

Programming, at it's heart, is about being able to reduce the amount of work it takes to accomplish a task. In manufacturing, this would look like building a machine that can accomplish portions of a task with less human effort. By reducing the amount of work that we have to put into a process, we free ourselves up to focus on the tasks that are not so easily accomplished by anyone besides a competent human being (us). 

Think of a program as really tiny machinery. Your goal is to make a machine (in code) that can accomplish routine tasks for you. When you're done, you get to focus on other important tasks that demand your attention. For example, you might want to spend your time working on a forecast model, but first you need to check to make sure that all values in your time series are valid. You COULD just open up your data, and look at every record to make sure that each fits the rules that valid data should follow. Or you could write a program that can check every line for you, and either alert you to problems, or possibly fix them without you even having to be involved. Then, all of your time is freed for the forecasting model.

Last week we talked about some of the types of information that we can store in Python. This week, we will start to learn about the tools that are baked into Python that allow us to begin the process of automation.

## Conditions

We have used conditions a few times already, but it is time to talk seriously about conditions and logical statements in Python. If you haven't noticed this yet, you will soon note that Python (and all other programming languages) are VERY literal. Things that we don't intend will occur whenever we assume that a computer will interpret an ambiguous statement in a single anticipated (by humans) way. Eventually, you will get used to being very careful when describing conditions in your code, and these problems will become less of an issue.

In Python, we have keywords that we can use to express different kinds of logic. Let's get started by talking about `if` statements. `if` statements function in Python pretty much the same way that they do in English: you state a condition, and then explain what should happen if that condition is met. You can then list alternative outcomes with the conditions that should be met prior to implementing those contingency plans. Finally, you can list what to do in any other outcomes that were not explicity described. Let's try this out:


```python
x = 150

if x > 100:
    print("Whoa, that's a big one!")
```

When we utilize conditions like the example above, every statement depends on the result of the evaluation of a **logical statement**. In this case, the **logical statement** is `x > 100`. This statement has a result that is a boolean value, as we can see if we ask Python to evaluate it as a standalone statement:


```python
x > 100
```






When we use `if` statements, we will *always* need logical statements. We can write the logical statement inline, like we just did, or we can evaluate the truth of any prior statement. Let's look at another helpful example of an `if` statement using existing values:


```python
x = 150
y = 200

xBigger = x > y
xBig = x > 100

if xBig & xBigger:
    print("That is a REALLY big number")
elif xBig:
    print("x is big, but not THAT big")
else:
    print("x isn't really that big")
```

Here we take two numbers (`x` and `y`), and use two logical statements (`x > y` and `x > 100`) to evaluate several possible outcomes. First, we check if both conditions are true using the statement `xBig & xBigger`. If both are `True`, then we print the statement assigned to the `if` block.

Next, we incorporate the keyword `elif`. `elif` is a keyword that *continues* an `if` statement. It tells Python to evaluate it's truthiness if the condition above it fails. In other words, the `elif` statement is only evaluated in this case when `xBig & xBigger` is `False`. If the `elif` statement is evaluated as `True`, then its assigned print statement is executed and we skip the `else` block that follows.

If the `elif` statement is *also* `False`, then we reach the `else` statement, which is automatically executed and prints the final print statement. `else` indicates that the code should associated with it should be run when all previous logical statements in the block are evaluated as `False`. It will not run if *any* of the previous statements evaluate as `True`.

When writing logical blocks, we always write our code in the following order: 

1) Write an `if` statement, and its corresponding code block 

2) If needed, write as many `elif` statements as needed, along with their corresponding code blocks. **NOTE**: `elif` statements will be evaluated from top to bottom in the code, and once a single `elif` statement is evaluated as `True`, none of the subsequent `elif` statements will be evaluated. Put your `elif` statements in the order that you want them to be prioritized! 

3) If needed, write an `else` statement that will apply to all events not covered by `if` or `elif` statements

**Solve it**: (from *The Python Workbook*)

The following table lists the sound level in decibels for several common noises.

| Noise | Decibel Level (dB) |
|---|---|
| Jackhammer | 130 |
| Gas Lawnmower | 106 |
| Alarm Clock | 70 |
| Quiet Room | 40 |


In the cell below, write code that reads a sound level in decibels from the user. If the user
enters a decibel level that matches one of the noises in the table then your program should display a message containing only that noise. If the user enters a number of decibels between the noises listed then your program should display a message indicating which noises the level is between. Ensure that your program also generates reasonable output for a value smaller than the quietest noise in the table, and for a value larger than the loudest noise in the table.



**Solve it**:

In the cell below, write a set of conditions that will check the value of `x`, then print the word for any number from 0 to 10 in Finnish:
nolla [0], yksi [1], kaksi [2], kolme [3], neljä [4], viisi [5], kuusi [6], seitsemän [7], kahdeksan [8], yhdeksän [9], and kymmenen [10].

If the number is outside of this range, then just print "out of range!"


## Loops

Just a minute ago, we thought about a problem where we might need to check each record in a data set for valid entries. If we want to accomplish this kind of task, we need to write code that will check the first line, then the second line, then the third line, etc. We can do this by hand, of course. Imagine a list of entries stored in the variable `forecastData`, where we need to make sure that each record is above 40 but below 50. Checking each value manually for validity might look something like the code below:


```python
forecastData = [49.5, 40.2, 53.7, 48.9, 51.0]

if (forecastData[0] > 40) & (forecastData[0] < 50):
    print(True)
else:
    print(False)
    
if (forecastData[1] > 40) & (forecastData[1] < 50):
    print(True)
else:
    print(False)
    
if (forecastData[2] > 40) & (forecastData[2] < 50):
    print(True)
else:
    print(False)
    
if (forecastData[3] > 40) & (forecastData[3] < 50):
    print(True)
else:
    print(False)
    
if (forecastData[4] > 40) & (forecastData[4] < 50):
    print(True)
else:
    print(False)
```

That is a LOT of redundant code. Does it work? Sure. But what happens when I need to fix it? As I typed those lines, I did some copying and pasting, and then noticed that I made a few typos. At that point, I had to fix the typos and then copy and paste the corrected code again. Not ideal, but functional. Then I did it again! And again, it was frustrating to fix each of the iterations of the code.

While convenience is important, it is also much more likely when I am copying and pasting code over and over that I will make mistakes than if I just have to write one version of the code that would work for each of the lines of my list.

What we are doing when we write logic like the code above is called **looping**. We are writing code that will iteratively work its way through each specified record, and will **loop** through the same logic for each of those records. Wouldn't it be easier if we could just specify the pattern of behavior we expect, and not have to walk our program through each specific iteration?

Yes. Yes it would.

### For Loops

The most common type of loop used in Python is a `for` loop. They are convenient and safe, as you will soon learn. Let's write a loop for the problem above.


```python
forecastData = [49.5, 40.2, 53.7, 48.9, 51.0]

for i in forecastData:
    if (i > 40) & (i < 50):
        print(True)
    else:
        print(False)
```

That was way easier! But really, what did we just do?

The structure of our `for` loop above is the standard format. It translates to English in the following way: "For every element (call it `i`) in the object `forecastData`, do the following:". We even end it with a colon like we would in English!

`i` becomes a **placeholder**, or a variable that will be temporarily assigned each time our loop goes to work. It will use each entry in `forecastData` one time, and while a given entry is being used, it will have the nickname `i`. That way, we can write all the code in our loop to describe what should happen to `i`. Then, in each pass of the loop, `i` takes the next value, and we follow the same set of instructions. In this case, we are just checking that our variables meet the established criteria, and then printing `True` if they do, or `False` if they don't.

One awesome side effect of this version of loops is that we can easily update our loop if there is a mistake or change to the pattern, and we only have to do so ONE time! No copying and pasting, and less risk of accidental errors popping up in our code.

**Solve it**:

Write a for loop that will concatenate and then print out each word in the following list one by one:
`["A","Long","Time","Ago","In","A","Galaxy","Far","Far","Away"]`


### List Comprehensions

Another great way to write a for loop is to use **list comprehensions**, or lists containing loop syntax that can generate a list as a result of the loop! It is a compact and effective way to get your concept into list form:


```python
forecastData = [49.5, 40.2, 53.7, 48.9, 51.0]

# Use a list comprehension to evaluate the conditions from our old for loop
meetsCondition = [(i > 40) & (i < 50) for i in forecastData]

print(meetsCondition)
```

In this list comprehension, we are able to use a *single line* to write out our previous `for` loop, and then we can simply print our results by printing out the list itself. List comprehensions can provide us a quick way to make all sorts of lists:


```python
# Make a list of integers from 0 to 9
quickList = [i for i in range(10)]

print("List from 0 to 9", quickList, "\n")

# Make a list that prints all numbers divisible by 3

anotherList = [i for i in range(100) if i%3==0]

print("List of multiples of 3", anotherList)
```

As we can see from that second example, we can even include statements that allow us to use `if` statements and control which elements are included within our list comprehension.

Comprehensions are frequently used to streamline code, and can make our work much easier to read if a for statement is simply intended to transform data based on a fixed pattern for all elements in an existing list or other iterable.

**Solve it**:

Write a list comprehension to find all numbers between 0 and 1000 with the number 4 in them, and store the resulting list as the variable `fours`


### While Loops

Another kind of loop that is used in some contexts is a `while` loop. `while` loops differ significantly from `for` loops in their intended use: a `for` loop is designed to execute a determined number of iterations, whereas a `while` loop is designed to execute code repeatedly until a **stopping condition** is met. This means that we can allow a `while` loop to repeat indefinitely. 

A **stopping rule** is the logical statement that is checked before each iteration of a `while` loop. Whenever this condition is evaluated as `True`, then the loop is executed. When the condition is evaluated as `False`, the loop is terminated and the program advances to subsequent commands. This is where the term **infinite loop** comes from! If we forget to update our stopping condition within our `while` loop, then it will never stop, because we never tell it to stop. It is **really** important to remember this when we are writing `while` loops, or we will probably crash our program if not our computer.

A fun example of a while loop would be writing a function to prompt the user to add numbers until the sum is above 42:


```python
total = 0
while (total<=42):
    total += float(input("Please enter a number:"))
    print(total)
```

In reality, we would probably use `while` loops for significantly more difficult problems than our toy example. `while` loops are valuable in cases where we are seeking convergence such as dynamic programming, search models, and optimization problems in the context of statistical models.

**Solve it**:

Write a while loop that takes `x` and subtracts 10 while `x` is still above 100.


# Functions

Functions are an excellent addition to our ability to generate reusable code, and can save us significant effort when we want to recycle code from one problem to the next. In fact, there will come a time later in this course where we will do very little programming that does not involve functions on just about every line of our code. Functions are where computer programs really get their strength, especially when used together with logical statements and loops to create simple instructions that we can use to perform complex tasks.

A function is created by using the keyword `def`, followed by the name of the new function we are creating. At the end of the name of the function, we place any the names of any values we want users to provide to our function within parentheses (`(` and `)`).

Let's start by creating a function that can calculate the circumference of any circle. It will require our user to provide the radius of the circle, since the circumference of a circle is $2\pi r$.


```python
def circumference(r):
    return 2*3.14159265*r
```

Our function starts just like we explained above. We declare a function named `circumference`, and in parentheses we ask the user to provide `r`, which we know is the radius of the circle. This `r` value is treated as a variable within our function, and we can refer to it by using `r` in our operations within the function.

The last line of any function should contain a `return` statement. This line tells our function what information to pass back to the program as a whole. It should typically be the final result of our function's operations.

When we **declare** a function, like we did above, we tell Python what to do if we ask for a function to be executed. The function is NOT executed, though! Python waits until we **call** a function, like we will do below:


```python
circumference(2)
```






We just **called** our `circumference` function with an `r` value of `2`. The function evaluates the circumference of the circle with radius 2, and returns the calculated value upon completion.

Let's write another fucntion, this time to calculate the *factorial* of a given number. A factorial is calculated as the product of an integer with all integers of smaller value. For example, $4!$ (4 factorial) is calculated as $4\times3\times2\times1$.


```python
def factorial(n):
    fac = 1
    while n > 0:
        fac *= n
        n -= 1
    return fac
```

This function takes a number `n`, and multiplies it by 1. Then, it subtracts 1 from `n`, and repeats the process so long as n is still greater than 0. We can confirm that it works properly by calling the function:


```python
factorial(5)
```






**Solve it**: (from *The Python Workbook*)

A prime number is an integer greater than 1 that is only divisible by one and itself. Write a function `isPrime` that determines whether or not its parameter is prime, returning True if it is, and False otherwise.



**Solve it**: (from *The Python Workbook*)

Write a function called `taxiPrice` that calculates taxi fares. The function should accept as an argument `distance`, which is the distance travelled by taxi (measured in km), and should return a price (just the number is fine, no currency symbol is needed). The fee schedule is a &euro;4.00 base fee, with a charge of &euro;0.25 for each 140m traveled.


### Recursive Functions

Another really helpful feature of functions is the ability to call a function within itself. This process is called **recursion**, and makes otherwise intractable problems straightforward. First, let's look at an example of our `factorial` function that has been rewritten as a recursive function:


```python
def factorial(n):
    if n <= 1:
        return 1
    else:
        return n*factorial(n-1)
```

Recursive functions increase our ability to write flexible programs at the cost of sometimes taking longer to read and interpret. The function above contains some very simple logic that allows us to calculate the same values as our old `factorial` function:

1) If `n` is less than or equal to 1, then we get back 1 as the resulting factorial. (Both 0 factorial and 1 factorial have a value of 1)

2) For any other number `n`, we just want to multiply that number times the factorial of `n-1`. For example, the value of $2!$ is $2\times 1!$, and the value of $3!$ is $3\times2!$.

Our program will continue to call `factorial(n-1)` until `n-1` is 1 or 0, at which point it will simply return the value `1`, and multiply each returned value back up the chain until we get our final result.

Recursive programs aren't always necessary, but they come in very handy where we need to explore conditions with unclear stopping points (recursive problems in dynamic programming are common in Economics, for example).

**Solve it**: 

Write a **recursive** function to calculate the n-th Fibonacci number. You should name your function `fib` and it should take one argument (`n`). It should return the Fibonnaci number corresponding to `n`.



### Why use functions?

When we use functions, we are able to write code in a single place that can be recycled anywhere in our code. We can even call functions from one script into another! This means that we only have to maintain a single block of code for each task we hope to implement in Python, and then we are able to use it over and over again.

The alternative to this is to write the same code over and over again. If we make a mistake, we have to fix it over and over again. If we update our code to improve functionality, we have to update it over and over again.

In short, functions save us effort in writing lines of code, updating lines of code, and fixing potential mistakes in our code.

## Commenting our code

It is important that, as we begin writing more and more complex code, we learn to leave explanations of our code. In the future, users of our code (future you, future me, and other users, as well!) will have an easier time understanding and updating the code if they can quickly grasp what we are attempting to do with that code.

The first way that we can comment code is by using the `#` symbol. Putting a `#` anywhere in a line of Python indicates that ALL text from that point until the end of the line is not code, but is a comment. These comments only last until the end of the line, at which point Python treats the text as code again.


```python
# This is a recursive function that calculates the factorial of n
def factorial(n):
    if n <= 1:
        return 1 # The return value for 0 and 1
    else:
        return n*factorial(n-1) # The return value for all numbers higher than 1
```

The comments provided above are helpful in understanding what is happening in our factorial code, but they are only visible while we are looking at the code itself. We would not be able to see those comments when we need help and are working in another script. Luckily, we also have ways to leave comments that are visible through the `help()` command at any time when working in Python.

**docstrings** enable us to leave messages that can be accessed by users when they need to remember what a function does and how it works. **docstrings** are called by using triple quotes `"""` at the beginning and end of the **docstring**.


```python
# This is a recursive function that calculates the factorial of n
def factorial(n):
    """
    factorial(n) takes an integer (n) as input
    and returns the mathematical factorial
    of that number.
    """
    if n <= 1:
        return 1 # The return value for 0 and 1
    else:
        return n*factorial(n-1) # The return value for all numbers higher than 1
```

Now, we can use the line `help(factorial)` to get some guidance on our `factorial` function:


```python
help(factorial)
```

### When should we leave comments in our code?

Always! We should comment ALL code that we write. This allows us to pick up where we left off when working on long-term projects, but also makes it easier to collaborate on projects with other programmers. If you ever want your code to be used by others, commenting will be a valuable tool for those users.

Comment your code when:
- You plan on using your code
- You might look at your code again at a different time
- Someone else might use your code
- Someone else might update your code
- Someone else might need to read your code

In other words, always comment your code.
