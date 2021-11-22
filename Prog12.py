# program on sorting s



li = [3,5,7,1,3,8,1,3,2,3,4,-1,-3]
s_li = sorted(li) #does not change original list, instead returns new list 

print('Sorted list \t',s_li)
print('Original list \t',li)


li.sort() #this will sort original list,return type void 
print('Original list \t',li)

li = [3,5,7,1,3,8,1,3,2,3,4,-1,-3]
s_li = sorted(li,reverse=True) #returns list in descending order
print('Sorted in reverse order \t',s_li)

li.sort(reverse=True) #by default is false 
print('Original list in descending order',li)


#sorting on tuples
tup = (9,5,7,3,54,23,90)
#tup.sort() #tuple object does not have attribute sort 
s_tup = sorted(tup)
print("Sorted tuple\t",s_tup," just for fun")


#sorting on dict
dict = {'name':'Mak','job':'developer','age':'21','OS':'ubuntu20.04'}
s_dict = sorted(dict)
print('Sorted dictionary\t',s_dict) #sorts only keys in key-value pair

#how to sort absolute values ?

li = [-6,4,-5,0,3,5,-1]
s_li = sorted(li,key=abs) #abs will call absolute function internally
print('Sorting according to absolute values\t',s_li)


class Employee():
    def __init__(self,name,age,salary) -> None:
        self.name = name
        self.age = age
        self.salary = salary


    def __repr__(self) -> str:
        return '({},{},{})'.format(self.name,self.age,self.salary)    



e1 = Employee('makarand',22,50000)
e2 = Employee('tanmay',22,70000)
e3 = Employee('siddhesh',22,65000)



#user defined function to sort employees
def e_sort(emp):
    return emp.name

employees = [e1,e2,e3]
s_employees = sorted(employees,key=e_sort,reverse=True)  #TypeError: '<' not supported between instances of 'Employee' and 'Employee'

#using lambda function
s_employees = sorted(employees,key=lambda e:e.salary)

#using attrgetter
from operator import attrgetter

s_employees = sorted(employees,key=attrgetter('name'))

print(employees,"\n",s_employees)

