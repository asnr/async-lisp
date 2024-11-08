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
