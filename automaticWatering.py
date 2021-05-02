from MCP3008 import MCP3008

import time
import requests
import math
sensor = MCP3008()



def main():
    
    voltage = sensor.read( channel = 0 ) # You can of course adapt the channel to be read out
    percentage = voltage_to_moisture(voltage)
    if percentage == 0:
        time.sleep(5)
        voltage = sensor.read( channel = 0 )
        percentage = voltage_to_moisture(voltage)

    reqParams = { 'seconds' : 15 }
    reqTwo = { 'seconds' : 6 } 

    reqUrl = 'https://automatic-watering.herokuapp.com/api/watertime'
    #reqUrl = 'http://localhost:5000/api/watertime'
    if percentage < 15:
        req = requests.post(reqUrl, data = reqParams)
    #elif percentage < 50:
    #    req = requests.post(reqUrl, data = reqTwo)
    #print(percentage)
    #if percentage < 10:
    #print("Applied voltage: %.2f" % (value / 1023.0 * 3.3) )
    print(percentage)

def voltage_to_moisture(voltage):
    percentage = 1 - (voltage - 465) / 200
    percentage = math.trunc(percentage * 100)
    if percentage < 0:
        percentage = 0
    return percentage

main()

