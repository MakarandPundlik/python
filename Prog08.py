#program on import and export of modules

#import mymodule as mm #can be imported as alias
import sys
from mymodule import find_index as fi,test # this also can be imported as alias,but we cannot access any variables in that modules

#to import everuthing use *

#concept of modules is analogous to packages in Java

#to import packages/modules outside the directory



courses = ['Maths','Science','Geography','Computer Science','Data Structures']

index = fi(courses,'Maths')

print(index)
print(test)

print(sys.path)
#directory where the code resides, python paths env variables, std libraries, std packages 
