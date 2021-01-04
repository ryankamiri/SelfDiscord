import SelfDiscord

client = SelfDiscord(token='token', useragent="Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.309 Chrome/83.0.4103.122 Electron/9.3.5 Safari/537.36", xsuperprops="eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjAuMC4zMDkiLCJvc192ZXJzaW9uIjoiMTAuMC4xODM2MyIsIm9zX2FyY2giOiJ4NjQiLCJjbGllbnRfYnVpbGRfbnVtYmVyIjo3MzgwNiwiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0=")

print(f"Logged in as {client.username}#{client.discriminator}")

#Get Proxies to bypass rate limiting
proxies = []
with open("proxies.txt") as file:
    for line in file:
        proxies.append(line.strip())

channelid = str(input("Please enter a channelid to spam: "))
print("Starting Spam!")
while(True):
    #Send message in an infinity loop
    client.SendMessage("Spammed from SelfDiscord!", channelid, proxies=proxies)