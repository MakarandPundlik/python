#loops 

#for loops

nums = [1,2,3,4,5,6]

for num in nums:
    if num == 3:
        print(num*num,' found')
        break
        
    print(num)
    
 
# loop inside loop
for num in nums:
    for letter in 'abc':
        print(num,letter)
        
#certain number of times

for i in range(-3,0): #starts with 0 and ends with num-1
    print(i)
    
    
    
# while loop
x = 0
while x < 10:
    print(x)
    x++