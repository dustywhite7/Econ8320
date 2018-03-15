<!--
$theme: gaia
template: invert
-->

# Programming Practice - Factoring & Debugging

---

### What is programming?

---

### What is programming?

- Problem solving
	- Using a specific toolkit (computer code)
	- Using logic

<br>

We write a series of logical steps that can be taken, given assumed inputs, in order to realize a proposed outcome

---

### How do we solve a problem?

---

### How do we solve a problem?

- In programming, we focus on a method called **Functional Decomposition**
	- Also called **Factoring**
	- Break a problem down (decompose it) into its smallest functional elements
	- Construct those elements
	- Combine elements to achieve the end goal

---

### Factoring Recent Assignments

1) Homework 4 - Least Squares Regression Problem
<br>

2) Lab 6 - Multiprocessing on a Random Draw
<br>

3) Homework 6 - Multiprocessing with Summary Statistics

<br>

Let's walk through factoring these problems


---

### Advantages of Factoring

<br>

- Your code will be easier to read
- You will know what you need to do
- It is clear what the next step is
- Your code will be reusable to a greater extent
	- Other programmers will have an easier time following your code
- It will be easier to **debug** and run **unit tests**

---

### What is Debugging?

---

### What is Debugging?

**Debugging** is, like the name suggests, the process of removing bugs from a program or script.

- Why do we get the error that we get?
- How is data moving through our code?
- What needs to be fixed?


---

### What is Unit Testing?

**Unit Testing** is the process of feeding as many different (and possibly wrong) types of information to our code in order to determine how the code will work under less than ideal circumstances.

- What happens if our input is incorrectly formatted?
- What if the data is the wrong **type**?
- What if ...

---

### Why Should I Debug and Unit Test?

<br>

- **Debugging** is critical, since our code will not work if it contains bugs. At the very least, it will not work as we expect it to
- **Unit Testing** is how we understand where our code fails to prepare for any possible case that could occur
	- We need this if we want to prevent "Garbage In, Garbage Out" problems in the future


---

### Moving from Jupyter to Spyder

<br>

In order to be better able to use these functions, we need to leave Jupyter behind.

Let's work through some code, in order to learn how to debug it.

Here is the [file]()