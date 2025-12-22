import psutil
cpu_threshold = int(input("Enter CPU threshold: "))
mem_threshold = int(input("Enter memory threshold: "))
disk_threshold =int(input("Enter disk threshold: ")) 

for i in range(5):
  def check_cpu_memory_disk(cpu_threshold,mem_threshold,disk_threshold):
    cpu_usage = psutil.cpu_percent(interval=1)
    virtual_mem_usage = psutil.virtual_memory().percent
    swap_mem_usage = psutil.swap_memory().percent
    disk_usage = psutil.disk_usage('/').percent

    if(cpu_usage > cpu_threshold):
      print("CPU Alert Email Sent...")
    else:
      print("CPU in Safe State:")

    if(virtual_mem_usage > mem_threshold):
      print("Memory Alert Email Sent...")
    else:
      print("Memory in Safe State...")

    if(disk_usage > disk_threshold):
      print("Disk Alert Email Sent...")
    else:
      print("Disk in Safe State...")

  check_cpu_memory_disk(cpu_threshold,mem_threshold,disk_threshold)