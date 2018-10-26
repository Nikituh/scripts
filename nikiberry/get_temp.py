import os
import requests
import time
import sched, time

# From:
# https://matthewmoisen.com/blog/how-to-use-the-ds18b20-temperature-sensor-with-raspberry-pi/

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

inside_device = "28-000009b8661b"
outside_device = "28-000009b7d3ca"

def temp_raw(sensor):
    
    base = "/sys/bus/w1/devices/"
    end = "/w1_slave"
    
    f = open(base + sensor + end, 'r')
    lines = f.readlines()
    f.close()
    
    return lines

def read_temp(sensor):

    lines = temp_raw(sensor)
    
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = temp_raw()
    
    temp_output = lines[1].find('t=')

    if temp_output != -1:
        temp_string = lines[1].strip()[temp_output+2:]
        temp_celsius = float(temp_string) / 1000.0
        temp_fahrenheit = temp_celsius * 9.0 / 5.0 + 32.0
        
        return temp_celsius

