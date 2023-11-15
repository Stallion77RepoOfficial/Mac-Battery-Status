import psutil
import time
import os

while True:
    battery = psutil.sensors_battery()
    plugged = battery.power_plugged
    percent = str(battery.percent)
    plugged = "Şarj Oluyor" if plugged else "Şarj Olmuyor"
    
    cycle_count = os.popen('system_profiler SPPowerDataType | awk \'/Cycle Count/ {print $3}\'').read().strip()
    health = os.popen('system_profiler SPPowerDataType | awk \'/Condition/ {print $2}\'').read().strip()
    
    if plugged == "Şarjda":
        wattage = os.popen('system_profiler SPPowerDataType | awk \'/Wattage/ {print $2}\'').read().strip()
        print(f"Şarj Yüzdesi: {percent}% | Şarj Durumu: {plugged} | Şarj Edilme Sayısı: {cycle_count} | Sağlık Durumu: {health} | Watt Girişi: {wattage}W")
    else:
        print(f"Şarj Yüzdesi: {percent}% | Şarj Durumu: {plugged} | Şarj Edilme Sayısı: {cycle_count} | Sağlık Durumu: {health}")
    
    time.sleep(1)