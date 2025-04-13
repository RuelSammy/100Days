import matplotlib.pyplot as plt
import numpy as np

# 1. Line Chart
x = [1, 2, 3, 4, 5]
y = [10, 12, 8, 14, 11]

plt.figure(figsize=(6, 4))
plt.plot(x, y, marker='o', linestyle='-', color='b')
plt.title("Line Chart Example")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.tight_layout()
plt.show()

# 2. Bar Chart
categories = ['A', 'B', 'C', 'D']
values = [23, 17, 35, 29]

plt.figure(figsize=(6, 4))
plt.bar(categories, values, color='skyblue')
plt.title("Bar Chart Example")
plt.xlabel("Categories")
plt.ylabel("Values")
plt.tight_layout()
plt.show()

# 3. Pie Chart
labels = ['Apples', 'Bananas', 'Cherries', 'Dates']
sizes = [25, 30, 20, 25]

plt.figure(figsize=(6, 6))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
plt.title("Pie Chart Example")
plt.axis('equal')
plt.tight_layout()
plt.show()

# 4. Scatter Plot
x = np.random.rand(50)
y = np.random.rand(50)

plt.figure(figsize=(6, 4))
plt.scatter(x, y, color='green')
plt.title("Scatter Plot Example")
plt.xlabel("X values")
plt.ylabel("Y values")
plt.grid(True)
plt.tight_layout()
plt.show()

# 5. Histogram
data = np.random.randn(1000)

plt.figure(figsize=(6, 4))
plt.hist(data, bins=30, color='purple', edgecolor='black')
plt.title("Histogram Example")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()
