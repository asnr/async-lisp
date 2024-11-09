from lexer import String, Symbol
from parser import Element, List, Program


def evaluate(program: Program):
    env = _builtin_functions()
    for currList in program.lists:
        _evaluate_list(env, currList)


def _builtin_functions():
    return {"print": print}


def _evaluate_list(env: dict, aList: List):
    if not aList.elements:
        return  # list is empty, do nothing

    func_symbol = aList.elements[0]
    if not isinstance(func_symbol, Symbol):
        raise Exception(f"Function call should start with symbol, got {func_symbol}")
    if func_symbol.name == "define":
        # handle this specifically, because we don't want the initial symbol resolved
        _evaluate_define(env, aList)
        return

    argument_values = []
    for argument in aList.elements[1:]:
        value = _evaluate_element(env, argument)
        argument_values.append(value)

    func = env[func_symbol.name]
    return func(*argument_values)


def _evaluate_element(env: dict, element: Element):
    match element:
        case String():
            return element.value
        case Symbol():
            return env[element.name]


def _evaluate_define(env: dict, aList: List):
    assert len(aList.elements) == 3
    assert isinstance(aList.elements[1], Symbol)

    [_, variable, value_expression] = aList.elements
    value = _evaluate_element(env, value_expression)

    env[variable.name] = value
