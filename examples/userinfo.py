import SelfDiscord

client = SelfDiscord(token='token')

print(f"Hello my discord is {client.username}#{client.discriminator}")