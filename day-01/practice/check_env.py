# Get the Environment from User and print it

env = input("Enter the Environment") # taking input from the user (Keyboard) in env variable

print("The User input Env is: ",env)

# conditional statement simple if else

# == != > < >= <=

if env == "prd": # True or False
    print("Don't Deploy on Friday")
elif env == "stg": # True or False
    print("Take backup & Test well")
elif env == "test":
    print("Test it well")
else: # False
    print("Safe to deploy any day")


# Type Casting - conversion of 1 data type to another
a = int(input("Enter the num 1"))
b = int(input("Enter the num 2"))
print(type(a))
print("Multiplication is: ",a*b)
print("Addition is: ",a+b)
print("Subtraction is: ",a-b)
print("Division is: ",a/b)


