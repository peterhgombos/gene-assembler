import unittest
from ..scanner import scanner


class TestScanner(unittest.TestCase):

    def setUp(self):
        with open('gene/test/test.gas', 'r') as f:
            self.assembly = [line for line in f]
        with open('gene/test/test.gas.tokens', 'r') as f:
            # cutting the last character to get rid of \n
            self.correct = [line[:-1] for line in f]

    def test_scanner(self):
        tokens = map(scanner.scan, self.assembly)

        for token, correct_token in zip(tokens, self.correct):
            self.assertEqual(str(token), str(correct_token))
