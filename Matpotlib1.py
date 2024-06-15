import matplotlib.pyplot as plt
import numpy as np

# Line plot.
# Line plot of sin(x).
x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.plot(x, y)
plt.xlabel("x")
plt.ylabel("sin(x)")
plt.title("Line plot of sin(x)")
plt.show()

# Line plot of cos(x).
x1 = np.linspace(0, 10)
y1 = np.cos(x1)

plt.plot(x1, y1)
plt.xlabel("X axis")
plt.ylabel("cos(x)")
plt.title("Line plot of cos(x)")
plt.show()

# Scatter plot.
x2 = np.random.randn(100)
y2 = np.random.randn(100)

plt.scatter(x2, y2)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Scatter plot of random data")
plt.show()

# Barchart

x3 = ['Apples', 'Oranges', 'Mangoes', 'Avocadoes']
y3 = [10, 5, 15, 4]

plt.bar(x3, y3)
plt.xlabel("Fruits")
plt.ylabel("Quantity")
plt.title("Bar chart of fruit quantities")
plt.show()

# Histogram

data = np.random.randn(1000)

plt.hist(data, bins=30)
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.title("Histogram of random data")
plt.show()