import pytest


# Test 1: test to make sure name and surname inputs/arguments are strings not numbers. 
#STRING
def test_name_input():
    with pytest.raises(nameType) as error:
        convert_to_letter_grade(1)
    assert str(error.value) == "Name and surname inputs must be written in letters."
#LIST
    with pytest.raises(nameType) as error:
        convert_to_letter_grade([0, 1, 2])
    assert str(error.value) == "Name and surname inputs must be written in letters."
#NONE
    with pytest.raises(nameType) as error:
        convert_to_letter_grade(None)
    assert str(error.value) == "Name and surname inputs must be written in letters."
