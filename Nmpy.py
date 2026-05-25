import matplotlib.pyplot as plt
import numpy as np

# Data
x = np.arange(1, 19)
y1 = x * 2
y2 = x ** 2

# Create figure
plt.figure(figsize=(10, 6))

# Line plot
plt.plot(x, y1, label='2x', color='blue', marker='o', linewidth=2)

# Second line
plt.plot(x, y2, label='x^2', color='red', marker='s', linewidth=2)

# Labels and title
plt.title('Matplotlib Demo Program', fontsize=16)
plt.xlabel('X Values')
plt.ylabel('Y Values')

# Grid and legend
plt.grid(True)
plt.legend()

# Show graph
plt.show()