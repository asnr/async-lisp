import unittest
import io
from contextlib import redirect_stdout

from interpreter import interpret


class TestInterpreter(unittest.TestCase):
    def test_print(self):
        with redirect_stdout(io.StringIO()) as output:
            interpret('(print "hello world")')
        program_output = output.getvalue()
        self.assertEqual("hello world\n", program_output)
