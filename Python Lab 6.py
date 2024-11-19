
def list_operations():
    my_list = [5, 3, 2, 8, 1]
    print("Original List:", my_list)

    # Append an element
    my_list.append(10)
    print("After Append:", my_list)

    # Sort the list
    my_list.sort()
    print("After Sort:", my_list)

    # Reverse the list
    my_list.reverse()
    print("After Reverse:", my_list)

    # Count occurrences of an element
    count_of_2 = my_list.count(2)
    print("Count of 2:", count_of_2)

    # Remove an element
    my_list.remove(8)
    print("After Remove 8:", my_list)
list_operations()

# 2. Passing a list as an argument to a function
def print_list_elements(my_list):
    for element in my_list:
        print(element)
print_list_elements([10, 20, 30, 40, 50])

# 3. Taking variable length arguments and cubing each element
def cube_elements(*args):
    cubed_values = [x**3 for x in args]
    return cubed_values
print(cube_elements(2, 3, 4, 5))

# 4. Tower of Hanoi for n = 3 disks
def tower_of_hanoi(n, source, target, auxiliary):
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    tower_of_hanoi(n-1, source, auxiliary, target)
    print(f"Move disk {n} from {source} to {target}")
    tower_of_hanoi(n-1, auxiliary, target, source)
tower_of_hanoi(3, 'A', 'C', 'B')

# 5. Computing the GCD of two numbers
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
num1 = 56
num2 = 98

# 6. Counting uppercase and lowercase letters in a string
def count_upper_lower(s):
    upper_count = sum(1 for char in s if char.isupper())
    lower_count = sum(1 for char in s if char.islower())
    return upper_count, lower_count
sample_text = "Hello World!"
upper, lower = count_upper_lower(sample_text)

