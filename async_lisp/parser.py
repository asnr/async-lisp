from dataclasses import dataclass

from lexer import LeftParens, RightParens, String, Symbol, Token

# Grammar:
#
#   program  ::= list | list program
#   list     ::= "(" ")" | "(" elements ")"
#   elements ::= element | element elements
#   element  ::= list | SYMBOL | STRING


@dataclass
class Program:
    lists: list["List"]


@dataclass
class List:
    elements: list["Element"]


Element = List | Symbol | String


def parse(token_list: list[Token]) -> Program:
    return _parse_program(TokenReader(token_list))


def _parse_program(tokens: "TokenReader") -> Program:
    lists = []
    while tokens.peek_next():
        lists.append(_parse_list(tokens))

    return Program(lists)


def _parse_list(tokens: "TokenReader") -> List:
    open_token = tokens.get_next()
    if not isinstance(open_token, LeftParens):
        raise Exception(f"Expected '(' but got token {open_token}")

    next_token = tokens.peek_next()
    match next_token:
        case None:
            raise Exception("Dangling left parens")
        case RightParens():  # maybe can drop?
            tokens.get_next()  # consume token
            return List([])
        case _:
            elements = _parse_elements(tokens)
            close_token = tokens.get_next()
            if not isinstance(close_token, RightParens):
                raise Exception(f"Expected ')' but got token {close_token}")
            return List(elements)


def _parse_elements(tokens: "TokenReader") -> list[Element]:
    elements = []
    while curr_token := tokens.peek_next():
        match curr_token:
            case LeftParens():
                elements.append(_parse_list(tokens))
            case Symbol() | String():
                tokens.get_next()  # consume token
                elements.append(curr_token)
            case _:
                break

    return elements


class TokenReader:
    def __init__(self, tokens: list[Token]):
        self._next_idx = 0
        self._tokens = tokens

    def get_next(self):
        next_token = self.peek_next()
        self._next_idx += 1
        return next_token

    def peek_next(self):
        if self._next_idx >= len(self._tokens):
            return None
        return self._tokens[self._next_idx]
