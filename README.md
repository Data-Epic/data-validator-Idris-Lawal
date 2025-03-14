# Data Validation Package
This is a python package that provides a simple data validation module that validates given fields of inputs ranging from email address, phone number, date, and url. It checks the validity of the given input in alignment to the corresponding standard. 

## Functions:
1. **Email Validator**: A feature that verifies that a given input comforms with a standard email format, e.g, "olatomiwal679@gmail.com"
2. **Phone Number Validator**: A feature that verifies that a given input comforms with the standard phone number format, e.g, "+2348162057433"
3. **Date Validator**: A feature that verifies that a given input comforms with the standard Date format (MM-DD-YYYY), e.g, "14-03-2025"
4. **URL Validator**: A feature that verifies that a given input comforms with the standard url format with and optional "https://", e.g, "https://discord.com"

## Applied Python Concepts:
* OOP - Object Oriented Programming
* Testing - Unit Testing with Pytest
* Regular Expression (RegEx)
* Python Packages and Modules

## Use Case
```python
from DataValidator.Validator import DataValidator

# Initiate validator
validator = DataValidator()

# Apply functions
validator.validate_email("olatomiwal679@gmail.com")
validator.validate_phone_number("+2348162057433")
validator.validate_date("14-03-2025")
validator.validate_url("https://discord.com")
```
## Available on Pypi

