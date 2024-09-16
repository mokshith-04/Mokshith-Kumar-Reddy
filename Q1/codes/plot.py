import matplotlib.pyplot as plt

with open('dat.txt', 'r') as file:
    lines = file.readlines()

x_coords = []
y_coords = []
labels = []

for line in lines:
    parts = line.strip().split(';')
    x_coords.append(float(parts[0]))
    y_coords.append(float(parts[1]))
    labels.append(parts[2])

plt.plot(x_coords, y_coords, marker='o', linestyle='-', color='b')

for x, y, label in zip(x_coords, y_coords, labels):
    plt.text(x, y, label, fontsize=12, ha='right')

plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Graph')

plt.grid(True)
plt.savefig('plot.png')
plt.show()

