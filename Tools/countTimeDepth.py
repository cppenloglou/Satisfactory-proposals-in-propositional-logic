import csv
import os

# Get the current working directory
current_directory = os.getcwd() + "\\..\\M200-1200_N10_K6_26_TEST1"

# Number of tests and test iterations
num_tests = 26
test_iterations = 10
m_start = 200
m_step = 40

# CSV file path to store the results in the current directory
csv_file_path = os.path.join(current_directory, "depthTime.csv")

# Open the CSV file for writing
with open(csv_file_path, mode='w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)

    # Write header to CSV file
    csv_writer.writerow(["Test", "M", "Iteration", "Time"])

    # Iterate through each test
    for test_num in range(1, num_tests + 1):
        # Calculate M for the current test
        m_value = m_start + (test_num - 1) * m_step

        for iteration_num in range(1, test_iterations + 1):
            # Generate the filename
            filename = f"solution_depth_test{test_num}_M{m_value}_N10_K6_{iteration_num}.txt"
            file_path = os.path.join(current_directory, filename)

            # Check if the file exists
            if not os.path.exists(file_path):
                print(f"File not found: {file_path}. Skipping...")
                continue

            # Read the last number from the file
            try:
                with open(file_path, 'r') as file:
                    last_number = float(file.readlines()[-1].split()[-1])
            except Exception as e:
                print(f"Error reading file {file_path}: {e}. Skipping...")
                continue

            # Write the data to CSV file
            csv_writer.writerow([f"{test_num}", m_value, f"iteration{iteration_num}", last_number])

print(f"Data has been successfully written to {csv_file_path}")
