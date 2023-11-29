import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

# Initialize empty lists to store data
x_data = []
y_data = []

# Create a figure and axis
fig, ax = plt.subplots()
line, = ax.plot([], [], marker='o', linestyle='-', color='b')

# Set the axis limits
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

# Update function for animation
def update(frame):
    x_data.append(frame)
    y_data.append(np.random.uniform(1, 10))
    line.set_data(x_data, y_data)
    return line,

# Create the animation
ani = FuncAnimation(fig, update, frames=np.arange(0, 10, 1), interval=1000, blit=True)

# Show the plot
plt.show()
