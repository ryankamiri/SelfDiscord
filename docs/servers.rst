.. currentmodule:: SelfDiscord

.. _getservers:

GetServers
==============

Returns all servers of current users.

.. code-block:: python3

    client.GetServers()

.. _createcategory:

CreateCategory
==============

Creates a Category in specified server.

.. code-block:: python3

    client.CreateCategory("serverid", "name")

.. _createtextchannel:

CreateTextChannel
==============

Creates a Text Channel in specified server.

.. code-block:: python3

    client.CreateTextChannel("serverid", "name", "categoryid (not required)")

.. _createvoicechannel:

CreateVoiceChannel
==============

Creates a Voice Channel in specified server.

.. code-block:: python3

    client.CreateVoiceChannel("serverid", "name", "categoryid (not required)")

.. _joinserver:

JoinServer
==============

Joins server with given invite code.

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

Creates Server with given name.

.. code-block:: python3

    client.CreateServer("name")

.. _getserverinfo:

GetServerInfo
==============

Returns server info. 

.. code-block:: python3

    client.GetServerInfo("serverid")

.. _getserverchannels:

GetServerChannels
==============

Returns server channels. 

.. code-block:: python3

    client.GetServerChannels("serverid")

.. _getservermemberinfo:

GetServerMemberInfo
==============

Returns specific member's info in a given server.

.. code-block:: python3

    client.GetServerMemberInfo("serverid", "userid")

.. _kickuser:

KickUser
==============

Kicks a user from a server.

.. code-block:: python3

    client.KickUser("serverid", "userid", "reason (not required)")

.. _banuser:

BanUser
==============

Bans a user from a server. The "delete_message_days" arguement must be a string and is the messages from x amount of days before to delete. Can be "0" as well.

.. code-block:: python3

    client.BanUser("serverid", "userid", "delete_message_days", "reason (not required)")