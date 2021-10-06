#user defined module

print('Into user defined module')

test = 'Testing variable'

def find_index(to_search,target):
	for i,value in enumerate(to_search):
		if value==target:
			return i
			
	return -1		