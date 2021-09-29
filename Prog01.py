# data types in python
message = "Hello World"

# message = 'Makarand's World'
message = 'Makarand\'s World'  # escape sequence character in python is same as Java
message = "Makarand's World" # alternative to escape sequence character
message = """ India is my country all indians are my brothers and
sisters , I love my country
Blah blah blah
fsdgag""" # tripple double quotes can provide paragraph
print(message)

# function to get length of string
print(len(message))

message = "Makarand's World"

# to access individual characters in a String
print(message[0]) # 0 based indexing

# to print single word
print(message[0:5]) # first index is inclusive and second is not eg [0,5)
print(message[:5])  #default start location is 0
print(message[0:]) #default end location is length of String

# some methods of string
print(message.lower()) # all lowercase
print(message.upper()) # all uppercase
print(message.count('a')) # count number of occurrences of letter, if doesnt exist will return -1 same as Java



