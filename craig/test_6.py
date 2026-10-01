from age_checker import *

def test_user_enter_DOB():
    result = age_checker("2007/12/30")
    assert result == 18

def test_access_denied():
    result = age_checker("2016/12/30")
    assert result == "Access denied: You are 10, you must be 16"

def test_access_granted():
    result = result = age_checker("2007/12/30")
    assert result == "Access granted"

#test_incorrect_format