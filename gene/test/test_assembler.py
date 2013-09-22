import unittest
from ..assembler import assemble


class TestAssembler(unittest.TestCase):

    def setUp(self):
        with open('gene/test/test.gas', 'r') as f:
            self.assembly = [line for line in f]
        with open('gene/test/test.gas.assembled', 'r') as f:
            # cutting the last character to get rid of \n
            self.correct = f.next()[:-1]

    def test_assembler(self):
        assembled = assemble(self.assembly)
        self.assertEqual(str(assembled), self.correct)
