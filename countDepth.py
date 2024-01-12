import os
import re

def count_files_with_prefix_and_extension(prefix, start, end, extension):
    counts_per_i = {}

    for i in range(start, end + 1):
        filename_pattern = re.compile(f"{prefix}{i}_M{160+i*40}.*{extension}")
        matching_files = [file for file in os.listdir("M200-1200_N10_K6_26TEST") if filename_pattern.match(file)]
        counts_per_i[i] = len(matching_files)

    return counts_per_i

def write_results_to_file(results, output_file):
    with open(output_file, 'w') as file:
        for i, count in results.items():
            file.write(f"{i}: {count}\n")

def main():
    prefix = "solution_depth_test"
    start_number = 1
    end_number = 26
    file_extension = ".txt"
    output_file = "depth_results.txt"

    counts_per_i = count_files_with_prefix_and_extension(prefix, start_number, end_number, file_extension)
    
    write_results_to_file(counts_per_i, output_file)

if __name__ == "__main__":
    main()
