from unittest import mock
from main import receive_numberOfStates

def test_receive_numberOfStates_valid_input():
    with mock.patch('builtins.input', return_value="5"):
        assert receive_numberOfStates() == 5

def test_receive_numberOfStates_invalid_input():
    with mock.patch('builtins.input', side_effect=["invalid", "5"]):
        assert receive_numberOfStates() == 5

def test_receive_numberOfStates_out_of_range_input():
    with mock.patch('builtins.input', side_effect=["0", "11", "5"]):
        assert receive_numberOfStates() == 5