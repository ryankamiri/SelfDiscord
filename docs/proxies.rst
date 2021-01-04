.. currentmodule:: SelfDiscord

.. _proxies:

Using Proxies
==============

Using Proxies to bypass rate limiting or other features is really easy to do. Every function has proxy support. All you need to do is to add proxies=[your list of proxies] to the arguements. Take a look at the example below.

The file proxies.txt would have proxies formatted like this: 127.0.0.0:80

If you choose not to use proxies, SelfDiscord handles rate limiting by waiting the specific time givin by the Discord API.

.. code-block:: python3

    import SelfDiscord

    proxies = []
    with open("proxies.txt") as file:
        for line in file:
            proxies.append(line.strip())

    client = SelfDiscord(token='token')
    client.SendMessage("Hi from SelfDiscord!", "channelid", proxies=proxies)