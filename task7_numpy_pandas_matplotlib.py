

import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")  # allows saving plots without a display/GUI window
import matplotlib.pyplot as plt

# b. NumPy: 1D array of 10 numbers, mean, sum, reshape to 2x5
numbers_array = np.array([12, 4, 17, 9, 25, 3, 30, 8, 14, 21])
array_mean = numbers_array.mean()
array_sum = numbers_array.sum()
reshaped_array = numbers_array.reshape(2, 5)

print("b. NumPy 1D array:", numbers_array)
print("   Mean:", array_mean)
print("   Sum:", array_sum)
print("   Reshaped to 2x5:\n", reshaped_array)

# c. NumPy: element-wise arithmetic on two arrays
array_a = np.array([10, 20, 30, 40, 50])
array_b = np.array([1, 2, 3, 4, 5])

print("\nc. Element-wise arithmetic:")
print("   array_a + array_b:", array_a + array_b)
print("   array_a - array_b:", array_a - array_b)
print("   array_a * array_b:", array_a * array_b)
print("   array_a / array_b:", array_a / array_b)

# d. Pandas: DataFrame from a dictionary, 4+ columns, 5 rows of student data
student_data = {
    "name": ["Alice", "Brian", "Carol", "David", "Eunice"],
    "age": [21, 22, 20, 23, 21],
    "course": ["IT", "CS", "IT", "Business", "CS"],
    "marks": [78, 45, 62, 88, 39],
}
students_df = pd.DataFrame(student_data)
print("\nd. Student DataFrame:")
print(students_df)

# e. Pandas: filter rows where marks > 50
passed_students = students_df[students_df["marks"] > 50]
print("\ne. Students with marks > 50:")
print(passed_students)

# f. Matplotlib: bar chart of names vs marks
plt.figure()
plt.bar(students_df["name"], students_df["marks"], color="steelblue")
plt.title("Student Marks")
plt.xlabel("Student Name")
plt.ylabel("Marks")
plt.tight_layout()
plt.savefig("bar_chart_marks.png")
plt.close()
print("\nf. Bar chart saved as 'bar_chart_marks.png'")

# g. Matplotlib: line graph showing a trend, saved as .png
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
data_usage_mb = [120, 150, 90, 200, 180, 250, 300]

plt.figure()
plt.plot(days, data_usage_mb, marker="o", color="darkorange")
plt.title("Weekly Data Usage Trend")
plt.xlabel("Day of the Week")
plt.ylabel("Data Usage (MB)")
plt.tight_layout()
plt.savefig("weekly_trend.png")
plt.close()
print("g. Line graph saved as 'weekly_trend.png'")