import requests
from errors import *
import time
import random
import base64
import json

class SelfDiscord(object):
    def __init__(self, token):
        self.token = token
        os, browser, useragent, browserver, osvers = self.getInfo()
        self.prop = self.GetProps(os, browser, useragent, browserver, osvers)
        self.ua = useragent
        self.s = requests.Session()
        self.s.headers.update({'authorization': self.token, "user-agent": self.ua, "x-super-properties": self.prop})
        #Test Token
        result = self.SendRequest("GET", "/v7/users/@me").json()
        self.id = result["id"]
        self.username = result["username"]
        self.avatar = result["avatar"]
        self.discriminator = result["discriminator"]
        self.public_flags = result["public_flags"]
        self.flags = result["flags"]
        self.email = result["email"]
        self.verified = result["verified"]
        self.locale = result["locale"]
        self.nsfw_allowed = result["nsfw_allowed"]
        self.mfa_enabled = result["mfa_enabled"]
        self.phone = result["phone"]
    
    def getInfo(self):
        id = random.randint(1, 7)
        if id == 1:
            return ("Windows", "Chrome", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36", "69.0.3497.100", "10")
        elif id == 2:
            return ("Windows", "Chrome", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763", "18.17763", "10")
        elif id == 3:
            return ("Windows", "Edge", "Mozilla/5.0 (Windows NT 5.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36", "60.0.3112.90", "XP")
        elif id == 4:
            return ("Windows", "Chrome", "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36", "60.0.3112.113", "8.1")
        elif id == 5:
            return ("Windows", "Internet Explorer", "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729; rv:11.0) like Gecko", "11.0", "7")
        elif id == 6:
            return ("Windows", "Firefox", "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0", "54.0", "7")
        elif id == 7:
            return ("Windows", "Firefox", "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0", "66.0", "10")

    def GetProps(self, os, browser, useragent, browser_version, os_version):
        props = {
            "os": os,
            "browser": browser,
            "device": "",
            "browser_user_agent": useragent,
            "browser_version": browser_version,
            "os_version": os_version,
            "referrer": "",
            "referring_domain": "",
            "referrer_current": "",
            "referring_domain_current": "",
            "release_channel": "stable",
            "client_build_number": 70781,
            "client_event_source": None
        }
        return base64.b64encode(json.dumps(props, separators=",:").encode()).decode()

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
    
    def GetUserInfo(self, proxies=None):
        result = self.SendRequest("GET", "/v7/users/@me", proxies).json()
        self.id = result["id"]
        self.username = result["username"]
        self.avatar = result["avatar"]
        self.discriminator = result["discriminator"]
        self.public_flags = result["public_flags"]
        self.flags = result["flags"]
        self.email = result["email"]
        self.verified = result["verified"]
        self.locale = result["locale"]
        self.nsfw_allowed = result["nsfw_allowed"]
        self.mfa_enabled = result["mfa_enabled"]
        self.phone = result["phone"]
        return result
    
    def GetServers(self, proxies=None):
        result = self.SendRequest("GET", "/users/@me/guilds", proxies)
        return result.json()
    
    def GetDMs(self, proxies=None):
        result = self.SendRequest("GET", "/users/@me/channels", proxies)
        return result.json()
    
    def GetFriends(self, proxies=None):
        result = self.SendRequest("GET", "/users/@me/relationships", proxies)
        return result.json()

    def SendMessage(self, content, channelid, proxies=None):
        data = {"content":content,"nonce":''.join([str(random.randint(1, 9)) for i in range(18)]),"tts":False}
        result = self.SendRequest("POST", f"/v8/channels/{channelid}/messages", proxies, data)
        return result.json()
    
    def SendTTSMessage(self, content, channelid, proxies=None):
        data = {"content":content,"nonce":''.join([str(random.randint(1, 9)) for i in range(18)]),"tts":True}
        result = self.SendRequest("POST", f"/v8/channels/{channelid}/messages", proxies, data)
        return result.json()

    def GetMessages(self, channelid, proxies=None):
        result = self.SendRequest("GET", f"/v8/channels/{channelid}/messages", proxies)
        return result.json()

    def DeleteChannel(self, channelid, proxies=None):
        result = self.SendRequest("DELETE", f"/v8/channels/{channelid}", proxies)
        return result.json()
    
    def AddFriend(self, userid, proxies=None):
        self.SendRequest("PUT", f"/v8/users/@me/relationships/{userid}", proxies, data={})
        return f"AddedFriend {userid}"

    def UnFriend(self, userid, proxies=None):
        self.SendRequest("DELETE", f"/v8/users/@me/relationships/{userid}", proxies)
        return f"UnFriended {userid}"

    def JoinServer(self, invite, proxies=None):
        result = self.SendRequest("POST", f"/v8/invites/{invite}", proxies)
        return result.json()
    
    def LeaveServer(self, serverid, proxies=None):
        self.SendRequest("DELETE", f"/v8/users/@me/guilds/{serverid}", proxies)
        return f"Left Server {serverid}"

    def CreateServer(self, name, proxies=None):
        data = {"name":name,"icon":None,"channels":[],"system_channel_id":None,"guild_template_code":"2TffvPucqHkN"}
        result = self.SendRequest("POST", "/v8/guilds", proxies, data)
        return result.json()
    
    def DeleteServer(self, serverid, proxies=None):
        data = {}
        self.SendRequest("POST", f"/v8/guilds/{serverid}/delete", proxies, data)
        return f"Deleted Server {serverid}"

    

            


discord = SelfDiscord("Nzg1NTkzNDEzODM0ODk5NDg2.X-7PvQ.Pi7zamBUZuoFSZAOcONRTJm26XU")
print(discord.DeleteServer("795550386508791829"))