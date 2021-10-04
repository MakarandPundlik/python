# dictionaries 
# same as hashmap in Java

student = {'name':'Makarand','age':22,'courses':['DSA','OS','DBMS','Digital Communication']}

print(student)

#to access individual keys
print(student['name'])

#keys can be any mutable data type

#if key exists 
print(student.get('name')) #returns value
print(student.get('phone','Not found')) #return none, 2nd parameter String to be returned when key is not found

student['phone'] = '34523467534'
student['name'] = 'Samu' # overwrites if already exists

#update in one go
student.update({'name':'Makarand','age':'23','phone':'69696969'})
print(student)

#to delete specific keys, pop method is also applicable here
del student['age']
print(student)

#size of dixtionary
print(len(student))

# to get all keys and values
print(student.keys())
print(student.values())

#key value pair representation
print(student.items())

#loop through keys and values 
for key,value in student.items():
    print(key,value)

