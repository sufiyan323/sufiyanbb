fruits = ['apple', 'banana', 'cherry']
print("length of the list is")
print(len(fruits))
print("after adding element to end of list")
fruits.append('mango')
print(fruits)
fruits.insert(1,34)
print(fruits)
fruits.extend(['grapes',6])
print(fruits)
print("after removing some elements")
fruits.remove(34)
print(fruits)
fruits.pop(2)
print(fruits)
print("index of perticular element","apple")
print(fruits.index('apple'))
