# Take 5 numbers as input from the user
n1 = float(input("Enter number 1: "))
n2 = float(input("Enter number 2: "))
n3 = float(input("Enter number 3: "))
n4 = float(input("Enter number 4: "))
n5 = float(input("Enter number 5: "))

# Store numbers in a list
numbers = [n1, n2, n3, n4, n5]

# Sort in descending order
numbers.sort(reverse=True)

# Print result
print("Numbers in descending order:", numbers)