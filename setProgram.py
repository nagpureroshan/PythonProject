numbers = {1, 2, 3, 3, 4}
print(numbers)  # {1, 2, 3, 4}

print("Length of the set:", len(numbers))  # 4

set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

print(set1)
print(set2)
print(set3)
print(type(set1))
print(type(set2))
print(type(set3))

thisset = set(("coconut", "cashewnut", "peanut"))
print(thisset)

for x in thisset:
    print(x)

print("banana" in set1)  # True
print("grape" in set1)  # False

set1.add("orange")
print(set1)

thisset.update(set1)
print(thisset)

mylist = ["kiwi", "melon", "mango"]
thisset.update(mylist)
print(thisset)

thisset.remove("banana")
thisset.discard("mango")  # No error if "banana" is not present

x=thisset.pop()  # Removes and returns an arbitrary element from the set
print("Popped element:", x)
print(thisset)

set4 = set1.union(set2)
print('Set1 join Set2: ', set4)

set5 = set1 | set2
print('Set1 | Set2: ', set5)

set6 = set1.union(list(set2))
print('Set1 union with list of Set2: ', set6)

del thisset
try:    print(thisset)  # This will raise a NameError since thisset is deleted
except NameError as e:    print("Error:", e)    
