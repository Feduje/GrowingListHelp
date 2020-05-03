myUniqueList = []
def addToList(x):
	if myUniqueList == []: # If the list is empty, append x
		myUniqueList.append(x)
	elif myUniqueList[0] == x: # If the first element is equal to x, don't do anything
		return False           # and return False
	else:
		myUniqueList.append(x) # Otherwise, add it to myUniqueList
		return True            # and return True
addToList(0)
addToList(0)
addToList(1)
print(myUniqueList)
"""
As I understand it, I want to compare the x given with every element of the list.
The problem is that I can't figure out how to define "every element" for the check that I want to do
in a list that keeps growing.
"""