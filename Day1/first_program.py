# Learning about variables, data types, and basic input/output in Python

a = 10
b = 20.01
c = "Hello, World!"
d = True

print(a)  # Python only has the print() function for console output, which automatically adds a newline at the end by default. There's no separate println function like in some other languages.
print(b)
print(c)
print(d)

e = 10
f = 20

print(type(e))
print(type(b))

g = e + f  # OPERATOR, OPERAND, OPERATION
#   Addition operation
#   + is the operator
#   e and f are operands
#   e + f is the operation
#   The result of the operation is stored in variable g

print(g)



# Taking user input, Learn about input() function

num1 = input("Enter first number: ")
num2 = input("Enter second number: ")

print(type(num1))
print(type(num2))

num3 = num1 + num2  # This will concatenate the two inputs as strings
print("The concatenated result is:", num3)

# When you use input() to get user input, Python always returns a string, regardless of what the user types:

num1 = int(input("Enter first number: "))  # Convert input to integer
num2 = int(input("Enter second number: "))  # Convert input to integer      


print(type(num1))
print(type(num2))

num3 = num1 + num2  # This will now add the two numbers mathematically
print("The sum is:", num3)

# Functions learned so far: print(), type(), input(), int()
# Functions learned so far: print(), type(), input(), int()
# Functions learned so far: print(), type(), input(), int()
# Functions learned so far: print(), type(), input(), int()
# Functions learned so far: print(), type(), input(), int()
# Functions learned so far: print(), type(), input(), int()
# Functions learned so far: print(), type(), input(), int()
# Functions learned so far: print(), type(), input(), int()
# Functions learned so far: print(), type(), input(), int()
# Functions learned so far: print(), type(), input(), int()
# Functions learned so far: print(), type(), input(), int()



# Learning about loops and if, elif, else statements in Python

for i in range(5): # from 0 to 4
    if i % 2 == 0:
        print(f"{i} is even")
    else:
        print(str(i) + " is odd")  # or print(i, "is odd")



# f is not a function. It's a prefix that tells Python to treat the string as an f-string (formatted string literal).

name = "Prabhjot"
age = 25

# f-string (modern way)
print(f"My name is {name} and I'm {age} years old")
# Output: My name is Prabhjot and I'm 25 years old



for i in range(1,3): # from 1 to 2
    print("Enter a number:")
    input01 = int(input())
    if input01 == 1:
        print("i is one")
    elif input01 == 2:
        print("i is two")
    elif input01 == 3:
        print("i is three") 
    else:
        print("i is something else")

for i in range(3): # from 0 to 2
    print("Enter a number:")
    input01 = int(input())
    if input01 == 1:
        print("i is one")
    elif input01 == 2:
        print("i is two")
    elif input01 == 3: 
        print("i is three") 
    else:
        print("i is something else")




# Things learned so far: print(), type(), input(), int(), range(), f strings, for loops, if, elif, else statements
# Things learned so far: print(), type(), input(), int(), range(), f strings, for loops, if, elif, else statements
# Things learned so far: print(), type(), input(), int(), range(), f strings, for loops, if, elif, else statements
# Things learned so far: print(), type(), input(), int(), range(), f strings, for loops, if, elif, else statements  
# Things learned so far: print(), type(), input(), int(), range(), f strings, for loops, if, elif, else statements
# Things learned so far: print(), type(), input(), int(), range(), f strings, for loops, if, elif, else statements
# Things learned so far: print(), type(), input(), int(), range(), f strings, for loops, if, elif, else statements
# Things learned so far: print(), type(), input(), int(), range(), f strings, for loops, if, elif, else statements
# Things learned so far: print(), type(), input(), int(), range(), f strings, for loops, if, elif, else statements
# Things learned so far: print(), type(), input(), int(), range(), f strings, for loops, if, elif, else statements   


q = ""
while q != "q":
    print ("Enter number for table:")
    input01 = int(input())
    for i in range(1,11):
        print(f"{input01} x {i} = {input01 * i}")
    print("Press q to quit")
    q = input()

# Things learned so far: print(), type(), input(), int(), range(), f strings, for loops, if, elif, else statements,while loops
# Things learned so far: print(), type(), input(), int(), range(), f strings, for loops, if, elif, else statements,while loops
# Things learned so far: print(), type(), input(), int(), range(), f strings, for loops, if, elif, else statements,while loops
# Things learned so far: print(), type(), input(), int(), range(), f strings, for loops, if, elif, else statements,while loops
# Things learned so far: print(), type(), input(), int(), range(), f strings, for loops, if, elif, else statements,while loops
# Things learned so far: print(), type(), input(), int(), range(), f strings, for loops, if, elif, else statements,while loops
# Things learned so far: print(), type(), input(), int(), range(), f strings, for loops, if, elif, else statements,while loops
# Things learned so far: print(), type(), input(), int(), range(), f strings, for loops, if, elif, else


# Key points:

# Any Python file you run while the environment is activated will use myenv

# This works regardless of which folder the .py file is in

# You can run files from Day2, Day3, etc. - as long as myenv is activated

# If you don't activate, it uses system Python (no psutil)

# Check if environment is active:

# Look for (myenv) at the start of your terminal prompt

# Run which python - should show path to myenv, not system python

# The environment follows your terminal session, not your file location.