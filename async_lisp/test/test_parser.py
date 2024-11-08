import unittest

from parser import parse, Program, List
from lexer import lex, Symbol, String


class TestParser(unittest.TestCase):
    def test_smallest_program(self):
        self.assertEqual(Program([List([])]), _parse_lex("()"))

    def test_lone_left_parens(self):
        with self.assertRaises(Exception):
            _parse_lex("(")

    def test_lone_right_parens(self):
        with self.assertRaises(Exception):
            _parse_lex("(")

    def test_lone_symbol(self):
        with self.assertRaises(Exception):
            _parse_lex("a")

    def test_dangling_open_quote(self):
        with self.assertRaises(Exception):
            _parse_lex('"')

    def test_list_with_single_element(self):
        self.assertEqual(Program([List([Symbol("a")])]), _parse_lex("(a)"))

    def test_list_with_two_elements(self):
        self.assertEqual(
            Program([List([Symbol("a"), Symbol("b")])]), _parse_lex("(a b)")
        )

    def test_list_with_string(self):
        self.assertEqual(Program([List([String("a")])]), _parse_lex('("a")'))

    def test_two_lists(self):
        self.assertEqual(Program([List([]), List([])]), _parse_lex("()()"))


def _parse_lex(code):
    return parse(lex(code))
