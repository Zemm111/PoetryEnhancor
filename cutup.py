
# Define the input and output file names
input_file_name = "input.txt"
output_file_name = "output.txt"

# Read lines from the input file
with open(input_file_name, "r") as input_file:
    lines = input_file.readlines()

# Reorder the lines
lines.sort()  # You can change this to a custom sorting logic if needed

# Write the reordered lines to the output file
with open(output_file_name, "w") as output_file:
    for i, line in enumerate(lines, start=1):
        # Append a digit in the format (1), (2), etc.
        formatted_line = f"({i}) {line.strip()}\n"
        blank_line = f"\n"
        output_file.write(formatted_line)
        output_file.write(blank_line)

print(f"Lines have been reordered and written to '{output_file_name}'.")