class Employee:
    #pass #to keep class body empty 
    def __init__(self,first,last,pay): #constructor in another language
        #by convention slef which is first object in constructor is object itself, anologous to this keyword in java
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first+'.'+last+'@gmail.com'

    def fullname(self):#each method in class will take self(this object) as argument
        return '{} {}'.format(self.first,self.last)
# e1 = Employee()
# print(e1)
# e2 = e1 #referencing the same object 
# print(e1)

e1 = Employee('Makarand','Pundlik',50000) #self is taken care of by compiler
e2 = Employee('Tanmay','Pardeshi',60000)

print('{} {}'.format(e1.first,e1.last))
print(e1.fullname())