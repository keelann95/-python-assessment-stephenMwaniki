# a. if-elif-else: classify a student grade based on marks
marks = 72

if marks >= 80:
    grade = "A"
elif marks >= 70:
    grade = "B"
elif marks >= 60:
    grade = "C"
elif marks >= 50:
    grade = "D"
else:
    grade = "F"

print("a. Marks:", marks, "-> Grade:", grade)

# b. for loop: iterate over a list of 5 fruits
fruits = ["apple", "banana", "orange", "mango", "pear"]
print("\nb. Looping through fruits:")
for fruit in fruits:
    print("  -", fruit)

# c. while loop: count 1 to 10, print only even numbers
print("\nc. Even numbers from 1 to 10 (while loop):")
count = 1
while count <= 10:
    if count % 2 == 0:
        print("  ", count)
    count += 1

# d. break and continue in a practical example
print("\nd. break and continue demo:")
print("   Searching for the first fruit starting with 'm':")
for fruit in fruits:
    if fruit.startswith("m"):
        print("   Found:", fruit)
        break  # stop the loop once we find it

print("   Printing all fruits except 'banana':")
for fruit in fruits:
    if fruit == "banana":
        continue  # skip this one, go to the next iteration
    print("  ", fruit)

# e. nested loop: 3x3 multiplication grid
print("\ne. 3x3 multiplication table (grid layout):")
for i in range(1, 4):
    row = ""
    for j in range(1, 4):
        row += str(i * j).rjust(4)
    print(row)