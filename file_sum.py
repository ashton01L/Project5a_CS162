# Author: Ashton Lee
# Github User: ashton01L
# Date: 10/30/2024
# Description: Write a function named file_sum that takes as a parameter the name of a text file that contains a list
# of numbers, one to a line.
def file_sum(filename):
    """
    Opens and reads file, checks to ensure data is numeric and sums numeric data. Raises error if non-numeric.
    Writes sum of numeric data to file named sum.txt

    :param: filename
    :return: Writes to file
    """
    try:
        total = 0.0
        with open(filename, 'r') as f:
            for line in f:
                line = line.strip()
                if line:  # Check if the line is not empty
                    try:
                        total += float(line)
                    except ValueError:
                        raise ValueError("The file contains non-numeric data.")

        with open('sum.txt', 'w') as out_file:
            out_file.write(f"{total}")

    except FileNotFoundError:
        raise FileNotFoundError(f"The file '{filename}' was not found.")


# file_sum('numbers.txt')
