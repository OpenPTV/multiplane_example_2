# Read the original file
with open('plane_3.txt', 'r') as file:
    lines = file.readlines()

# Modify the last column for each row
modified_lines = []
for line in lines:
    columns = line.split()
    columns[-1] = '-200.0'
    modified_lines.append('    '.join(columns))

# Write the modified data to a new file
with open('modified_plane_3.txt', 'w') as file:
    file.write('\n'.join(modified_lines))