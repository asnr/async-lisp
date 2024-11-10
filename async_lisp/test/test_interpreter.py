import glob
import unittest
import io
import os
import re
from contextlib import redirect_stdout

from interpreter import interpret


# Dynamically generate tests by traversing the Async Lisp programs in the
# ./programs subdirectory. Each file in that directory contains its own expected
# output in lines starting with the comment ";; ".
#
# Collect these files, extract the expected output and then assert the match the
# actual output from running the programs.
class TestInterpreter(unittest.TestCase):

    def test_programs(self):
        root_dir = os.path.dirname(os.path.realpath(__file__))
        for filename in glob.glob("./programs/*.al", root_dir=root_dir):
            with self.subTest(filename=filename):
                with open(os.path.join(root_dir, filename)) as test_file:
                    code = test_file.read()
                    expected_output = "\n".join(
                        re.findall(r"^;; (.*)", code, flags=re.MULTILINE)
                    )
                    # Currently, async-lisp has only one print function which
                    # always finishes with a newline. Match the last newline by
                    # slapping on a newline to the expected output.
                    if expected_output:
                        expected_output += "\n"
                with redirect_stdout(io.StringIO()) as output:
                    interpret(code)
                self.assertEqual(expected_output, output.getvalue())
