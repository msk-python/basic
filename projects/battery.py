import psutil # pip install psutil

battery = psutil.sensors_battery()
plugged = battery.power_plugged
percent = battery.percent

if percent <= 90 and plugged!=True:
    print("Battery Low : ", percent)