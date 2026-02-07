Module 3: Interactive Calculator Command-Line Application

A robust Python-based calculator built using a Read-Eval-Print Loop (REPL), comprehensive unit testing, and Continuous Integration (CI). This project demonstrates professional software development practices, including the DRY principle and enforcement of 100% test coverage.

FEATURES

REPL Interface
Continuous Read-Eval-Print Loop for seamless user interaction.

Arithmetic Operations
Supports Addition, Subtraction, Multiplication, and Division.

Input Validation
Ensures users follow the correct command format and handles non-numeric input gracefully.

Error Handling
Custom handling for division by zero and unexpected application errors.

100% Test Coverage
All application code is fully tested using pytest and pytest-cov.

Automated CI
GitHub Actions pipeline enforces 100% test coverage on every push.

SETUP INSTRUCTIONS

Clone the Repository

git clone https://github.com/kushyarwar/calculator_assignment.git

cd calculator_assignment

Create and Activate a Virtual Environment

Windows (PowerShell):

python -m venv venv
.\venv\Scripts\activate

Mac / Linux:

python3 -m venv venv
source venv/bin/activate

Install Dependencies

pip install -r requirements.txt

USAGE

Start the calculator application by running:

python -m app.main

SUPPORTED COMMANDS

Use the following format inside the application:

<operation> <number1> <number2>

Examples:

add 10 5
Result: 15.0

sub 20 4
Result: 16.0

mul 3 3
Result: 9.0

div 10 2
Result: 5.0

Type exit to close the program.

TESTING AND QUALITY ASSURANCE

Run the test suite:

pytest

Check test coverage and ensure 100% coverage:

pytest --cov=app --cov-report term-missing

CONTINUOUS INTEGRATION

This repository uses GitHub Actions. On every push, the CI pipeline:

Sets up a Python environment

Installs all project dependencies

Runs all tests

Fails the build if test coverage is below 100%

LICENSE

This project is intended for educational purposes.