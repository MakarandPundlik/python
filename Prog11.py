#program on list comprehension 

from typing import MutableMapping


nums = [1,2,3,4,5,6,7,8,9,10]

# i want n for each n in nums
my_list = []
for i in nums:
    my_list.append(i)
print(my_list)    

#using list comprehension 
my_list = [n for n in nums]
print(my_list)


# i want n*n for each n in nums
my_list = []
for i in nums:
    my_list.append(i*i)
print(my_list)

#using comprehension
my_list = [n*n for n in nums]
print(my_list)


#i want n for each n in nums if n is even
my_list = []
for i in nums:
    if(i%2==0):
        my_list.append(i)
print(my_list)

#using comp
my_list = [n for n in nums if n%2==0]
print(my_list)


#i want a letter number pair for each letter in abcd and each number in 1234
my_list = []
for  letter in 'abcd':
    for number in '0123':
        my_list.append((number,letter))
print(my_list)        

#using comp
my_list = [(number,letter) for letter in 'abcd' for number in '0123']
print(my_list)


#dictionary comprehension 

names = ['bucky','steve','tony','peter']
heros = ['captain america','iron man','spiderman','winter soldier']

#pairs up one to one 
print(list(zip(names,heros))) #corect way to print zip functions 

# i want dict{name,hero} for each name,hero in zip(name,hero)

my_list = {}
for name,hero in zip(names,heros):
    my_list[name] = hero
print(my_list)    
