
for i in range(5):
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


    