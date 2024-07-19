import requests
import json
import django


class MainRequestHandler():
    def GetRequest(order, sort, min, max, tagged, site)
        try:
            requests.get(f"http://api.stackexchange/2.3/questions?{order}{sort}{min}{max}{tagged}{site}")
        except requests.exceptions.RequestException as e:
            print(e)