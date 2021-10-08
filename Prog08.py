#program on import and export of modules

#import mymodule as mm #can be imported as alias
import sys
from mymodule import find_index as fi,test # this also can be imported as alias,but we cannot access any variables in that modules

#to import everuthing use *

#concept of modules is analogous to packages in Java

#to import packages/modules outside the directory
import antigravity
import random
import math
import datetime
import calendar
import os
courses = ['Maths','Science','Geography','Computer Science','Data Structures']

index = fi(courses,'Maths')

print(index)
print(test)

print(sys.path)
#directory where the code resides, python paths env variables, std libraries, std packages 

random_course = random.choice(courses)

print(random_course)

print(math.radians(90))
print(math.sin(math.radians(90))) #sin function takes arg as radian and not degree

print(datetime.date.today()) #prints date in yyyy-mm-dd format 

print(calendar.isleap(2018)) #return boolean 

print(os.getcwd()) #prints current directory

print(os.__file__) #returns the location of module
print(calendar.__file__)
