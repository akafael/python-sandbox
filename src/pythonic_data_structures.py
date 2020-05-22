# List Comprehensions

# Generate a list with square numbers from 0 to 10
squares = [x ** 2 for x in range(10)]

# List with element that are not equal to 4
not4s = [x for x in squares if x != 4]