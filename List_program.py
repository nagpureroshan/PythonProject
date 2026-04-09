import random

def get_even_numbers_from_random_list(size, lower=0, upper=100):
    random_list = [random.randint(lower, upper) for _ in range(size)]
    print(random_list)  # Print the generated random list
    
    random_list.append(42)  # Append a specific value to the list
    print('appended 42 to list: ',random_list)  # Print the list after appending

    print('Element at index 3: ', random_list[3])   # Print the element at index 3 of the list

    random_list.pop()  # Remove the last element from the list
    print('popped last element from list: ', random_list)  # Print the list after popping the last element

    random_list.extend([24, 36])  # Extend the list with multiple values
    print(random_list)  # Print the list after extending

    #random_list.pop()  # Remove the last element from the list
    #random_list.pop()  # Remove the last element from the list

    random_list.insert(0, 12)  # Insert a value at the beginning of the list
    print('inserted 12 at start: ', random_list)  # Print the list after inserting

    random_list.pop()  # Remove the last element from the list
    print(random_list)  # Print the list after popping the last element

    random_list.insert(5, 18)  # Insert a value at a specific index
    print('inserted 18 at index 5: ', random_list)  # Print the list after inserting at index

    random_list.pop()  # Remove the last element from the list
    print('popped last element from list: ', random_list)  # Print the list after popping the last element

    print('list from index 1 to 5 (inclusive):', random_list[1:6])  # Print a slice of the list from index 1 to 5 (inclusive)
    print('list from the beginning to index 2 (inclusive):', random_list[:3])  # Print a slice of the list from the beginning to index 2 (inclusive)
    print('list from index 3 to the end:', random_list[3:])  # Print a slice of the list from index 3 to the end

    random_list.sort()  # Sort the list in ascending order
    print('sorted random_list: ', random_list)  # Print the list after sorting

    even_numbers = [num for num in random_list if num % 2 == 0]
    return even_numbers

# Example usage:
even_numbers = get_even_numbers_from_random_list(10)
print(even_numbers)