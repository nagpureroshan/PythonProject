from itertools import count
from operator import index


studentTuple = ("John", "Doe", 20, "Computer Science")
print("Student Tuple:", studentTuple)
print("First Name:", studentTuple[0])
print("Last Name:", studentTuple[1])
print("Age:", studentTuple[2])
print("Major:", studentTuple[3])

(fname, Lname, age, major) = studentTuple  # Unpacking the tuple into variables
print("First Name:", fname)
print("Last Name:", Lname)
print("Age:", age)
print("Major:", major)

(*name, age, major) = studentTuple
print("Name:", name)


print('range of tuple: ', studentTuple[0:3])  # Print a slice of the tuple from index 0 to 2 (inclusive)
print(studentTuple[:1])
print(studentTuple[2:])  # Print a slice of the tuple from index 2 to the end
print(studentTuple[-3:-1])  # Print the last element of the tuple

if "John" in studentTuple:
    print("John is in the student tuple.")

print("Length of the tuple:", len(studentTuple))  # Print the length of the tuple

# Attempting to modify a tuple (this will raise an error)
#try:
 #   studentTuple[2] = 21  # This will raise a TypeError
#except TypeError as e:
 #   print("Error:", e)

try:
    studentList = list(studentTuple)  # Convert the tuple to a list
    studentList[2] = 21  # Modify the age in the list
    studentTuple = tuple(studentList)  # Convert the list back to a tuple
    print("Modified Student Tuple:", studentTuple)
except Exception as e:
    print("Error:", e)


try:
    studentList = list(studentTuple)  # Convert the tuple to a list
    studentList.append("IT")  # Add a new element to the list
    studentList.append("AI")  # Add another element to the list
    studentTuple = tuple(studentList)  # Convert the list back to a tuple
    print("Extended Student Tuple:", studentTuple)
except Exception as e:
    print("Error:", e)
    print("Failed to extend the student tuple.")

(fname, Lname, age, *major) = studentTuple  # Unpacking the tuple into variables
print("Majors:", major)

for item in studentTuple:
    print("Item:", item) 

counter = 3
while counter < len(studentTuple):
    print("Counter Item:", studentTuple[counter])
    counter += 1

itemCount = studentTuple.count("Computer Science")# Count the occurrences of "Computer Science" in the tuple
print("Item Count:", itemCount)

indexNumber = studentTuple.index("Computer Science")# Get the index of the first occurrence of "Computer Science" in the tuple
print("Index Number:", indexNumber)
