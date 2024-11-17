import abc

from environment import Environment
from lexer import String, Symbol
from parser import Element, List, Program


def evaluate(program: Program):
    env = Environment()
    _define_builtin_functions(env)
    for currList in program.lists:
        _evaluate_list(env, currList)


def _define_builtin_functions(env: Environment):
    env.define(Symbol("print"), PythonFunction(print))


def _evaluate_list(env: Environment, aList: List):
    if not aList.elements:
        return  # list is empty, do nothing

    func_symbol = aList.elements[0]
    if not isinstance(func_symbol, Symbol):
        raise Exception(f"Function call should start with symbol, got {func_symbol}")
    if func_symbol.name == "define":
        # handle this specifically, because we don't want the assignee resolved
        _evaluate_define(env, aList)
        return

    argument_values = []
    for argument in aList.elements[1:]:
        value = _evaluate_element(env, argument)
        argument_values.append(value)

    func = env.get(func_symbol)
    return func.call(env, *argument_values)


def _evaluate_element(env: Environment, element: Element):
    match element:
        case List():
            return _evaluate_list(env, element)
        case String():
            return element.value
        case Symbol():
            return env.get(element)


def _evaluate_define(env: Environment, aList: List):
    assert len(aList.elements) == 3

    lhs = aList.elements[1]
    match lhs:
        case Symbol():
            [_, variable, value_expression] = aList.elements
            value = _evaluate_element(env, value_expression)
            env.define(variable, value)
        case List():
            func_symbol = lhs.elements[0]
            func_parameters = lhs.elements[1:]
            func_body = aList.elements[2]
            env.define(func_symbol, LispFunction(func_parameters, func_body))


class Function(abc.ABC):
    @abc.abstractmethod
    def call(self, env: Environment, *args): ...


class LispFunction(Function):
    def __init__(self, parameters: list[Symbol], body: List):
        self._parameters = parameters
        self._body = body

    def call(self, env: Environment, *args):
        assert len(args) == len(self._parameters)

        function_env = Environment(env)
        for parameter, arg in zip(self._parameters, args):
            function_env.define(parameter, arg)

        return _evaluate_element(function_env, self._body)


class PythonFunction(Function):
    def __init__(self, func):
        self._func = func

    def call(self, env: Environment, *args):
        return self._func(*args)
