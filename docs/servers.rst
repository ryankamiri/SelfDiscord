.. currentmodule:: SelfDiscord

.. _getservers:

GetServers
==============

Returns all servers of current users.

.. code-block:: python3

    client.GetServers()

.. _createtextchannel:

CreateTextChannel
==============

Creates a Text Channel in specified server.

.. code-block:: python3

    client.CreateTextChannel("serverid", "name", "categoryid (not required)")

.. _createtextchannel:

CreateVoiceChannel
==============

Creates a Voice Channel in specified server.

.. code-block:: python3

    client.CreateVoiceChannel("serverid", "name", "categoryid (not required)")

.. _joinserver:

JoinServer
==============

Joins server with givin invite code.

.. code-block:: python3

    client.JoinServer("invie code")

.. _leaveserver:

LeaveServer
==============

Leaves specified server.

.. code-block:: python3

    client.LeaveServer("serverid")

.. _createserver:

CreateServer
==============

Creates Server with givin name.

.. code-block:: python3

    client.CreateServer("name")