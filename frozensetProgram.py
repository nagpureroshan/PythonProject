frozenset1 = frozenset({1, 2, 3, 4, 5})
frozenset2 = frozenset({4, 5, 6, 7, 8})

print("Frozenset 1:", frozenset1)
print("Frozenset 2:", frozenset2)

print(type(frozenset1))  # <class 'frozenset'>

cp = frozenset1.copy()
print("Copy of Frozenset 1:", cp)

diff1 = frozenset1.difference(frozenset2)
print("Difference between Frozenset 1 and Frozenset 2:", diff1)

diff2 = frozenset2 - frozenset1
print("Difference between Frozenset 2 and Frozenset 1:", diff2)

print(frozenset1 - frozenset2)  # Same as difference

print("Intersection of Frozenset 1 and Frozenset 2:", frozenset1.intersection(frozenset2))

print("Frozenset 1 is disjoint with Frozenset 2:", frozenset1.isdisjoint(frozenset2))

print("Frozenset 1 is subset of Frozenset 2:", frozenset1.issubset(frozenset2))

print("Frozenset 1 is superset of Frozenset 2:", frozenset1.issuperset(frozenset2)) 

print('systemic difference version: ', frozenset1.symmetric_difference(frozenset2))

print('Union of Frozenset 1 and Frozenset 2: ', frozenset1.union(frozenset2))

print('Frozenset 1 | Frozenset 2: ', frozenset1 | frozenset2) 
