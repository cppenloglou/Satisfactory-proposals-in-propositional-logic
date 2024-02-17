# Satisfactory-proposals-in-propositional-logic

This project explores the use of propositional logic to generate and validate satisfactory proposals. 

## Files

- **M200-1200_N10_K6_26_Solved:** This file contains a solved instance of a propositional logic problem.
- **M200-1200_N10_K6_26_TEST1, M200-1200_N10_K6_26_TEST2, ..., M200-1200_N10_K6_26_TEST5:** These files contain test instances of the propositional logic problem.
- **Tests:** This directory contains scripts for testing the project's code.
- **Tools:** This directory contains tools for generating and validating propositional logic formulas.
  - **countDepth.py, countHill.py, countTimeDepth.py, countTimeHill.py:** These scripts count the depth, hill climbing distance, time to find a solution using depth-first search, and time to find a solution using hill climbing, respectively.
  - **generator.py:** This script generates propositional logic formulas.
  - **Tools_bat:** This directory contains batch files for running the tools.
    - **generate.bat:** This batch file generates propositional logic formulas.
    - **run_tests.bat:** This batch file runs the tests.
    - **validate_test.bat:** This batch file validates the test instances.
- **bcsp.c, bcsp.exe:** These files contain the implementation of a Boolean constraint solver.
- **bcsp_generate.c, bcsp_generate.exe:** These files contain a tool for generating Boolean constraint satisfaction problems.
- **bcsp_validate.c, bcsp_validate.exe:** These files contain a tool for validating Boolean constraint satisfaction problems.
- **LICENSE:** This file contains the project's license.
- **Makefile:** This file is used to build the project.
- **README.md:** This file (the one you are reading now) contains information about the project.

## Usage

To run the project, you will need to have a C compiler and Python installed. You can then build the project by running the following command in the project's root directory:

```bash
make
```
Once the project is built, you can run the tests by running the following command:
```bash
./run_tests.bat
```
You can generate new propositional logic formulas by running the following command:
```bash
./generate.bat
```

