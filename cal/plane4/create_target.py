import numpy as np

# Define the number of rows and columns
num_rows = 19
num_cols = 25

# z = 1300.0 # 1st plane is forward 1300 mm for plane 1
# z = 650.0 # 2nd plane, /3DPTV_Illmenau/2025_03_05_Data_set/Target_Positions_BOI.pdf
# z = 0.0 # 3nd plane, /3DPTV_Illmenau/2025_03_05_Data_set/Target_Positions_BOI.pdf
z = -750.0 # 3nd plane, /3DPTV_Illmenau/2025_03_05_Data_set/Target_Positions_BOI.pdf

# Define the spacing between points
spacing = 40.0

# Initialize the matrix with zeros
matrix = np.zeros((num_rows * num_cols, 4))

# Fill the matrix with the appropriate values
id_counter = 4000
for i in range(num_rows):
    for j in range(num_cols):
        index = i * num_cols + j
        matrix[index, 0] = id_counter
        matrix[index, 1] = j * spacing
        matrix[index, 2] = i * spacing
        matrix[index, 3] = z
        id_counter += 1


# Shift the matrix by 1190 - 400 mm up in y direction
matrix[:, 2] += (1190 - 400)

# Shift the matrix by 13 * 40 mm to the left
matrix[:, 1] -= (13 * spacing)

# Adjust the middle grid point at 10th row and 13th column to become at (0, 1190, 1300)
middle_index = (10 - 1) * num_cols + (13 - 1)
# matrix[middle_index, 1] = 0
# matrix[middle_index, 2] = 1190
# matrix[middle_index, 3] = 1300

# Save the matrix to a file
import os
np.savetxt(os.path.join(os.path.dirname(__file__),'plane4.txt'), matrix, fmt='%4d\t%.2f\t%.2f\t%.2f')

import matplotlib.pyplot as plt

# Create a scatter plot
plt.scatter(matrix[:, 1], matrix[:, 2])

# Annotate the middle point
plt.text(matrix[middle_index, 1], matrix[middle_index, 2], str(int(matrix[middle_index, 0])), fontsize=12, ha='right')

# Annotate the corners
corner_indices = [0, num_cols - 1, (num_rows - 1) * num_cols, num_rows * num_cols - 1]
for idx in corner_indices:
    plt.text(matrix[idx, 1], matrix[idx, 2], str(int(matrix[idx, 0])), fontsize=12, ha='right')

# Set labels and title
plt.xlabel('X coordinate (mm)')
plt.ylabel('Y coordinate (mm)')
plt.title('2D Scatter Plot of Matrix Points')

# Show the plot
plt.show()
