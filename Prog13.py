#string formatting

person = {'name':'makarand','age':22}

#can only concatenate str (not "int") to str
myintro = 'Hello Good Morning!, my name is ' + person['name'] + ' and iam ' + str(person['age']) + ' years old'

myintro = 'Hello Good Morning!, my name is {} and iam {} years old'.format(person['name'],person['age']) 

myintro = 'Hello Good Morning!, my name is {0} and iam {1} years old'.format(person['name'],person['age']) 

myintro = 'Hello Good morning my name is {0[name]} and i am {0[age]} old'.format(person)
print(myintro)


tag = 'h1'
text = 'This is breaking news'

news = '<{0}><{1}></{0}>'.format(tag,text)
print(news)


print("======================================================")

#formatting with the class
class Person():
    def __init__(self,name,age) -> None:
        self.name = name
        self.age = age


p1 = Person('makarand',22)

myintro = 'my name is {0.name} and i am {0.age} years old'.format(p1)


#passing keywrord args to string
myintro = 'my name is {name} and i am {age} years old'.format(name='makarand',age=22)

#by unpacking dictionary 
myintro = 'my name is {name} and i am {age} years old'.format(**person)
print(myintro)

for i in range(1,11):
    sentence = 'the number is {:03}'.format(i) #padding digits 
    print(sentence)

#to format decimal places
pi = 3.1425435456
sentence = 'the value of pi is {:.2f}'.format(pi)
print(sentence)

sentence = 'value of 1Mb is {:,.2f}'.format(1000**2) # ** is power
print(sentence)

import datetime
mydate = datetime.datetime(2000,8,23,18,21,00) #if last 3 parameters are not given, default is 00:00:00
sentence = '{:%d,%b,%a,%Y}'.format(mydate)
print(sentence)

#23rd augst fell on the wednesday and it was nth day of the year
#if placeholders>number of args then specify position of args
sentence = '{0:%d,%b} fell on the {0:%A} was the {0:%j} of the year'.format(mydate)
print(sentence)


