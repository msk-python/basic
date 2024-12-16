import psutil # pip install psutil

battery = psutil.sensors_battery()
plugged = battery.power_plugged
percent = battery.percent

b = int(percent)



# print( psutil.sensors_battery() )
# print( psutil.virtual_memory() )
# print( psutil.swap_memory() )
# print( psutil.disk_partitions() )
# print( psutil.cpu_percent() )
# print( psutil.pids() )
# print( psutil.Process(7055) )