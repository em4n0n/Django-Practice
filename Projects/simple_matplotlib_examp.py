# Import the necessary modules.
import matplotlib.pyplot as plt
import numpy as np

# Generate random data for the plot.
x = np.random.rand(100)
y = np.random.rand(100)

# Create the scatter plot.
plt.scatter(x, y)

# Add labels to the axes.
plt.xlabel('X')
plt.ylabel('Y')

# Show the plot.
plt.show()