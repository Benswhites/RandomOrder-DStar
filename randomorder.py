import cv2
import numpy as np
import math
import random

image = cv2.imread('factory_world_bw.pgm') #Billedet blir loadet med opencv

#variabler
start = []
goal = []
howmanybots = 9
bots = []
conversion = 407/19.9


for i in range(howmanybots): #Det her laver bare strings (navne) man kan koble til robotterne
    bots.append("bot"+str(i))


for i in bots: #Her blir der lavet random spawn punkter til robotterne (det kan fjernes)
    while True:
        x = int(random.uniform(0, 407))
        y = int(random.uniform(0, 399))
        if np.any(image[x, y] != 0):
            conx = x/conversion
            cony = y/conversion
            start.append([conx, cony])
            break

for i in start: #Her blir der lavet random slut punkter til robotterne (der blir lavet random 1-5 random punkter for hver robot der er)
    rand = int(random.uniform(1, 5))
    localgoal = []
    for j in range(rand):
        while True:
            x = int(random.uniform(1, 407))
            y = int(random.uniform(1, 399))
            if np.any(image[x, y] != 0):
                conx = round(x / conversion, 2)
                cony = round(y / conversion, 2)
                localgoal.append([conx, cony])
                break
    goal.append(localgoal)


print(goal) #prints for at tjekke om det virker
print(bots)