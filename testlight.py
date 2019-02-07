#!/usr/bin/python
import bh1750
import time

light = bh1750.BH1750()
print("Default parameters:" + str(light.get_light_mode()))
print()

light = bh1750.BH1750(mode = 5)
print("Low resolution, but faster:" + str(light.get_light_mode()))
print()

light = bh1750.BH1750(0, 1, 0) # Address pin low, I2Cbus 1, continuous mode
light.set_mode()
for i in range(20):
    print("Continuous readings, " + str(i) + ":" + str(light.get_light()))
    time.sleep(1)
