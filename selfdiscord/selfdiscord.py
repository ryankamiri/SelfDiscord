from .route import Route
import random
import base64
import requests

class SelfDiscord:
    def __init__(self, token, useragent=None, xsuperprops=None):
        self.CheckForUpdates(0.6)
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
    
    def CheckForUpdates(self, version):
        currentversion = float(requests.get("https://pypi.org/pypi/SelfDiscord/json").json()["info"]["version"])
        if currentversion > version:
            print(f"WARNING: You’re using version {version} but version {currentversion} is available. Use \"pip install SelfDiscord --upgrade\" to update.")

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
        result = self.route.SendRequest("GET", "/v8/users/@me/guilds", proxies)
        return result.json()
    
    def GetDMs(self, proxies=None):
        result = self.route.SendRequest("GET", "/v8/users/@me/channels", proxies)
        return result.json()
    
    def GetFriends(self, proxies=None):
        result = self.route.SendRequest("GET", "/v8/users/@me/relationships", proxies)
        return result.json()
    
    def ConvertUserToChannel(self, userid, proxies=None):
        dms = self.GetDMs(proxies)
        for dm in dms:
            if dm["type"] == 1 and dm["recipients"][0]["id"] == userid:
                return dm["id"]
        return None
    
    def ConvertChannelToUser(self, channelid, proxies=None):
        dms = self.GetDMs(proxies)
        for dm in dms:
            if dm["type"] == 1 and dm["id"] == channelid:
                return dm["recipients"][0]["id"]
        return None
    
    def ConvertIdToUsername(self, userid, proxies=None):
        dms = self.GetDMs(proxies)
        for dm in dms:
            if dm["type"] == 1 and dm["recipients"][0]["id"] == userid:
                return dm["recipients"][0]["username"]
        return None
    
    def ConvertUsernameToId(self, username, proxies=None):
        dms = self.GetDMs(proxies)
        for dm in dms:
            if dm["type"] == 1 and dm["recipients"][0]["username"] == username:
                return dm["recipients"][0]["id"]
        return None

    def CreateNewDM(self, userid, proxies=None):
        data = {"recipients":[userid]}
        result = self.route.SendRequest("POST", "/v8/users/@me/channels", proxies, data)
        return result.json()
    
    def CreateNewGroup(self, channelid, userid, proxies=None):
        result = self.route.SendRequest("PUT", f"/v8/channels/{channelid}/recipients/{userid}", proxies)
        return result.json()

    def AddToGroup(self, channelid, userid, proxies=None):
        self.route.SendRequest("PUT", f"/v8/channels/{channelid}/recipients/{userid}", proxies)
        return f"Added {userid} to {channelid}"
    
    def RemoveFromGroup(self, channelid, userid, proxies=None):
        self.route.SendRequest("DELETE", f"/v8/channels/{channelid}/recipients/{userid}", proxies)
        return f"Removed {userid} from {channelid}"

    def SendTyping(self, channelid, proxies=None):
        self.route.SendRequest("POST", f"/v8/channels/{channelid}/typing", proxies)
        return f"Sent Typing to {channelid}"

    def SendMessage(self, content, channelid, proxies=None):
        data = {"content":content,"nonce":''.join([str(random.randint(1, 9)) for i in range(18)]),"tts":False}
        result = self.route.SendRequest("POST", f"/v8/channels/{channelid}/messages", proxies, data)
        return result.json()
    
    def SendTTSMessage(self, content, channelid, proxies=None):
        data = {"content":content,"nonce":''.join([str(random.randint(1, 9)) for i in range(18)]),"tts":True}
        result = self.route.SendRequest("POST", f"/v8/channels/{channelid}/messages", proxies, data)
        return result.json()

    def EditMessage(self, content, channelid, messageid, proxies=None):
        data = {"content":content}
        result = self.route.SendRequest("PATCH", f"/v8/channels/{channelid}/messages/{messageid}", proxies, data)
        return result.json()
    
    def DeleteMessage(self, channelid, messageid, proxies=None):
        self.route.SendRequest("DELETE", f"/v8/channels/{channelid}/messages/{messageid}", proxies)
        return f"Deleted Message {messageid}"

    def GetMessages(self, channelid, proxies=None):
        result = self.route.SendRequest("GET", f"/v8/channels/{channelid}/messages", proxies)
        return result.json()
    
    def GetOldMessages(self, channelid, before, proxies=None):
        result = self.route.SendRequest("GET", f"/v8/channels/{channelid}/messages?before={before}", proxies)
        return result.json()

    def CreateCategory(self, serverid, name, proxies=None):
        data = {"type":4,"name":name,"permission_overwrites":[]}
        result = self.route.SendRequest("POST", f"/v8/guilds/{serverid}/channels", proxies, data)
        return result.json()

    def CreateTextChannel(self, serverid, name, parentid=None, proxies=None):
        name = name.lower()
        name.replace(" ", "-")
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

    def BlockUser(self, userid, proxies=None):
        data = {"type":2}
        self.route.SendRequest("PUT", f"/v8/users/@me/relationships/{userid}", proxies, data)
        return f"Blocked {userid}"

    def UnBlockUser(self, userid, proxies=None):
        self.route.SendRequest("DELETE", f"/v8/users/@me/relationships/{userid}", proxies)
        return f"UnBlocked {userid}"

    def MuteChannel(self, channelid, proxies=None):
        data = {"channel_overrides":{channelid:{"muted":True,"mute_config":{"selected_time_window":-1,"end_time":None}}}}
        result = self.route.SendRequest("PATCH", "/v8/users/@me/guilds/%40me/settings", proxies, data)
        return result.json()
    
    def UnMuteChannel(self, channelid, proxies=None):
        data = {"channel_overrides":{channelid:{"muted":False}}}
        result = self.route.SendRequest("PATCH", "/v8/users/@me/guilds/%40me/settings", proxies, data)
        return result.json()

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

    def ChangeAvatar(self, path, proxies=None):
        image = None
        with open(path, "rb") as pic:
            image = "data:image/png;base64," + base64.b64encode(pic.read()).decode('utf-8')
        imagePayload = {
            "avatar": image
        }
        
        result = self.route.SendRequest("PATCH", "/v8/users/@me", proxies, imagePayload)
        return result.json()
    
    def GetServerInfo(self, serverid, proxies=None):
        result = self.route.SendRequest("GET", f"/v8/guilds/{serverid}", proxies)
        return result.json()
    
    def GetServerChannels(self, serverid, proxies=None):
        result = self.route.SendRequest("GET", f"/v8/guilds/{serverid}/channels", proxies)
        return result.json()
    
    def GetServerMemberInfo(self, serverid, userid, proxies=None):
        result = self.route.SendRequest("GET", f"/v8/guilds/{serverid}/members/{userid}", proxies)
        return result.json()
    
    def KickUser(self, serverid, userid, reason=None, proxies=None):
        if reason == None:
            reason = ""
        self.route.SendRequest("DELETE", f"/v8/guilds/{serverid}/members/{userid}?reason={reason}", proxies)
        return f"Kicked {userid} from {serverid}"
    
    def BanUser(self, serverid, userid, delete_message_days, reason=None, proxies=None):
        if reason == None:
            reason = ""
        data = {"delete_message_days":str(delete_message_days),"reason":reason}
        self.route.SendRequest("PUT", f"/v8/guilds/{serverid}/members/bans/{userid}", proxies, data)
        return f"Banned {userid} from {serverid}"

    def AddReaction(self, channelid, messageid, emoji, proxies=None):
        hexemoji = emoji.encode('utf-8')
        hexemoji = hexemoji.hex()
        hexemoji = f"%{hexemoji[0]}{hexemoji[1]}%{hexemoji[2]}{hexemoji[3]}%{hexemoji[4]}{hexemoji[5]}%{hexemoji[6]}{hexemoji[7]}"
        self.route.SendRequest("PUT", f"/v8/channels/{channelid}/messages/{messageid}/reactions/{hexemoji}/%40me", proxies)
        return f"Reacted with {emoji} to {messageid}"
    
    def DeleteReaction(self, channelid, messageid, emoji, proxies=None):
        hexemoji = emoji.encode('utf-8')
        hexemoji = hexemoji.hex()
        hexemoji = f"%{hexemoji[0]}{hexemoji[1]}%{hexemoji[2]}{hexemoji[3]}%{hexemoji[4]}{hexemoji[5]}%{hexemoji[6]}{hexemoji[7]}"
        self.route.SendRequest("DELETE", f"/v8/channels/{channelid}/messages/{messageid}/reactions/{hexemoji}/%40me", proxies)
        return f"Deleted {emoji} from {messageid}"

#Made By RedBall