

# a. Built-in functions: len(), max(), sorted()
scores = [67, 89, 45, 92, 78]
print("a. Built-in functions:")
print("   len(scores):", len(scores))
print("   max(scores):", max(scores))
print("   sorted(scores):", sorted(scores))


# b. User-defined function: calculate_area
def calculate_area(length, width):
    """Returns the area of a rectangle."""
    return length * width


area = calculate_area(8, 5)
print("\nb. calculate_area(8, 5):", area)


# c. Function with default parameter values
def greet_student(name, course="Undeclared"):
    """Greets a student, using a default course if none is given."""
    print(f"Hello {name}, you are enrolled in {course}.")


print("\nc. Default parameter demo:")
greet_student("Susan")                     
greet_student("Peter", "Data Science")      


# d. Function accepting *args
def sum_all(*args):
    """Sums any number of arguments passed in."""
    return sum(args)


print("\nd. sum_all(1, 2, 3):", sum_all(1, 2, 3))
print("   sum_all(5, 10, 15, 20):", sum_all(5, 10, 15, 20))

# e. Lambda function to square a number, used with map()
square = lambda n: n ** 2
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(square, numbers))
print("\ne. Squaring numbers with lambda + map():")
print("   Original:", numbers)
print("   Squared:", squared_numbers)


# f. Variable scope: local vs global, using the global keyword
counter = 0 


def increment_counter():
    """Modifies the global counter variable."""
    global counter
    counter += 1  # without 'global', this would create a new LOCAL variable


def show_local_scope():
    """Demonstrates a local variable that only exists inside this function."""
    local_message = "I only exist inside this function"
    print("  ", local_message)


print("\nf. Variable scope demo:")
print("   Counter before:", counter)
increment_counter()
increment_counter()
print("   Counter after two increments (global):", counter)
show_local_scope()