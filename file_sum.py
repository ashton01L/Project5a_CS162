def file_sum(filename):
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


file_sum('numbers.txt')