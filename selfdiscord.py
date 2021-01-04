from route import Route
import random
import base64

class SelfDiscord(object):
    def __init__(self, token, useragent=None, xsuperprops=None):
        self.token = token
        self.useragent = useragent
        self.xsuperprops = xsuperprops
        self.route = Route(token, useragent, xsuperprops)
        #Test Token
        result = self.route.SendRequest("GET", "/v8/users/@me").json()
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
    
    def GetUserInfo(self, proxies=None):
        result = self.route.SendRequest("GET", "/v8/users/@me", proxies).json()
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
        result = self.route.SendRequest("GET", "/users/@me/guilds", proxies)
        return result.json()
    
    def GetDMs(self, proxies=None):
        result = self.route.SendRequest("GET", "/users/@me/channels", proxies)
        return result.json()
    
    def GetFriends(self, proxies=None):
        result = self.route.SendRequest("GET", "/users/@me/relationships", proxies)
        return result.json()

    def SendMessage(self, content, channelid, proxies=None):
        data = {"content":content,"nonce":''.join([str(random.randint(1, 9)) for i in range(18)]),"tts":False}
        result = self.route.SendRequest("POST", f"/v8/channels/{channelid}/messages", proxies, data)
        return result.json()
    
    def SendTTSMessage(self, content, channelid, proxies=None):
        data = {"content":content,"nonce":''.join([str(random.randint(1, 9)) for i in range(18)]),"tts":True}
        result = self.route.SendRequest("POST", f"/v8/channels/{channelid}/messages", proxies, data)
        return result.json()

    def GetMessages(self, channelid, proxies=None):
        result = self.route.SendRequest("GET", f"/v8/channels/{channelid}/messages", proxies)
        return result.json()

    def CreateTextChannel(self, serverid, name, parentid=None, proxies=None):
        data = {"type":0,"name":name,"permission_overwrites":[]}
        if parentid:
            data["parent_id"] = parentid
        result = self.route.SendRequest("POST", f"/v8/guilds/{serverid}/channels", proxies, data)
        return result.json()
    
    def CreateVoiceChannel(self, serverid, name, parentid=None, proxies=None):
        data = {"type":2,"name":name,"permission_overwrites":[]}
        if parentid:
            data["parent_id"] = parentid
        result = self.route.SendRequest("POST", f"/v8/guilds/{serverid}/channels", proxies, data)
        return result.json()

    def DeleteChannel(self, channelid, proxies=None):
        result = self.route.SendRequest("DELETE", f"/v8/channels/{channelid}", proxies)
        return result.json()
    
    def AddFriend(self, userid, proxies=None):
        self.route.SendRequest("PUT", f"/v8/users/@me/relationships/{userid}", proxies, data={})
        return f"AddedFriend {userid}"

    def UnFriend(self, userid, proxies=None):
        self.route.SendRequest("DELETE", f"/v8/users/@me/relationships/{userid}", proxies)
        return f"UnFriended {userid}"

    def JoinServer(self, invite, proxies=None):
        result = self.route.SendRequest("POST", f"/v8/invites/{invite}", proxies)
        return result.json()
    
    def LeaveServer(self, serverid, proxies=None):
        self.route.SendRequest("DELETE", f"/v8/users/@me/guilds/{serverid}", proxies)
        return f"Left Server {serverid}"

    def CreateServer(self, name, proxies=None):
        data = {"name":name,"icon":None,"channels":[],"system_channel_id":None,"guild_template_code":"2TffvPucqHkN"}
        result = self.route.SendRequest("POST", "/v8/guilds", proxies, data)
        return result.json()
    
    def DeleteServer(self, serverid, proxies=None):
        data = {}
        self.route.SendRequest("POST", f"/v8/guilds/{serverid}/delete", proxies, data)
        return f"Deleted Server {serverid}"
    
    def ChangeUsername(self, username, proxies=None):
        data = {
            "username": username
        }
        
        result = self.route.SendRequest("PATCH", "/v8/users/@me", proxies, data)
        return result.json()

    def ChangeProfilePicture(self, path, proxies=None):
        image = None
        with open(path, "rb") as pic:
            image = "data:image/png;base64," + base64.b64encode(pic.read()).decode('utf-8')
        imagePayload = {
            "avatar": image
        }
        
        result = self.route.SendRequest("PATCH", "/v8/users/@me", proxies, imagePayload)
        return result.json()

    

            


discord = SelfDiscord("Nzg1NTkzNDEzODM0ODk5NDg2.X-7PvQ.Pi7zamBUZuoFSZAOcONRTJm26XU", "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.309 Chrome/83.0.4103.122 Electron/9.3.5 Safari/537.36", "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjAuMC4zMDkiLCJvc192ZXJzaW9uIjoiMTAuMC4xODM2MyIsIm9zX2FyY2giOiJ4NjQiLCJjbGllbnRfYnVpbGRfbnVtYmVyIjo3MzgwNiwiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0=")
print(discord.DeleteServer("795550386508791829"))