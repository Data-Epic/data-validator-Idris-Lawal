import pytest
from datavalidator.Validator import DataValidator

@pytest.fixture
def validator():
    validator = DataValidator()
    return validator

def test_validate_email(validator):
    assert validator.validate_email("olatomiwal679@gmail.com") is True
    assert validator.validate_email("olatomiwagmail.com") is False

def test_validate_phone_number(validator):
    assert validator.validate_phone_number("+2348162057433") is True
    assert validator.validate_phone_number("30289dsd018") is False

def test_validate_date(validator):
    assert validator.validate_date("12-03-2025") is True
    assert validator.validate_date("13-20-2020") is False

def test_validate_url(validator):
    assert validator.validate_url("https://discord.com/channels/1159077758962503762/1246459768357523527") is True
    assert validator.validate_url("@discord-com") is False