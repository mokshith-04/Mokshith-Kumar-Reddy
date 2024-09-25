import matplotlib.pyplot as plt

def read_triangle_coordinates(filename):
    coordinates = []
    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split(';')
            # Extract x and y coordinates from the first part
            x, y = map(float, parts[0:2])
            coordinates.append((x, y))
    return coordinates

def draw_triangle(coordinates, save_as=None):
    # Unzip the coordinates into x and y lists
    x, y = zip(*coordinates)

    # Create the plot
    plt.figure()
    
    # Draw the triangle lines
    plt.plot(x + (x[0],), y + (y[0],), marker='o')  # Draw the triangle lines
    
    # Label each point with A, B, C
    labels = ['A', 'B', 'C']
    for i, (x_coord, y_coord) in enumerate(coordinates):
        plt.text(x_coord, y_coord, f'{labels[i]}({x_coord}, {y_coord})', fontsize=12, ha='right')

    plt.xlim(-1, 7)
    plt.ylim(-1, 6)
    plt.title(' ')
    plt.grid()
    plt.axhline(0, color='black', linewidth=0.5, ls='--')
    plt.axvline(0, color='black', linewidth=0.5, ls='--')
    plt.gca().set_aspect('equal', adjustable='box')
    
    # Save the figure if a filename is provided
    if save_as:
        plt.savefig(save_as)
    
    plt.show()

if __name__ == "__main__":
    filename = 'dat.txt'
    triangle_coords = read_triangle_coordinates(filename)
    draw_triangle(triangle_coords, save_as='plot.png')  # Save as PNG

