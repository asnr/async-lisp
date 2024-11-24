import http.client
from urllib.parse import urlparse

from environment import Environment, PythonFunction
from lexer import Symbol


def base_environment():
    env = Environment()
    _define_builtin_functions(env)
    return env


def _define_builtin_functions(env: Environment):
    env.define(Symbol("print"), PythonFunction(print))
    env.define(Symbol("fetch"), PythonFunction(fetch))


def fetch(raw_url: str):
    url = urlparse(raw_url)
    conn = http.client.HTTPConnection(url.netloc)
    conn.request("GET", url.path)
    response = conn.getresponse()
    print(response.status, response.reason, response.read().decode("utf-8"))
