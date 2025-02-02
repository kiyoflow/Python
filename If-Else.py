#!/bin/python3

import math
import os
import random
import re
import sys




n = int(input().strip())

if n < 1 or n > 100:
    print("F off")
    
if n%2 == 1:
    print("Weird")
else:
    if n in range(2,5) or n > 20:
        print("Not Weird")
    elif n in range(6,21):
        print("Weird") 


