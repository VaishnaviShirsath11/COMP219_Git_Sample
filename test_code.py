
# Define the filename
file_name = "sample_data1.txt"

# Open the file for reading
with open(file_name, 'r') as file:
    # Read and print the file content line by line
    for line in file:
        print(line.strip())


