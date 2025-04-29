# BNP Paribas MLE Technical Test

This repository contains my solutions for the BNP Paribas Machine Learning Engineer technical test.

## Project Structure

bnp_paribas_test/
├── src/ # Main source code
│ ├── coding_challenge_1.py
│ └── coding_challenge_2.py
  └── sql.py # SQL exercises
├── tests/ # Unit tests
│ ├── test_coding_challenge_1.py
  └── test_coding_challenge_2.py
  

## Setup Instructions

## Setup Instructions

1. Clone the repository:
```bash
git clone <your-repository-url>
cd bnp_paribas_test
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

## Running Tests
Make sure your virtual environment is activated, then run:
```bash
python3 -m pytest tests/
```
```

Try these commands in order:
```bash
# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
python3 -m pip install -r requirements.txt

# Run tests
python3 -m pytest tests/
```