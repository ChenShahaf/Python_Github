#Homework 4 - Lists

#1 Create global list named myUniqueList
#Extra credit create global leftover array
global myUniqueList
global myLeftovers

myUniqueList = []
myLeftovers = []

#2 create a function to add things to the list
#all the values in this function added to the global
#list, unless it's already exist, and if so the function should return False

def add_to_list(value):
    if value in myUniqueList:
        myLeftovers.append(value)
        return False
    else:
        myUniqueList.append(value)
        return myUniqueList

print(add_to_list("apple"))
print(add_to_list("banana"))
print(add_to_list("apple"))
print(add_to_list(5))
print(add_to_list("banana"))
print(myLeftovers)
