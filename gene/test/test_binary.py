import unittest
from ..assembler import assemble, ascii_binary_to_real_binary


class TestAssembler(unittest.TestCase):

    def setUp(self):
        with open('gene/test/test.gas', 'r') as f:
            self.assembly = [line for line in f]
        with open('gene/test/test.gas.binary', 'rb') as f:
            # cutting the last character to get rid of \n
            self.correct = f.next()

    def test_assembler(self):
        assembled = assemble(self.assembly)
        ascii_binary = ''.join(map(lambda x: x.toBinary(), assembled))
        binary = ascii_binary_to_real_binary(ascii_binary)
        self.assertEqual(binary, self.correct)
