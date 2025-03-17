import pytest
import pytest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Validators.Validator import DataValidator

@pytest.fixture
def validator():
    validator = DataValidator()
    return validator

def test_validate_email(validator):
    assert validator.validate_email("olatomiwal679@gmail.com") is True
    assert validator.validate_email("olatomiwal679@gmail.com", verbose=True) is True
    assert validator.validate_email("olatomiwagmail.com") is False
    assert validator.validate_email("olatomiwagmail.com", verbose=True) is False

def test_validate_phone_number(validator):
    assert validator.validate_phone_number("+2348162057433") is True
    assert validator.validate_phone_number("+2348162057433", verbose=True) is True
    assert validator.validate_phone_number("30289dsd018") is False
    assert validator.validate_phone_number("30289dsd018", verbose=True) is False

def test_validate_date(validator):
    assert validator.validate_date("12-03-2025") is True
    assert validator.validate_date("12-03-2025", verbose=True) is True
    assert validator.validate_date("13-20-2020") is False
    assert validator.validate_date("13-20-2020", verbose=True) is False

def test_validate_url(validator):
    assert validator.validate_url("https://discord.com") is True
    assert validator.validate_url("https://discord.com", verbose=True) is True
    assert validator.validate_url("discord.com", verbose=True) is True
    assert validator.validate_url("@discord-com") is False
    assert validator.validate_url("@discord-com", verbose=True) is False