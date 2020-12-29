# 2D Terrain Generator
# V0LT
# Licensed under the GPLv3
# Version 1.0


# ----- Configuration -----

# To add more diversity to generated land, 'fields' can be randomly created. Fields are just random instances of flat land, which generate indpendently of the rest of the terrain.
field = False # Determines whether or not fields will generate.
fieldmin = 3 # The minimum field length that can be randomly selected.
fieldmax = 12 # The maximum field length that can be randomly selected.
fieldchance = 100 # How likely a field is to generate (1 in x chance). The higher the number, the less likely. A value of 1 means the entire terrain will be a field.

# To prevent terrain from reaching too far off the screen, "rebound zones" are used to bias the terrain generation near the edges. When passing the minimum/maxium rebound zones, the terrain is more likely to beginning moving back towards the center. If you have a smaller screen, you may want to change the max rebound zone to something lower.
reboundzonemin = 10 # The minimum width the terrain can be before it starts rebounding.
reboundzonemax = 190 # The maximum width the terrain can be before it starts rebounding.
reboundzonestrength = 1 # How much of an influence the rebound zone has (The higher the value, the stronger the rebound)

startingwidth = 50 # The starting width of the terrain.
generationdelay = 0.05 # The delay in seconds between each line of terrain generated. A value of 0 will cause the lines to generate as fast as the CPU can handle.

roughness = 5 # How much variation in elevation the terrain has. The higher the number, the more likely steep slopes are to occur.

# ----- End of Configuration -----



import random
import time

width = startingwidth
increment = 0

def printLine():
    line = ""
    for i in range(width):
        line = line + "#"
    print(line)
while True:
    if random.randint(1, fieldchance) == 1 and field == True:
        increment = 0
        for i in range(random.randint(fieldmin,fieldmax)):
            printLine()
            time.sleep(generationdelay)
   
    if (width <= reboundzonemin):
        increment = increment + random.randint(0,reboundzonestrength) 
    if (width >= reboundzonemax):
        increment = increment - random.randint(0,reboundzonestrength)

    increment = increment + random.randint(-1 - round(increment/roughness), 1 - round(increment/roughness))
    width = width + increment
    printLine()
    time.sleep(generationdelay)

