import unittest
from unittest.mock import patch
import main  # assuming your function is in a file named main.py

class TestReceiveChains(unittest.TestCase):

    @patch('builtins.input', side_effect=['chain1', 'chain2', 'chain3'])
    def test_receive_chains_normal(self, mock_input):
        chains = main.receive_Chains(3)
        self.assertEqual(chains, ['chain1', 'chain2', 'chain3'])

    @patch('builtins.input', side_effect=['chain1'*21])
    def test_receive_chains_too_long(self, mock_input):
        with self.assertRaises(SystemExit):
            main.receive_Chains(1)

    @patch('builtins.input', side_effect=['chain1', 'chain2', ''])
    def test_receive_chains_less_than_expected(self, mock_input):
        with self.assertRaises(SystemExit):
            main.receive_Chains(3)

if __name__ == '__main__':
    unittest.main()