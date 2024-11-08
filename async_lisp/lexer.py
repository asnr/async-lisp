from enum import Enum
from dataclasses import dataclass


class LeftParens: ...


class RightParens: ...


@dataclass
class Symbol:
    name: str


@dataclass
class String:
    value: str


Token = LeftParens | RightParens | Symbol | String


def lex(code: str) -> list[Token]:
    tokens = []
    idx = 0
    while idx < len(code):
        char = code[idx]
        if char == "(":
            tokens.append(LeftParens())
        elif char == ")":
            tokens.append(RightParens())
        elif char == '"':
            string_end_idx = idx + 1
            while string_end_idx < len(code) and code[string_end_idx] != '"':
                string_end_idx += 1
            if code[string_end_idx] != '"':
                raise Exception("string is not closed")
            string_value = code[idx + 1 : string_end_idx]
            tokens.append(String(string_value))
            idx = string_end_idx
        elif char.isspace():
            ...
        else:
            symbol_end_idx = idx + 1
            while (
                symbol_end_idx < len(code)
                and not code[symbol_end_idx] in ["(", ")", '"']
                and not code[symbol_end_idx].isspace()
            ):
                symbol_end_idx += 1
            symbol_name = code[idx:symbol_end_idx]
            tokens.append(Symbol(symbol_name))
            idx = symbol_end_idx - 1

        idx += 1
    return tokens
