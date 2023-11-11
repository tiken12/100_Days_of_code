#Creating Lists using List Comprehension
#new_list = [new_item for item in list]
number = [1, 2, 3] # I am just trying to add comments to my codes. 
new_numbers= [n +1 for n in number]
print(new_numbers)

name = "Wikender"
new_name = [letter for letter in name]
print(new_name)

num = range(1,5)
new_num = [n*2 for n in num]
print(new_num)
#Another way to try it
range_num = [no *2 for no in range(1,5)]
print(range_num)

#Conditional list Comprehension
#new_list = [new_item for item in list if test]
names = ["Wikender", "Wendy", "Wesner", "Stone", "Wisgens"]
short_names = [name for name in names if len(name) <6]
print(short_names)

Up_names = [name.upper() for name in names if len(name)> 5]
print(Up_names)