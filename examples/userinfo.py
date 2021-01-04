import SelfDiscord

client = SelfDiscord(token='token')

print(f"Hello my discord is {client.username}#{client.discriminator}")
print(f"You can contact me at {client.email} or {client.phone}")
if client.nsfw_allowed:
    print("I am above the age of 18.")
else:
    print("I am below the age of 18.")
if client.verified:
    print("My account is verified.")
else:
    print("My account is not verified.")
if client.mfa_enabled:
    print("My account has 2FA enabled.")
else:
    print("My account does not have 2FA enabled.")
