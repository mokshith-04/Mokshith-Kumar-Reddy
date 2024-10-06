import matplotlib.pyplot as plt
import numpy as np

# Read data from the file
filename = 'dat.txt'
x_circle = []
y_circle = []
x_line = []
y_line = []

with open(filename, 'r') as file:
    for line in file:
        parts = line.strip().split(';')
        x = float(parts[0])
        y = float(parts[1])
        if parts[2] == 'Circle':
            x_circle.append(x)
            y_circle.append(y)
        elif parts[2] == 'Line':
            x_line.append(x)
            y_line.append(y)

# Plotting the circle
plt.figure(figsize=(8, 8))
plt.scatter(x_circle, y_circle, color='blue', label='Circle', s=1)

# Plotting the line
plt.plot(x_line, y_line, color='red', label='Line', linewidth=2)

# Plot the circle with bold edges
circle_edge = plt.Circle((0, 0), 1.5, color='blue', fill=False, linewidth=2, linestyle='-')
plt.gca().add_artist(circle_edge)

# Define intersection points
intersection_points = [(1.5, 0), (0, 1.5)]

# Generate points for the shaded area
# Points along the line
x_fill = np.linspace(0, 1.5, 100)
y_fill = -x_fill + 1.5  # y = -x + 1.5 (line equation)

# Points along the circle
circle_x = np.linspace(0, 1.5, 100)
circle_y = np.sqrt((1.5 ** 2) - circle_x ** 2)  # upper half of the circle

# Combine the points for the shaded area
x_shade = [intersection_points[0][0]] + list(circle_x) + [intersection_points[1][0]]
y_shade = [intersection_points[0][1]] + list(circle_y) + [intersection_points[1][1]]

# Shade the smaller area intersected by the line and the circle
plt.fill(x_shade, y_shade, color='lightblue', alpha=0.5)

# Annotate points of intersection
plt.annotate('A(1.5, 0)', (1.5, 0), textcoords="offset points", xytext=(0,10), ha='center', fontsize=12, fontweight='bold', color='black')
plt.annotate('B(0, 1.5)', (0, 1.5), textcoords="offset points", xytext=(-10,-10), ha='center', fontsize=12, fontweight='bold', color='black')

# Set limits and labels
plt.xlim(-2, 2)
plt.ylim(-2, 2)
plt.title(' ')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.axhline(0, color='black', linewidth=0.5, ls='--')
plt.axvline(0, color='black', linewidth=0.5, ls='--')
plt.grid()
plt.legend()
plt.gca().set_aspect('equal', adjustable='box')
plt.savefig('plot.png')
plt.show()

