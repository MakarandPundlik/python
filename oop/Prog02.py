#program on class variables/static variables

class Employee:
    rise = 1.04
    total_emp = 0
    #pass #to keep class body empty 
    def __init__(self,first,last,pay): 
        
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first+'.'+last+'@gmail.com'
        Employee.total_emp+=1
   
    def fullname(self):
        return '{} {}'.format(self.first,self.last)

    def appraisal(self):
        #self.pay = int(self.pay*rise) rise is not defined 
        #we have to access class variables using classname or instance of class
        self.pay = int(self.pay*self.rise)

e1 = Employee('Makarand','Pundlik',50000) 
e2 = Employee('Tanmay','Pardeshi',60000)

print(e2.pay)
e2.appraisal()
print(e2.pay)

print(Employee.rise)
print(e1.rise)
print(e2.rise)
print("\n")
e1.rise = 1.05 #just like java this will change rise amount of e1 only
e2.rise = 1.07 #applicable for e2 only
Employee.rise = 1.06 #applicable for Employee clas memeber only and will affect instances here onwards 

print(Employee.rise)
print(e1.rise)
print(e2.rise)

e3 = Employee('Kaustubh','Odak',60000)
print(e2.rise)


print(e3.__dict__) #if rise is not called in lifecycle of this object then it wont have a copy of rise 
print(Employee.__dict__)


#get me the number of emplyees created in the program
print(Employee.total_emp)