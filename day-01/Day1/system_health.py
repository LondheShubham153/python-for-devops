import psutil

RED = '\033[91m'
GREEN = '\033[92m'
RESET = '\033[0m'

user_input_cpu = float(input("Enter CPU usage percentage: "))
user_input_disk = float(input("Enter Disk usage percentage: "))
user_input_memory = float(input("Enter Memory usage percentage: "))

print(f"CPU usage {psutil.cpu_percent(interval=1)}%")
print(f"Memory usage {psutil.virtual_memory().percent}%")
print(f"Disk usage {psutil.disk_usage('/').percent}%")

if psutil.cpu_percent(interval=1) < user_input_cpu:
    print(f"{GREEN}CPU usage is under the threshold.{RESET}")
else:
    print(f"{RED}CPU usage is over the threshold.{RESET}")

if psutil.virtual_memory().percent < user_input_memory:
    print(f"{GREEN}Memory usage is under the threshold.{RESET}")
else:
    print(f"{RED}Memory usage is over the threshold.{RESET}")

if psutil.disk_usage('/').percent < user_input_disk:
    print(f"{GREEN}Disk usage is under the threshold.{RESET}")
else:
    print(f"{RED}Disk usage is over the threshold.{RESET}")