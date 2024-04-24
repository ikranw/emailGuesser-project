import pytest
from emailGuesser.py import get_user_input

# Test 1: test to make sure name and surname inputs/arguments are strings not numbers. 
import pytest
from emailGuesser import get_user_input

# Test 1: test to make sure name and surname inputs/arguments are strings not numbers.
def test_name_input_string():
    with pytest.raises(ValueError) as error:
        get_user_input()
    assert str(error.value) == "Name and surname inputs must contain only letters."

