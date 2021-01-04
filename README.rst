SelfDiscord

.. image:: https://discord.com/api/guilds/795758135679516762/embed.png
   :target: https://discord.gg/CSJZYC3AZF
   :alt: Discord server invite
.. image:: https://img.shields.io/pypi/v/SelfDiscord.svg
   :target: https://pypi.python.org/pypi/SelfDiscord
   :alt: PyPI version info
.. image:: https://img.shields.io/pypi/pyversions/SelfDiscord.svg
   :target: https://pypi.python.org/pypi/SelfDiscord
   :alt: PyPI supported Python versions

An easy API wrapper for discord self bots written in python.

Key Features
-------------

- Proxy Support.
- Self Bot Support.
- Proper rate limit handling.
- Coverage of the supported Discord API.
- Optimised in both speed and memory.

Installing
----------

**Python 3.5.3 or higher is required**

To install the library without full voice support, you can just run the following command:

.. code:: sh

    # Linux/macOS
    python3 -m pip install -U SelfDiscord

    # Windows
    py -3 -m pip install -U SelfDiscord


Quick Example
--------------

.. code:: py

    from selfdiscord import SelfDiscord

    client = SelfDiscord(token='token')

    print(f"Logged in as {client.username}#{client.discriminator}")

    client.CreateServer("SelfDiscord")

You can find more examples in the examples directory.

Links
------

- `Documentation <https://github.com/RedBallG/SelfDiscord/tree/main/docs>`_
- `Official Discord Server <https://discord.gg/CSJZYC3AZF>`_
- `Discord API <https://discord.gg/discord-api>`_