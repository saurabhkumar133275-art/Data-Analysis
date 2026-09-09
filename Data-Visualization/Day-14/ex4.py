import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

sizes = [30, 80, 150, 200, 300]

plt.scatter(x, y, s=sizes, alpha=0.5, edgecolors='blue', linewidths=2)
plt.title("Bubble Plot Example")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()
