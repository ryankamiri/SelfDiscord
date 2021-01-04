import SelfDiscord

client = SelfDiscord(token='token')

print(f"Logged in as {client.username}#{client.discriminator}")
print("Starting server creation")

#Create the server
serverid = client.CreateServer("New Server made by SelfDiscord")["id"]

#Create the category and channels
categoryid = client.CreateCategory(serverid, "SelfDiscord")["id"]
client.CreateTextChannel(serverid, "welcome")
client.CreateTextChannel(serverid, "selfdiscord-general", categoryid)
client.CreateVoiceChannel(serverid, "Self Discord Voice", categoryid)

print("Finished Creating and Setting up Server!")