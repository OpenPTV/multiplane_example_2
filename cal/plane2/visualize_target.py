import matplotlib.pyplot as plt

# Read the data from plane1.txt
data = []
with open('/home/user/Downloads/2025_03_05_Data_set/multiplane_example_2/cal/plane1/plane1.txt', 'r') as file:
    for line in file:
        parts = line.split()
        data.append((int(parts[0]), float(parts[1]), float(parts[2])))

# Extract IDs, x, and y coordinates
ids = [row[0] for row in data]
x_coords = [row[1] for row in data]
y_coords = [row[2] for row in data]

# Plot the scatter plot
plt.scatter(x_coords, y_coords)

# Find the corners
min_x = min(x_coords)
max_x = max(x_coords)
min_y = min(y_coords)
max_y = max(y_coords)

corners = [
    (min_x, min_y),
    (min_x, max_y),
    (max_x, min_y),
    (max_x, max_y)
]

# Annotate the corners with their IDs
for corner in corners:
    for i, (x, y) in enumerate(zip(x_coords, y_coords)):
        if (x, y) == corner:
            plt.annotate(ids[i], (x, y), textcoords="offset points", xytext=(0,10), ha='center')

# Show the plot
plt.xlabel('X')
plt.ylabel('Y')
plt.title('2D Scatter Plot with Corner IDs')
plt.show()
# Save the plot as an image file in the same folder
output_path = '/home/user/Downloads/2025_03_05_Data_set/multiplane_example_2/cal/plane1/scatter_plot.png'
plt.savefig(output_path)