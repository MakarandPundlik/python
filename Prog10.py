# slicing in list 
#slicing is a way to extract certain elements from list 

my_list = [1,2,3,4,5,6,7,8,9,10]
          #0,1,2,3,4,5,6,7,8,9
          # -10,-9,-8-,m-7,-6,-5,-4,-3,-2,-1
          #we can us enegative index also 

print(my_list[-10])
print(my_list[-1])

#to extract renage of value 
print(my_list[0:3])  #start index,end index+1, same a java 

print(my_list[4:8])
print(my_list[:]) #to print entire list 
#to print start point to eol [x:]
#to print 0 to ending poiny [:x]

# same is applicable to negative numbers 
print(my_list[-1:-3]) #if start point > end point, prints empty list does not throw any exceptions 

#to skip numbers in between 
#start index,end index,skip numbers 
#negative step applicable 
print(my_list[0:-1:2] ) #start from 0th index skip 2 numbers after every one number and print 

