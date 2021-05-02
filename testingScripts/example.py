from MCP3008 import MCP3008

import time

adc = MCP3008()


while True:

    value = adc.read( channel = 0 ) # You can of course adapt the channel to be read out



    print("Applied voltage: %.2f" % (value / 1023.0 * 3.3) )
    print(value)
    perc = (1 - ( value - 465 ) / 220)
    if perc < 0:
        perc = 0
    print(perc)
    time.sleep(1)



