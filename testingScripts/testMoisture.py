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

    reqParams = { 'percentage' : percentage }
    
    reqUrl = 'https://automatic-watering.herokuapp.com/api/moisture'

    #req = requests.post(reqUrl, data = reqParams)


    #print("Applied voltage: %.2f" % (value / 1023.0 * 3.3) )
    print(percentage)
def voltage_to_moisture(voltage):
    percentage = 1 - (voltage - 465) / 200
    percentage = math.trunc(percentage * 100)
    if percentage < 0:
        percentage = 0
    return percentage

main()

