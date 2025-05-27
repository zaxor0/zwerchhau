#!/usr/bin/python3

import numpy
import random

sides = 6

for i in range (1,7):
  results = []
  for j in range(0,i):  
    diceResult = random.randint(1,sides) 
    results.append(diceResult)
  print(results)
