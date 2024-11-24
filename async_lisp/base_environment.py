import http.client
from urllib.parse import urlparse

from environment import Environment, Function, PythonFunction
from lexer import Symbol


def base_environment():
    env = Environment()
    _define_builtin_functions(env)
    return env


def _define_builtin_functions(env: Environment):
    env.define(Symbol("print"), PythonFunction(print))
    env.define(Symbol("fetch"), PythonFunction(fetch))


def fetch(raw_url: str, callback: Function):
    url = urlparse(raw_url)
    conn = http.client.HTTPConnection(url.netloc)
    conn.request("GET", url.path)
    response = conn.getresponse()
    if response.status != 200:
        raise Exception(f"HTTP call returned with bad status {response.status}")

    # Create a new environment. Alternatively, this could pass on the
    # environment that `fetch` was called in.
    env = base_environment()
    response_body = response.read().decode("utf-8")
    callback.call(env, response_body)
