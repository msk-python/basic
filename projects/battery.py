import psutil # pip install psutil
from jarvis import speak

battery = psutil.sensors_battery()
plugged = battery.power_plugged
percent = battery.percent

print(percent)