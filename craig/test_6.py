from age_checker import *
import pytest

# def test_user_enter_DOB():
#     result = age_checker("07/12/30")
#     assert result == 18

def test_access_denied():
    result = age_checker("16/12/30")
    assert result == "Access denied: You are 10, you must be 16"

def test_access_granted():
    result = result = age_checker("07/12/30")
    assert result == "Access granted"

def test_incorrect_format():
    with pytest.raises(ValueError):
        age_checker("2007/12/20")
    
