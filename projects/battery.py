import psutil # pip install psutil
from jarvis import speak

battery = psutil.sensors_battery()
plugged = battery.power_plugged
percent = battery.percent
percent = battery.percent
b = int(percent)

# speak(f'Total Battery Charged {percent} %')

if b <= 76 and plugged == False:
    speak("Please Plugin Charger Battery Low")