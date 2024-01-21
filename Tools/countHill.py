import os
import re
import csv

def count_files_with_prefix_and_extension(prefix, start, end, extension, directory):
    counts_per_i = {}

    for i in range(start, end + 1):
        filename_pattern = re.compile(f"{prefix}{i}_M{160+i*40}.*{extension}")
        matching_files = [file for file in os.listdir(directory) if filename_pattern.match(file)]
        counts_per_i[i] = len(matching_files)

    return counts_per_i

def write_results_to_csv(results, output_csv, directory):
    current_directory = os.getcwd() + "\\" + directory
    csv_file_path = os.path.join(current_directory, output_csv)
    with open(csv_file_path, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(["Test", "Count"])

        for i, count in results.items():
            csv_writer.writerow([f"{i}", count])

def main():
    prefix = "solution_hill_test"
    start_number = 1
    end_number = 26
    file_extension = ".txt"
    directory = "../M200-1200_N10_K6_26_Solved"
    output_csv = "hill_results.csv"

    counts_per_i = count_files_with_prefix_and_extension(prefix, start_number, end_number, file_extension, directory)
    
    write_results_to_csv(counts_per_i, output_csv, directory)

if __name__ == "__main__":
    main()
