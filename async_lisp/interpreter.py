import argparse
import sys

from lexer import lex
from parser import parse
from evaluator import evaluate


def main():
    parser = argparse.ArgumentParser(prog="async-lisp")
    parser.add_argument("filename")
    args = parser.parse_args()

    with open(args.filename) as file:
        interpret(file.read())


def interpret(code: str):
    evaluate(parse(lex(code)))


if __name__ == "__main__":
    main()
