dictCar = {
    "brand": "Toyota",
    "model": "Camry",
    "year": 2020,
    "year": 2021 # type: ignore 
}

print(dictCar)
print(type(dictCar))

# Accessing values
print('Brand: ', dictCar["brand"])
print('Model: ', dictCar["model"])
print('Year: ', dictCar["year"])

brand = dictCar.get("brand")
print('Brand using get method: ', brand)
model = dictCar.get("model")
print('Model using get method: ', model)
year = dictCar.get("year")
print('Year using get method: ', year)

# Keys are overwritten if duplicated, the last value will be used. In this case, the year 2021 will overwrite the year 2020.
print('Item count: ', len(dictCar))

dictUser = dict(name="John", age=30, city="New York")
print(dictUser)

keys = dictCar.keys()
print('Keys: ', keys)
print('values: ', dictCar.values())

#accessing values using keys() and values() methods
for key in dictCar.keys():
    print('print using keys function: ',f'Key: {key},{dictCar[key]}')

for value in dictCar.values():
    print('print using values function: ', f'Value: {value}')

for key, value in dictCar.items():
    print('print using Iterms function: ', f'Key: {key}, Value: {value}')

#copying a dictionary using copy function
dictCarCopy = dictCar.copy()
print('Copied dictionary: ', dictCarCopy)

#copying a dictionary using dict() constructor
dictCarCopy2 = dict(dictCar)
print('Copied dictionary using dict constructor: ', dictCarCopy2)

# Adding a new key-value pair to the dictionary
dictCar["color"] = "red"
print('Keys: ', dictCar.keys())
print('values: ', dictCar.values())

print('Items: ', dictCar.items())

#check if key exists in dictionary
varKey = "brand"
if varKey in dictCar:
    print(varKey, " is present in the dictionary.")
else:
    print(varKey, " is not present in the dictionary.")

#Adding multiple key-value pairs/modifying existing ones to the dictionary using update() method
dictCar.update({"year": 2022, "mileage": 15000})
print(dictCar)

dictCar.pop("model")  # Remove a specific key-value pair from the dictionary
print('After popping model: ', dictCar)

dictCar.popitem()  # Remove the last inserted key-value pair from the dictionary
print('After popping last item: ', dictCar)

#clearing the dictionary
dictUser.clear()
print('After clearing dictUser: ', dictUser)

#deleting the dictionary
del dictUser
try:
    print(dictUser) # This will raise an error since dictUser has been deleted
except NameError:    print("dictUser has been deleted and is no longer accessible.")


