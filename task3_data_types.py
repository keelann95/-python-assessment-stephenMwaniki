

# a. Integer variable
age = 22
print("a. Integer -> age:", age, "| type:", type(age))

# b. Float variable and arithmetic
height = 1.75
weight = 68.5
bmi = weight / (height ** 2)
print("\nb. Float -> height:", height, ", weight:", weight)
print("   BMI calculation (weight / height^2):", round(bmi, 2))

# c. Boolean variable used in a conditional expression
is_adult = age >= 18
print("\nc. Boolean -> is_adult:", is_adult)
if is_adult:
    print("   This person is an adult.")
else:
    print("   This person is a minor.")

# d. String: concatenation, slicing, len()
first_name = "Grace"
last_name = "Mumbi"
full_name = first_name + " " + last_name       
initials = full_name[0] + full_name[6]         
print("\nd. String -> full_name:", full_name)
print("   First 5 characters (slicing):", full_name[:5])
print("   Length of full_name (len()):", len(full_name))

# e. List: append(), remove(), indexing
fruits = ["apple", "banana", "orange", "mango", "pear"]
print("\ne. List -> original:", fruits)
fruits.append("grapes")
fruits.remove("banana")
print("   After append('grapes') and remove('banana'):", fruits)
print("   Item at index 0:", fruits[0])

# f. Tuple: demonstrate immutability
coordinates = (10, 20, 30)
print("\nf. Tuple ->", coordinates)
try:
    coordinates[0] = 99
except TypeError as error:
    print("   Attempted to modify tuple, caught error:", error)

# g. Set: duplicates removed automatically
numbers_with_duplicates = {1, 2, 2, 3, 3, 3, 4, 5, 5}
print("\ng. Set (duplicates auto-removed):", numbers_with_duplicates)

# h. Dictionary: access, add, delete a key
student = {"name": "Grace Mumbi", "age": 22, "course": "IT"}
print("\nh. Dictionary -> original:", student)
print("   Accessing 'name':", student["name"])
student["grade"] = "A"          # adding a new key
print("   After adding 'grade':", student)
del student["age"]              # deleting a key
print("   After deleting 'age':", student)

# i. Type casting: int(), float(), str()
num_string = "45"
num_int = int(num_string)          
num_float = float(num_int)         
back_to_string = str(num_float)    
print("\ni. Type casting:")
print("   Original string:", num_string, "| type:", type(num_string))
print("   Cast to int:", num_int, "| type:", type(num_int))
print("   Cast to float:", num_float, "| type:", type(num_float))
print("   Cast back to string:", back_to_string, "| type:", type(back_to_string))