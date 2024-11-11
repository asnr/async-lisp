from lexer import Symbol


# Values are either str or Function. (I can't be bothered getting type checking
# to work.)
class Environment:
    def __init__(self, enclosing: "Environment" = None):
        self._values = {}
        self._enclosing = enclosing

    def define(self, symbol: Symbol, value):
        self._values[symbol.name] = value

    def get(self, symbol: Symbol):
        value = self._values.get(symbol.name)

        if value is None and self._enclosing is not None:
            value = self._enclosing.get(symbol)

        if value is None:
            raise Exception(f"Environment does not contain {symbol}")

        return value
