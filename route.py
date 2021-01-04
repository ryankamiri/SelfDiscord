import requests
from errors import *
import time
import random

class Route(object):
    def __init__(self, token, useragent=None, xsuperprops=None):
        self.token = token
        self.useragent = useragent
        self.xsuperprops = xsuperprops
        self.s = requests.Session()
        self.headers = {'authorization': self.token}
        if self.useragent:
            self.headers["user-agent"] = self.useragent
        if self.xsuperprops:
            self.headers["x-super-properties"] = self.xsuperprops
        self.s.headers.update(self.headers)

    def SendRequest(self, method, endpoint, proxies=None, data=None):
        response = None
        proxy = None
        if proxies:
            proxy = {"https": "https://" + proxies[random.randint(0, len(proxies) - 1)]}
        if method == "GET":
            if proxy:
                response = self.s.get("https://discord.com/api" + endpoint, proxies=proxy, json=data)
            else:
                response = self.s.get("https://discord.com/api" + endpoint, json=data)
        elif method == "POST":
            if proxy:
                response = self.s.post("https://discord.com/api" + endpoint, proxies=proxy, json=data)
            else:
                response = self.s.post("https://discord.com/api" + endpoint, json=data)
        elif method == "PUT":
            if proxy:
                response = self.s.put("https://discord.com/api" + endpoint, proxies=proxy, json=data)
            else:
                response = self.s.put("https://discord.com/api" + endpoint, json=data)
        elif method == "PATCH":
            if proxy:
                response = self.s.patch("https://discord.com/api" + endpoint, proxies=proxy, json=data)
            else:
                response = self.s.patch("https://discord.com/api" + endpoint, json=data)
        elif method == "DELETE":
            if proxy:
                response = self.s.delete("https://discord.com/api" + endpoint, proxies=proxy, json=data)
            else:
                response = self.s.delete("https://discord.com/api" + endpoint, json=data)
        if response.status_code == 401:
            raise Unauthorized
        elif response.status_code == 403:
            raise Forbidden
        elif response.status_code == 400:
            raise BadRequest
        elif response.status_code == 404:
            raise NotFound
        elif response.status_code == 429:
            if proxies:
                return self.SendRequest(method, endpoint, proxies)
            else:
                time.sleep(response.headers["retry-after"])
                return self.SendRequest(method, endpoint)
        else:
            return response