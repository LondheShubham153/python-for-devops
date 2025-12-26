# SCRIPTING = set of instructions
# Function = Kaam 

# ek kaam karo, 2 number input lo aur
# sum print kara do
# indented block / indentation

def sum_of_num(): # function definition (KAAM)
    num1 = int(input("Enter num 1: ")) # steps
    num2 = int(input("Enter num 2: ")) # steps

    sum = num1 + num2 # step 
    print(sum) #step

env = input("Enter the Environment") # taking input from the user (Keyboard) in env variable

print("The User input Env is: ",env)

if env == "prd":
    sum_of_num() # function calling



def take_backup():
    print("Backup script started ...")


if day == "Monday":
    take_backup()