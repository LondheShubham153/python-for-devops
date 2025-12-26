num = int(input("Enter the number you want the table for"))

# string Formatting "f"
name = input("Enter dost ka name")
print(f"Hello Dosto,{name} ")
# two ones are 2
# two tows are 4

# to toza 4
# to forza

for i in range(1,11):
    print(f" {num} x {i} = {num*i}")



# suraj = "chand"

# while suraj == "chand":
#     print("TWS name") # infinte loop
#     break


# real world

choice = input("Enter the choice (press q to quit):")

while choice != "q":
    num = int(input("Enter the number you want the table for"))

    for i in range(1,11):
        print(f" {num} x {i} = {num*i}")
    choice = input("Enter the choice (press q to quit):")