###### This lesson is based on notes from [sebastianraschka.com](http://sebastianraschka.com/Articles/2014_multiprocessing.html)

What actually happens when you run code, or execute a program on a computer? If we focus on Python, what happens when we run Python code? Does our computer "speak Python", understand what we type, and do what we ask?

It turns out that no, our computer does NOT speak Python. When we execute Python code, our code is passed to an **interpreter**. This interpreter is what reads our code and translates what we have written into what is called **machine code**. Machine code is typically not human-readable. That's the reason we have languages like Python, R, C++, Java, etc. We need a way to express logic clearly and explicitly, so that it can be translated into the kind of code that our computer DOES understand. 

So far, human speech (or written human language) does not translate directly to machine code.

But what actually happens once we write our code, and the computer starts to run that code? We can understand the basics of this process through the following six (simplified!) steps:

1) The computer allocates memory to the program
2) The program issues a series of instructions to the processor (the thinking part of the computer)
3) Upon completion of one instruction by the processor, the next is started
4) Information is returned from the processor to the program as needed
5) New instructions are sent to the processor based on information received from the processor
6) Return to step 2, repeat until program is finished


When a program is running, it typically has a single space in memory in which it stores all information relevant to its task. This memory space allows the information to be used by whichever part of the program requires that information to use it. Basically, think of all of the things in memory as shared assets, and different parts of the program want to be able to access them at the same time. Kind of like if you share a storage space with a friend or family member. Sometimes you'll be pulling out the camping gear, and sometimes they will be instead.

Information that is accessible across the entire program are called **globally defined values**. But not all variables are global. Some variables with reduced **scope** are not available to all segments of a program. You might have valuables that you don't share with the other people using your storage space. It's kind of like that. Variables with reduced scope are only available to parts of the program that share that scope.

While for people, we restrict access primarily based on keeping valuables safe, programs tend to do it in order to ensure that information is not lost or modified while it is needed by a part of the program. You wouldn't want to have someone change your budgeting spreadsheet in the middle of the month, would you?

Again, **scope** is a term used to define the areas in which a given value in memory is accessible. Variables that are **Global** in scope can typically be accessed by any function or command running as part of the program. Variables that are **Local** can only be accessed within the scope in which they are defined. A variable created inside a function is said to be **local** to that function, and only available until the function is concluded. Then it is either returned to the global space, or forgotten.



![](https://github.com/dustywhite7/Econ8320/blob/master/SlidesCode/serialParallel.png?raw=true)

One of the single biggest changes in computational technology in the recent past was the advent and spread of parallel computation. This concept is the crux of this lesson, but needs a lot of explaining, because it isn't something that we as computer USERS have to deal with. It happens behind the scenes, despite its tremendous importance.

### Sequential programs

When we perform tasks, some steps must be performed sequentially. This happens because one task depends on the results of the other task. For example, an American football team will only make a play on fourth down if they fail to score or convert on third down. We can't fully implement our plan for fourth down until we have seen whether or not fourth down will occur. 

We need to aim our penalty shot in FIFA before taking the kick. We even need to wait to complete the details for the elimination rounds of the tournament until group play has ended. Until then, we don't know enough about which teams will advance to complete the bracket.

In programming speak, sequential programs are sequential because it is critical that the results of one calculation be within the **scope** of the other calculations. If one sequential calculation cannot view the results of the prior calculation, then the second function cannot be completed.

### Parallel Programs

On the other hand, some calculations can be performed independent of the results of other steps. These tend to be calculations that can essentially be considered separate tasks, but part of a larger overall task. Some examples include

- Batch processing of files
- Non-sequential simulations
- Serving recommended products to many users
- Repeated random draws
- Rendering polygons

The key difference between serial and parallel programs is the dependency (or lack of dependency) of calculations on the results of previous calculations.

- Serial programs rely on previous results
- Parallel programs do not depend on the results of other calculations

Parallel programs can occur simultaneously, allowing us to accelerate execution. If we can run four calculations simultaneously, then in theory we might be able to run 100 computations in the time that a serial program might run 25 similar computations.

Parallel computations have enabled advances like improved graphics in video games, and have made possible the revolution in machine learning. Let's learn how to make parallel code work for our projects, as well!

One place where parallel processing really shines is in estimating complex mathematical calculations. While some math can be solved algebraically, other math problems can only be solved computationally. The more computations we can perform in a given amount of time, the sooner we can find the solution to those problems. We can buy faster computers to speed up calculations, but we can also parallelize many calculations, giving us benefits without having to upgrade our computer!

Some examples in which we will typically solve math problems with computation:
- Estimating Producer/Consumer Surplus
- Calculating probabilities from frequency tables
- Integrating on complicated functional forms

### Numeric Integration

Often, when integrating complicated functions, there is no **algebraic** solution to the integral. This means that we need to estimate the value of the integral **numerically**. The process that we follow to estimate an integral numerically follows:

1) Choose points at which to estimate the value of the function
2) Choose bandwidth
3) Multiply function values by bandwidth
4) Add all estimates to calculate approximate integral

![](https://github.com/dustywhite7/Econ8320/blob/master/SlidesCode/integralProcess.png?raw=true)

Let's start by just defining a function to integrate. We can use 

$$ f(x) = \frac{1}{1+x^2} $$

as our example function. First, we need to write this function as a Python function:

```python
# define any function here!
def f(x):
    # return the value of the function given x
    return 1/(1 + x**2)
```


Now, we need to write a function that can sample from our function, and calculate the area of the sampled rectangles, and then return an approximate area.


```python
import random

def serial_integral(nSample, f, xmin, xmax):
  # determine points of estimation
  sample = sorted([random.uniform(xmin, xmax) for i in range(nSample)])
  # Calculate height at each point
  value = [f(i) for i in sample]
  # Calculate areas of rectangles
  # We have to specially calculate the first rectangle,
  #   because xmin is not part of our list of samples
  area = [(sample[0]-xmin)*value[0]] + 
    [(sample[i]-sample[i-1])*value[i] for i in range(1, len(sample))]
  # Return sum as an approximate integral
  return sum(area)
```

This is our function for actually integrating a function `f` from `xmin` to `xmax` across `nSample` random intervals. Below is a picture of how this function gets (approximately) closer to estimating the true integral value as we increase the number of points at which we sample the function. Because integration is based on randomly drawn intervals, the convergence is not smooth. If we took many integrals at each bin number, however, we would expect this plot to become smooth.

![](https://github.com/dustywhite7/Econ8320/blob/master/SlidesCode/integral.png?raw=true)

### Parallel calculations

The ``multiprocessing`` library is designed to create multiple sub-instances of the python interpreter called processes, with each process returning values that are independent of the other processes. In order to coordinate this effort, some computational power must be assigned to send off processes and to retrieve their results upon completion. 

This "overhead" means that parallel processing is not usually justified for very simple problems, and is reserved for computationally intensive problems, or where there are very many processes to be completed in one batch.

Given the overhead of parallelization, it is not worthwhile to make a parallel version of our single integral function above. Instead, it IS worthwhile to create a function that can calculate the integral many times in parallel. Like we said above, convergence is noisy, but an average value for each given number of bins should be more stable.

Let's see how much time we can save by making a function that will calculate an average value in parallel when compared to a serialized alternative.

```python
import multiprocessing as mp # This module is part of the
			     # python standard library

def serial_average(n_bins, n_reps, f, xmin, xmax):
  attempts = [serial_integral(n_bins, f, xmin, xmax) for i in range(n_reps)]
  return sum(attempts)/n_reps

def parallel_average(processes, n_bins, n_reps, f, xmin, xmax):
  pool = mp.Pool(processes=processes)
  results = [pool.apply_async(serial_integral, (n_bins, f, xmin, xmax)) for i in range(n_reps)]
  results = [p.get() for p in results]
  return sum(results)/n_reps
```

Now let's explore what that function does.


```python
def parallel_average(processes, n_bins, n_reps, f, xmin, xmax):
  pool = mp.Pool(processes=processes)
  ...
  return ...
```

The `mp.Pool` class provides the functionality to organize our processes, and to define the degree to which we want to spread our work across various **processes**. We can specify how many active processes there should be at any time with the number of processes.

We need to take care to choose the right number of processes for our machine! In general, my experience has been that performance is best when you keep the number of processes at or below the number of cores available in your computer's processor.


```python
def parallel_average(processes, n_bins, n_reps, f, xmin, xmax):
  ...
  results = [pool.apply_async(serial_integral, (n_bins, f, xmin, xmax)) for i in range(n_reps)]
  ...
  return ...
```

We next use the `apply_async` method to pass the values that we want our pooled instances to calculate. We need to provide the function to be executed, as well as the arguments for the function in each iteration with each each of the arguments an element in a tuple. In our case, we are not varying the arguments, so we provide a single tuple that never changes, but we could vary those arguments whenever necessary or desirable.

```python
def parallel_average(processes, n_bins, n_reps, f, xmin, xmax):
  ...
  results = [p.get() for p in results]
  ...
  return ...
```
The next step is to use the `get()` method on each element of our returned processes. This will fetch the return statement values from each of the processes that we executed in the last line.

At this point the parallel computation is complete. The remainder of the function will look and work just like the results from our `serial_average` method.


### Timing it

Next, it is time to write code that will allow us to test our parallel and serial performance.

```python
import timeit # library for timing execution of code

benchmarks = [] # list to store our execution times

benchmarks.append(timeit.Timer('serial_average(10000, 100, f, 0, 1)',
  'from __main__ import serial_average, serial_integral, f').timeit(number=1))
    # Note that we need to include a second line
    # that imports our functions from __main__.
    # This tells the timer what needs to be IN SCOPE

benchmarks.append(timeit.Timer(
  'parallel_average(2, 10000, 100, f, 0, 1)',
  'from __main__ import parallel_average, serial_integral, f').timeit(
    number=1))
    # Need to include number of processes
    # when timing the parallel implementation
```

Amazing! When timing the output on my virtual machine (not at all a powerful computer), the parallel version runs nearly twice as fast (0.36 seconds vs 0.69 seconds). Even in a fairly trivial example, we see significant performance gains.

When I ran a similar trial on my computer with 16 cores, I saw the following performance pattern:

![w:750](https://github.com/dustywhite7/Econ8320/blob/master/SlidesCode/performance.png?raw=true)

On 16 cores, the parallel version of this problem executes over 5x faster than the serial version! Some observations:

- This was done on a 16-core processor, which is an expensive way to get a performance gain
- Creating too many processes (going past 16 to 32) actually started to slow the computations down
- We need to be aware of the hardware that we are utilizing when designing parallel code

If you are unsure of how many processes you should run on your machine, the following command will show you how many CPU cores are available to Python:

```python 
mp.cpu_count() # Tells us the number of available CPUs
```

Now it's your turn to give it a go!

Simulate 1,000 draws from a multivariate normal distribution and calculate the average value of the dependent variable, but do it 100 times! This is called "bootstrapping" and is a critical process in many statistical models and simulations. Draw from the following equation:

$$ y = \alpha + x_{1} + 2\cdot x_{2} + \frac{1}{2}x_{3} + \epsilon $$

where

$\alpha \sim \mathcal{N}(15,2)$, $x_1 \sim \mathcal{N}(3,5)$,

$x_2 \sim \mathcal{N}(10,1)$, $x_3 \sim \mathcal{N}(8,8)$, and

$\epsilon \sim \mathcal{N}(0,1)$

$\mathcal{N}(\mu, \sigma)$ represents the Normal distribution with mean $\mu$ and standard deviation $\sigma$

Write functions to generate all values and calculate . Test and time these draws using serial and parallel programming (2 cores), and report the difference in performance between the two versions.


Call your serial function `sCalc`, and your parallel function `pCalc`, store your results from each function as a list, with the lists named `sResults` and `pResults`, respectively.

Finally, store the timed values for each run as `sTime` and `pTime`, respectively. All code for this exercise should go in the `bootstrap.py` file found in the file tree.

**NOTE: Because we are running code on a virtual machine, and because the problem is not very computationally intensive, we should not be surprised if the serial version of our code outperforms the parallel version for this assignment.**

**OTHER NOTE: Because we need this to run in a reasonable amount of time, we are only running 100 rounds of samples. Typical bootstrapping procedures default to 10,000 rounds as good practice.**
