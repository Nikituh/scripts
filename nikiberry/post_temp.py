import os
import requests
import time
import sched, time
import get_temp

server = "http://nikitech.eu/"
controller = "Nikiberry/"
function = "UploadTemperature"
url = server + controller + function

hour = 60 * 60

scheduler = sched.scheduler(time.time, time.sleep)

def post_temperature(scheduler_param):
    
    inside_temp = get_temp.read_temp(get_temp.inside_device)
    outside_temp = get_temp.read_temp(get_temp.outside_device)
    date = int(round(time.time() * 1000))
    
    inside_temp = str(inside_temp)
    outside_temp = str(outside_temp)
    date = str(date)
    
    print("Posting temperature: ")
    print("inside: " + inside_temp)
    print("outside: " + outside_temp)
    print("______________________")
    print("\n")
    
    data = {
        'inside': inside_temp,
        'outside': outside_temp,
        'date': date
        }


    request = requests.post(url, data = data)
    print("Response: " + request.text)
    
    scheduler.enter(hour, 1, post_temperature, (scheduler_param,))

print("Started temperature update script. Next upload will be in one hour")

scheduler.enter(hour, 1, post_temperature, (scheduler,))
scheduler.run()



