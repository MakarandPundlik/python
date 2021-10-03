# lists sets tuples

#list
courses = ['maths','physics','geography'];
print(courses);
print(len(courses)) # returns number of items in square bracket
print(courses[0]) # accessing elements of lists
print(courses[-1]) #-1 is always last index
#print(courses[6]) # index out of bounds IndexError: list index out of range

# for specified range 
print(courses[0:2]) # start index , end index +1

# modify list 
courses.append('art')
print(courses)

courses.insert(0,'computer science') 
print(courses)

courses.insert(10,'dsa') #if index > list length then it is appended 
print(courses)

courses_2 = ['DBMS','OS','CNS']
#courses.insert(0,courses)  # entire list as object gets inserted
#print(courses)

courses.extend(courses_2) #individual element get appended at list 
print(courses)

courses.remove('geography') #removes geography
print(courses)

courses.pop() #removes last element bydefault
print(courses)

courses.reverse()
print(courses) #reverse order 

courses.sort() #sort in alphabatical order if both cases are present , preference is given to upper case
print(courses)

courses.sort(reverse=True) #reverse order
print(courses) 

#without altering the main list
sorted_courses = sorted(courses)
print(sorted_courses,courses)

#to find index of given element
print(courses.index('art'))

print('Art' in courses) # returns true/false case sensitive

for index,item in enumerate(courses,start=1): #can start at any index
    print(index,item)

course_str = ', '.join(courses) # puts specific string after every element in 
print(course_str)

courses = course_str.split(', ')#split string back into a list
print(courses)


#tuples
# tuples are same as list but are immutable
tuple_1 = ('maths','science','english','history','geography')
tuple_2 = tuple_1

print(tuple_1,tuple_2)

#tuple_1[0] = 'art' #'tuple' object does not support item assignment

#print(tuple_1,tuple_2)

#sets
set_1 = {'maths','science','english','history','geography'}
set_2 = {'science','geography','italian','german','french'}
print(set_1) #prints in unordered way

print(set_1.intersection(set_2)) #prints common elements
print(set_1.union(set_2)) #prints all elements but common elements only once

print(set_1.difference(set_2)) #all except common elements

#create empty list
empty_list = []
empty_list = list()

#empty set
empty_set = {} #not true, it is dictionary
empty_set = set()

#empty tuple
empty_tuple = ()
empty_tuple = tuple()
