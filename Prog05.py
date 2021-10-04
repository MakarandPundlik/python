# conditional statements 

language = 'Python'
if language == 'Java':
	print('The given language is',language)
elif language == 'Python':
    print('Given language is ',language)
else:
    print('No match')
    
# all comparison operators are same as Java except 
# is - checks whether objects share same reference 
    
# Python does not support switch case

# logical operators
user = 'admin'
logged_in = True

if user == 'admin' and logged_in:
    print('Welcome to the dashboard')
else:
    print('Bas credentials')
    
    
# 'and or not ' are the only logical operators in python


a = [1,2,3,4]
b = [1,2,3,4] 

print(a==b) #returns true because contents are same
print('id of a is ',id(a))
print('id of b is ',id(b))
print(a is b) #false because both have different memory locations/id of locations
 
a = [1,2,3,4]
b = a 

print(a==b) #returns true because contents are same
print('id of a is ',id(a))
print('id of b is ',id(b))
print(a is b) #false because both have different memory locations/id of locations 


#special cases for boolean types
#zero of any numeric data type - false
#false - false
#None - false
#{},[],(),'' - false
