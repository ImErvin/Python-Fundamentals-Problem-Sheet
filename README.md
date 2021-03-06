## Python Fundamentals Problem Sheet 

This is a simple python fundamentals problem sheet. The aim of this problem sheet is to catch up oh some python syntax and solve some coding problems using python. This problem sheet was created by [Ian Mcloughlin](https://github.com/ianmcloughlin) as part of our emerging technologies module in college.

You can find my solutions to each of these problems in this repository.

### How to use this repository

1. Ensure you have Python 3.x and Git installed locally.
2. Enter the following commands into your command line.
```bash
# Change directory to anywhere you desire
cd anywhere..

# Clone this repository using git
git clone https://github.com/ImErvin/Python-Problem-Sheet.git
cd Python-Problem-Sheet

# Run any of the solutions
py hello-world.py
py current-time.py
# and so on..

```

### What is Python?
Python is a programming language that was created by Guido van Rossum and released in 1991. Different to the other common high-level programming languages, Python uses whitespace indentation to delmit blocks (off-side rule).

### Why Python?
Python is massively trending at the moment and the objective of our "emerging technologies" module is to study the trending technologies.

Not only that, but popular neural network training libraries such as TensorFlow use python to express and control training models.

### Problem Sheet Questions

**1. Hello, World!**

	Write a program that prints "Hello, World!" to the screen.
**2. Current Time**
	
	Write a program that prints the current time and date to the console.
**3. FizzBuzz**
	
	Source: http://wiki.c2.com/?FizzBuzzTest
	
	Write a program that prints the numbers from 1 to 100, except for the following conditions.
	For multiples of three print "Fizz" instead of the number, and for multiples of give print "Buzz".
	For numbers which are multiples of both, print "FizzBuzz".
**4. Factorial digit sum**
	
	Write a function that calculates the sum of the digits of the factorial of a number. n! means n x(n -1)...x 3 x 2 x 1. 
	For example, 10! = 10 x 9 x 8 ... x 3 x 2 x 1 = 3628800, and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27. 
	Find the sum of the digits in the number 100!
**5. Guessing Game**
	
	Source: https://adriann.github.io/programming_problems.html
	
	Write a guessing game where the user must guess a secret number. 
	After every guess the program tells the user whether their number was too large or too small. 
	At the end the number of tries needed should be printed. 
	It counts only as one try if they input the same number multiple times consecutively.
**6. Largest and smallest in list**
	
	Source: https://adriann.github.io/programming_problems.html
	
	Write a function that returns the largest and smallest elements in a list. 
**7. Palindrome test**
	
	Source: https://adriann.github.io/programming_problems.html  
	
	Write a function that tests whether a string is a palindrome.
**8. Merge list and sort**
	
	Source: https://adriann.github.io/programming_problems.html 
	
	Write a function that merges two sorted lists into a new sorted list. [1,4,6] , [2,3,5] -> [1,2,3,4,5,6].
**9. Newton's method for square roots**
	
	Source: https://tour.golang.org/flowcontrol/8 
	
	Implement the square root function using Newton's method. 
	In this case, Newton's method is to approximate sqrt(x) by picking a starting point z and then repeating:
	
	z_next = z - ((z*z - x) / (2 * z))

	To begin with, just repeat that calculation 10 times and see how close you get to the answer for various values(1, 2, 3, ...). Next,  
	change the loop condition to stop once the value has stopped changing (or only changes to be very small delta). 
	How close are you to the math.sqrt value?
**10. Reverse String**
	
	Write a function to reverse a string.
