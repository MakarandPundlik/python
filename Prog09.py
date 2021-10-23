# LEGB
# Local,Elclosing,Global,Built In

# in the same order python checks for scope 

#x = 'global variable x'

def test(z):
    #to work explicitly with global x
    global x #doen not need to be defined previously 
    x = 'local variable x' #2)changed the value of global x ,1)will not override the global variable 
    #print(y)
    print(x) #checks in local scope,then enclosing scope,global scope and then built in scope
    print(z) #scope of z is local to this function

#print(y) #y is not defined 

test('69') 
print(x) #ok, it is a global variable

# def max(): #this will override built in function 
#     pass #null statment 

#built in scope
m = max([1,2,5,3,2,7,8,])#this is going to call min() in local scope because LEGB
print(m)

import builtins  #import statments can be placed wherever you want 
print(dir(builtins)) #builting methods with return statment 


#enclosing scope
#function within function

def outer():
    x = 'outer x'

    def inner():
        nonlocal x # considered as variable from enclosing scope,will change the value of "outer x" to "inner x"
        x = 'inner x' #LEGB rule 
        print(x)

    inner()    
    print(x) #this statment does not have access to 'inner x'

outer()        

