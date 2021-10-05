#functions 

# def stands for defination 

def helloworld():
	print('hello peter')

#print(helloworld) #prints the memory location
print(helloworld())

#function with arguement and return statement 

def withargs(greeting):
    return '{} peter'.format(greeting)

print(withargs('hello'))

#function with default value of parameter

def defaultvalue(greeting = 'Hi'):
    return '{} peter'.format(greeting)
    
print(defaultvalue())    


#special function
def student_info(*args,**kwargs):
    print(args) #stored in tuples
    print(kwargs) #stored in dictionary 
    
# *before list uppacks items individually 
# ** before dictionary unpacks items individually
# * before dict separates keys only

courses = ['maths','chem','bio']
info = {'name':'mak','age':22}
student_info(*courses,**info)
student_info('maths','science','bio',name='mak',age=54)

    
#putting everything together 
month_days = [0,31,28,31,30,31,30,31,31,30,31,30,31]

def isLeapYear(year):
    return year%4==0 and (year%100!=0 or year%400==0)
    
    
    
def days_in_month(month,year):
        if(month>12 or month<1):
            return 'Invalid arguement'
        
        if(month==2 and isLeapYear(year)):
            return 29
        return month_days[month]


print(days_in_month(1,2000))
print(days_in_month(2,2000))
print(days_in_month(-1,4324))
        