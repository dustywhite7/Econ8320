# Numeric Python (NumPy) and Scientific Python (SciPy)


## Arrays and Math

A while back, we created some matrix code using lists. This "works" in the sense that it is possible for us to construct matrices using lists, and it is possible for us to write code to do calculations with them. We have not yet tried to do any real computation with those tools, however. Doing so will make us regret our choice to implement matrix operations using lists. We will wish that there were a better way to do complex operations without the headaches of checking, rechecking, and worrying about having missed some critical part of the computation in our own code. (Matrix algebra is just a lot of steps, and hard to get right when you're still learning to code.)

Despite this knowledge, let's get started by writing some simple computations in pure Python to work with our "matrices" stored in lists. Let's calculate the dot product of two vectors of equal length as a first exercise.

### Calculating Dot Products

The **dot product** of two vectors is the sum of the products of the corresponding elements in each vector. We can write it as follows:

$$ a \cdot b = \sum_{i=1}^N a_i \times b_i $$

In other words, a dot product of two vectors (they MUST be of equal length) is calculated as the sum of the products of values in corresponding positions within the vectors. We need to walk through each position within our vectors, multiplying the values in the same position, and then adding all these products together. If we try this in code, we might write the following:


```python
def dotProd(v1, v2): # Define our function and arguments
    if len(v1) is len(v2): # Test equality of vector length
        dp = 0               # Initialize Dot Product Value
        for i in range(len(v1)): # Loop over all elements
            dp += v1[i]*v2[i]      # Add elements of the sum
        return dp            # Return the dot product
    else: # If vetors are of unequal length, return error
        raise RuntimeError("Vectors must be of equal length")
        
dotProd([1,2,3], [7,10,1])
```






Let's check by hand: 

$$ 1*7 + 2*10 + 3*1 = 7 + 20 + 3 = 30 $$


### Matrix Multiplication

In order to get to the point where we can do some real heavy lifting with matrices (solve systems of equations, etc.), we need to multiply two matrices together. This is possible when the number of columns in the first matrix are equal to the number of rows in the second matrix. We call two matrices that have this property relative to one another **conforming** matrices. It is also important to note that if $ A\times B $ is conforming this does NOT necessarily mean that $B\times A$ is conforming! Order matters with matrices! If

- $A$ is an $m \times n$ matrix (has $m$ rows, $n$ columns)

- $B$ is an $n \times q$ matrix (has $n$ rows, $q$ columns)

then the matrices are conforming, and can be multiplied together. The resulting matrix, $C$ is an $m \times q$ matrix.

The math to calculate multiplication of two matrices is somewhat complex. Here is an example of how it works:

$$
A =
  \begin{bmatrix}
    1 & 2 \\
    3 & 4
  \end{bmatrix}, 
B =
  \begin{bmatrix}
    6 \\
    5
  \end{bmatrix}
$$

Matrix $A$ has 2 columns, and $B$ has 2 rows (conforming).

$$ 
AB = C  = \begin{bmatrix}
    1\cdot 6 + 2\cdot5 \\
    3\cdot 6 + 4\cdot5
  \end{bmatrix} = 
  \begin{bmatrix}
    16 \\
    38
  \end{bmatrix} \checkmark $$

The more general pattern for matrix multiplication is as follows:

$$
A =
  \begin{bmatrix}
    a_{1,1} & \cdots & a_{1,m}\\
    \vdots & \ddots & \vdots\\
    a_{n,1} & \cdots & a_{n,m}
  \end{bmatrix}, 
B =
    \begin{bmatrix}
    b_{1,1} & \cdots & b_{1,p}\\
    \vdots & \ddots & \vdots\\
    b_{m,1} & \cdots & b_{m,p}
  \end{bmatrix} 
$$

Matrix $A$ has $m$ columns, and $B$ has $m$ rows (conforming). C will have shape $n \times p$

$$ c_{ij} = \sum_{k=1}^m a_{ik} \times b_{kj} $$

We calculate all elements of $C$ in this manner. One last way to look at this is with the following visual guide:

![](https://github.com/dustywhite7/Econ8320/raw/master/SlidesCode/matMult.png)


Now that we have looked at this process in significant detail, let's write an algorithm to perform arbitrary matrix multiplication given two conforming matrices.


```python
def matMul(a, b): # Define function, take 2 matrices
    for i in range(len(a)): # Make sure a is matrix
        if len(a[i]) is not len(a[0]): # If not,
            raise RuntimeError( # Raise an error
            "Matrix A is not correctly specified")
    for i in range(len(b)): # Make sure b is a matrix
        if len(b[i]) is not len(b[0]): # If not,
            raise RuntimeError( # Raise an error
            "Matrix B is not correctly specified")
    matrix = [] # Initialize new empty matrix
    if len(a[0]) is len(b): # Test for conformability
        for i in range(len(a)): # Iterate over rows of a
            row = [] # Create row of new matrix
            for j in range(len(b[0])): # Iterate over columns
                row.append(dotProd(a[i], # Append elements of col
                  [b[n][j] for n in range(len(b))]))
                matrix.append(row) # Append rows to matrix
        return matrix # Return the newly calculated matrix
    else: # If matrices are nonconforming
        raise RuntimeError( #Raise an error
        "Matrices are nonconformable for multiplication")
        
A = [[1,2],[3,4]]
B = [[6],[5]]

matMul(A, B)
```






Since we did this problem by hand before writing our code, we know that we got the right answer. Yay! But, really, that was a lot of annoying code to write... It's great that Python is so flexible that we can quickly write functions to do calculations like matrix multiplication. Do we WANT to write out functions to do all of the mathematical processes we need for different kinds of analysis? Random number generators? Matrix inversion algorithms? Solving matrix equalities?

![w:500](https://steamuserimages-a.akamaihd.net/ugc/1002555926635405089/63B75F86672E6D0197144382C960EAF51DFF5E21/)


## Numeric Python (Numpy)

Instead of writing our own algorithms, sometimes (pretty much all the time if we are honest) we prefer libraries with pre-written (and far more efficient) algorithms to solve complex mathematical problems. The `numpy` library is that library in Python. Its full documentation is available here: [Numpy Reference Page](https://docs.scipy.org/doc/numpy/reference/index.html).

There are a few reasons that we would strongly prefer `numpy` to our own code:
1. Many eyes - there are many, many contributors to the `numpy` project, so that bugs are worked out much more quickly than would happen on our own code
2. Underlying code is C++/Fortran - it turns out that Python is actually a pretty slow programming language when all of your code is written in pure python. `numpy` gets around this problem by being a library that actually contains Python code to interact with algorithms written in much faster languages like C++ and Fortran. This means that we get REALLY fast code, but without the burden of needing to learn more difficult programming languages
3. Well-seasoned - `numpy` has been around a long time (since at least 2006, maybe 1995 depending on how you look at it). This means that it has had lots of time to build up capabilities and functionality. It does pretty much all the things! Next week we will finish covering `numpy` with `scipy`, and then they really DO do all of the things. (haha... do do... 💩... sorry...)


Now that we know it exists (and have hopefully motivated you by explaining its value), let's learn how to use `numpy`! So much time saving!

### `numpy` arrays

The building blocks of `numpy` are arrays. Arrays can essentially be treated as equivalent to mathematical matrices (and vectors), and are a special object type that takes data and stores it in formats that allow us to more easily apply mathematical functions to that data. The big advantage of arrays is that the entire array must be of a certain type. If entries in an array are non-numeric, then the whole array is treated as non-numeric (called `object` arrays). If we have some `int` and some `float` values, the array becomes `float`. This allows us to homogenize operations across arrays. 

Arrays can have any number of dimensions, from 1 to whatever violates your computer's memory constraints. In this course we will generally deal with 1- and 2-dimensional arrays. Arrays work differently than lists of lists because they require that our data be **rectangular**. In other words, if we have 3 columns in one row, we must also have 3 columns in the other rows. Before we get too far into the nitty gritty, let's take a look at how we *create* arrays. We will focus on creating arrays in two ways:
1. Creating arrays by coercing lists and tuples to the array type
2. Creating arrays using `numpy` commands

#### Array Creation via List Coercion


```python
import numpy as np # import library as np object

myList = [1, 2, 3, 4]
myArray = np.array(myList)
myArray
```






Cool! We created a list, and transformed it into a 1-dimensional array. How do I know that it is a 1-dimensional array? We can use the `.shape` attribute to check for ourselves:


```python
myArray.shape
```






This `shape` attribute will help us to ensure that we understand the structure of any arrays we are working with. The number of elements in the `shape` tuple tells us the dimensionality of our array, and the value in each position tells us the size of each dimension. In this case, we see that we have a 1-dimensional array, with 4 values.

In sum, we can use the `np.array` function to generate an array from any arbitrary list (or tuple) of numbers.

#### Array Creation Using Commands

Sometimes we don't have data to put into our array quite yet, but we want to get it built out so that we can algorithmically update the array as data flows in. There are many commands that we can use to create arrays, depending on the kind of array that we need to build:


```python
np.array([1,2,3,4]) # Specify each element
```







```python
np.zeros((3,3)) # Generate 3 x 3 array of zeros
```







```python
np.eye(3) # Generate 3 x 3 identity matrix
```






The `array`, `zeros`, and `eye` functions are all ways to create arrays in `numpy`. The `np.eye` function, in particular, allows us to quickly create matrices that are essential in matrix algebra, since the identity matrix is the matrix version of the number 1, and is used to manipulate equations as we look to solve them in various contexts.

Many other functions exist to generate arrays that we won't cover, and there are a few more that we will cover later as we learn about other `numpy` functionality.


### Manipulation of Arrays

Once we create them, there are lots of things that we might want to do with our arrays, but some of the most basic are just transformations and manipulations of the arrays.

First, we sometimes want to reshape our data. This may be because we store data in one shape or structure, but need to perform calculations using the data in a different structure. If we store image data for 28x28 pixel images in a spreadsheet, for example, we would have one row per image, and each row would have 784 columns. In order to render one row as an image, we could then transform a row back into a 28x28 obejct using the `.reshape` method. Let's take a look: 


```python
myArray = np.array([1,2,3,4]) # Specify each element
np.shape(myArray)
```






Again, we will start with our 1-D array, and in the cell below, we will make it a 2-D array, or a matrix:


```python
myArray = np.array([[1,2,3,4]])
np.shape(myArray)
```






Now we see that the array is 2-D (this happened because we coerced a list embedded in a list into an array). We can reshape the array to make a square matrix using the following code:


```python
myArray.reshape((2,2)) # transform to square matrix
```






If we want to make it a matrix in one column rather than in one row, we can reshape accoringly:


```python
myArray.reshape((4,1)) # transform to column vector
```






We can also transform a matrix by **transposing** the matrix. This means that we make each row into a column, and each column into a row (preserving order). In other words, we flip the matrix across the main diagonal (positions (1,1), (2,2), etc.). The transpose of an array is always stored in the attribute `.T`:


```python
myArray = np.array([[1,2,3,4]])
myArray.T # transposes the array if 2-D
```






### Math Operations on Matrices/Arrays

Now that we can create and shape matrices, it's time to start doing math with them. I assume that you are familiar with the mathematical operations that we will discuss, and will instead focus on describing the notation used to perform the operations.

We can add a scalar value to an array:


```python
myArray = np.array([1,2,3,4])
newArray = np.array(myArray) + 1
newArray
```






Add (or subtract) arrays:


```python
myArray - newArray # must have same shape
```






And, critically, perform matrix multiplication:


```python
myArray.T.dot(myArray) # to get 4 x 4 product
```






We can also use the `@` operator to conduct matrix multiplication. It's much easier to read as math, but does the exact same thing:


```python
myArray.T @ myArray # '@' only works in python >=3.5
```






#### An Exercise Multiplying Matrices

To get more familiar with how to use `numpy` to create useful functionality, let's write a function that accepts four arguments ($a$, $b$, $c$, and $x$), and calculates the output ($y$) of the following functional form:

$$ y = a + b\cdot x +c\cdot x^2 $$

Remember that we can solve systems of equations by converting the equations into matrices, and then use matrix multiplication to solve the entire system of equations in one operation. This might seem silly in a simple example, but this powerful ability to solve systems of equations with matrix algebra is the core of regression analysis and machine learning algorithms.


```python
def squareFunc(a=1, b=1, c=1, x=1):
    coef = np.array([a, b, c])
    xs = np.array([1, x, x**2])
    return coef @ xs # we can do the same math with coef.dot(xs)

squareFunc(a=10, b=3, c=4, x=2)
```






On top of making our math into a single operation, vectorized math using `numpy` is FAR more efficient computationally than loops and standard Python code. This doesn't matter for our current use case, but is very important when writing large scale code. In the end, our goal is to be able to code efficiently even where the data that we use is very large, so we want to focus on solutions that will scale with our data.

Now that we have the ability to manipulate matrices, we have the first building blocks for constructing statistical models. We need a little bit extra help to make it convenient and fast to do all of the calculations, so we will spend the rest of this notebook looking at statistical functionality across `numpy` and `scipy`.

## Stats in `numpy` and `scipy`

Because `numpy` and `scipy` are adaptations of code that existed before Python, our statistical functionality is spread across the two libraries. Some of the stats that we need will come from `numpy`, while other elements will come from `scipy`. For the most part, random sampling happens through `numpy`, and calculating distributional propoerties will happen through `scipy`. Let's start generating random numbers!

### Random Numbers in `numpy`

In case you need some justification for why random numbers are so useful, we generate random numbers for all sorts of tasks. We use random numbers to generate simulations. If we didn't, each simulation would be identical to the others. We use random numbers when we conduct bootstrapping procedures, so that we can sample randomly from available observations in order to generate a more complete understanding of the data and likelihood that what we have seen is what we expected to see. `numpy` has the functionality to allow us to generate many different and useful types of random numbers, and to do so quickly and easily.

The code to generate random numbers is really simple, and also doubles as a great way to create arrays!


```python
import numpy as np
np.random.rand() # Generates a single value
```







```python
np.random.rand(3) # Array of 3 random values
```







```python
np.random.rand(5,5) # Create a 5 x 5 matrix of random numbers
```






This function draws from the uniform distribution, and can be utilized as the basis for ANY other random process. We won't have to do this very often, but if we start with a random number on the unit interval $[0, 1)$, we can generate any other distribution of random numbers. This is easily done in `numpy` via **Inverse Transform Sampling**. Let's use the uniform distribution to generate numbers from the *Exponential Distribution* with $\lambda = 1$.

First, we should look up the CDF of the Exponential Distribution, solve for $x$, and use it to generate values.

$$F = 1-e^{-\lambda x}=y $$
$$ x = - ln(1-y)$$

Inverse transform sampling is simply the process of using random uniform draws on the unit interval as sampled $y$ values (because the CDF of a distribution is always between 0 and 1). Once we have the CDF value, we can use that to work our way backward to the $x$ value from a given distribution that sits at that position on the CDF. We just need to write a function that draws a random sample of $y$ values, and then passes them through the equation we just solved for $x$.


```python
def expD(x): # Define my function
    if isinstance(x, float) | isinstance(x, int): # Test if argument is list or not
        return -1*np.log(1-x) # Return single value
    else: # If list
        return [-1*np.log(1-y) for y in x] # Return values

expD(np.random.rand(10))
```






And now we have 10 random values drawn from the exponential distribution! Like with our hand-made matrix operations, we really don't need to do this, though! Instead, we can simply use the built-in random number generators within `numpy`. Some common distributions to draw from:
- `np.random.rand` - Random uniform draws on the unit interval
- `np.random.randint` - Random draws among integers
- `np.random.beta` - Random draws from the beta distribution
- `np.random.normal` - Random draws from the normal distribution
- `np.random.poisson` - Random draws from the Poisson distribution

There are a ton more, and you can see them all [here](https://numpy.org/doc/stable/reference/random/legacy.html).

### Random Numbers and Pandas!

It turns out that `pandas` uses these random sampling capabilities behind the scenes. We see it in action when we use the `.sample(n)` method to sample from a `DataFrame`.


```python
sampled_data = full_data_name.sample(10000, replace=False) # Don't run, we don't have any data loaded. :)
```

### Distributional Calculations

While it is great to be able to *sample* from statistical distributions, it is also helpful to be able to calculate various statistics when we know that a particular distribution is generating our data. `scipy` includes [functions for calculating properties from most distributions](https://docs.scipy.org/doc/scipy/reference/stats.html):

Example: [Normal Distribution](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.norm.html#scipy.stats.norm)

Example: [Student's t Distribution](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.t.html#scipy.stats.t)

We can use this functionality when we build out statistical tests on regression analysis. These distributions include the ability to make calculations using the PDF, CDF, survival function, and many more parameters that are of interest in different contexts. Let's check it out with the normal distribution:


```python
from scipy.stats import norm

norm.sf(1.96)
```






So we can see that, for a standard normal distribution, the position `x=1.96` (which is also 1.96 standard deviations away from the mean) is associated with a probability of ~2.5% that a new draw would be higher than this point. That's why z-statistics of 1.96 or above are considered statistically significant at the 5% level for a two-tailed test (2.5% * 2 tails = 5%). 

We can calculate many other properties of the normal distribution. What is the likelihood that a draw from the random normal distribution would fall between 0 and 1? Let's find out!


```python
norm.cdf(1) - norm.cdf(0)
```






So 34% of draws would be expected to fall in that interval! If we use our `numpy` sampling tools, we can verify:


```python
draws = np.random.normal(size=100)
len([i for i in draws if (i<=1) & (i>=0)])
```






Crazy! My draw got exactly 34/100 observations between 0 and 1. If we keep sampling, we will see other values as the sample changes, but it will generally be pretty close to our estimate!

Let's put all these skills to work and build some statistical tools. It's time to make a regression algorithm!

## Solve it:

This week we learned about numeric libraries in Python, specifically NumPy and SciPy. For the assignment this week, I would like you to code a class called "RegressionModel", that will calculate all the values typically presented in the primary regression table by statistical software. You can see an example in the image below:

![](https://blog.minitab.com/hubfs/Imported_Blog_Media/regr_p_values.gif)

Your job is to create the following functionality within your class object:

- your class should take arguments for `x`, `y`, `create_intercept`, and `regression_type`
    - x and y should be data frames
    - create_intercept should be a binary variable (True or False)
    - regression_type should be a string, containing either `"ols"` or `"logit"` (we won't work with the logistic part this week... that is for next week)
- attributes `x` and `y` that store the exogenous and endogenous variables used in your regression
- a method (call it `add_intercept`) that adds a column of ones to the data frame `x` if create_intercept has a value of `True`. This can also be completed without a method if you so choose. Name the column `intercept`.
- a method (call it `ols_regression`) that estimates the results of ordinary least squares regression using your x and y data frames.
    - the results should be stored in a dictionary named `results`, where each variable name (including the intercept if `create_intercept` is True) is the key, and the value is another dictionary, with keys for `coefficient`, `standard_error`, `t_stat`, and `p_value`.
- a method (call it `summary`) that presents your regression results in a table, similar to the first 5 columns of the table above
    - Columns should be: `"Variable name"`, `"coefficient value"`, `"standard error"`, `"t-statistic"`, and `"p-value"`, in that order.

**You only need to define the class**. My code will create an instance of your class (be sure all the names match these instructions!), and provide data to run a regression. I will provide the same data to you, so that you can experiment and make sure that your code is functioning properly.

Put code that you want graded here $\downarrow\downarrow\downarrow$

