#regular methods class methods and static methods 



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

