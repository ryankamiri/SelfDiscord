.. currentmodule:: SelfDiscord

.. _proxies:

Using Proxies
==============

Using Proxies to bypass rate limiting or other features is really easy to do. Every function has proxy support. All you need to do is to add proxies=[your list of proxies] to the arguements. Take a look at the example below.

The file proxies.txt would have proxies formatted like this: 127.0.0.0:80.

Additionaly, you may add your own useragent and x-super-properties like in the example below to pass off the requests as realistic. By default, no user agent or x-super-properties is givin to the Discord API by SelfDiscord.

If you choose not to use proxies, SelfDiscord handles rate limiting by waiting the specific time givin by the Discord API.

.. code-block:: python3

    import SelfDiscord

    proxies = []
    with open("proxies.txt") as file:
        for line in file:
            proxies.append(line.strip())

    client = SelfDiscord(token='token', useragent="Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.309 Chrome/83.0.4103.122 Electron/9.3.5 Safari/537.36", xsuperprops="eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjAuMC4zMDkiLCJvc192ZXJzaW9uIjoiMTAuMC4xODM2MyIsIm9zX2FyY2giOiJ4NjQiLCJjbGllbnRfYnVpbGRfbnVtYmVyIjo3MzgwNiwiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0=")
    client.SendMessage("Hi from SelfDiscord!", "channelid", proxies=proxies)