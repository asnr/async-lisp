import http.client
from urllib.parse import urlparse


def fetch(raw_url: str):
    url = urlparse(raw_url)
    conn = http.client.HTTPConnection(url.netloc)
    conn.request("GET", url.path)
    response = conn.getresponse()
    print(response.status, response.reason, response.read().decode("utf-8"))
