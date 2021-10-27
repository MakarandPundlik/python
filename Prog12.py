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
