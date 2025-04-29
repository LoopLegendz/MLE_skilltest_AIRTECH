# AIR TECH MLE Technical Test

This repository contains my solutions for the AIR TECH Machine Learning Engineer technical test.

## Project Structure

```
mle_skilltest_airtech/
├── src/
│   ├── coding_challenge_1.py
│   ├── coding_challenge_2.py
│   ├── sql.py
│   └── __init.py__
└── tests/
    ├── test_coding_challenge_1.py
    ├── test_coding_challenge_2.py
    └── __init__.py
```

## Setup Instructions

1. Clone the repository:
```bash
git clone <your-repository-url>
cd mle_skilltest_airtech
```

2. Create a virtual environment (recommended):
```bash
python3 -m venv venv
source venv/bin/activate  # On macOS/Linux
```

3. Install dependencies:
```bash
python3 -m pip install -r requirements.txt
```

## Running the Code

### Coding Challenges
Run individual challenges:
```bash
python3 src/coding_challenge_1.py
python3 src/coding_challenge_2.py
```

### SQL Exercises
Run SQL exercises:
```bash
python3 src/sql.py
```

## Running Tests
Make sure your virtual environment is activated, then run:
```bash
# Run all tests
python3 -m pytest tests/

# Run tests with verbose output
python3 -m pytest -v tests/

# Run specific test file
python3 -m pytest tests/test_coding_challenge_1.py
python3 -m pytest tests/test_coding_challenge_2.py
```