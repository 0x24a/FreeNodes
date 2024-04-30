import requests
import base64
def make_function(url):
    def fetch():
        response = requests.get(url).text
        response = base64.b64decode(response).decode("utf-8")
        return response.split("\n")
    return fetch