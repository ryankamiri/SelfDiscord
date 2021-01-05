.. currentmodule:: SelfDiscord

.. _getuserinfo:

GetUserInfo
==============

Returns information about current user.

.. code-block:: python3

    client.GetUserInfo()

.. _getdms:

GetDMs
==============

Returns all dms of current user.

.. code-block:: python3

    client.GetDMs()

.. _getfriends:

GetFriends
==============

Returns all friends of current user.

.. code-block:: python3

    client.GetFriends()

.. _addfriend:

AddFriend
==============

Sends a friend request to givin user.

.. code-block:: python3

    client.AddFriend("userid")

.. _unfriend:

UnFriend
==============

UnFriends provided user.

.. code-block:: python3

    client.UnFriend("userid")

.. _blockuser:

BlockUser
==============

Blocks specified user.

.. code-block:: python3

    client.BlockUser("userid")

.. _blockuser:

UnBlockUser
==============

UnBlocks specified user.

.. code-block:: python3

    client.UnBlockUser("userid")

.. _changeusername:

ChangeUsername
==============

Changes username to new username provided.

.. code-block:: python3

    client.ChangeUsername("username")

.. _changeavatar:

ChangeAvatar
==============

Changes current user's avatar.

.. code-block:: python3

    client.ChangeAvatar("path to avatar")

.. _convertusertochannel:

ConvertUserToChannel
==============

Converts user id to a channel id. Returns None if there is no dm with this user.

.. code-block:: python3

    client.ConvertUserToChannel("userid")

.. _convertchanneltouser:

ConvertChannelToUser
==============

Converts channel id to a user id. Returns None if there is no dm with this user.

.. code-block:: python3

    client.ConvertChannelToUser("channelid")

.. _convertidtousername:

ConvertIdToUsername
==============

Converts user id to username. Returns None if there is no dm with this user.

.. code-block:: python3

    client.ConvertIdToUsername("userid")

.. _convertusernametoid:

ConvertUsernameToId
==============

Converts username to user id. Returns None if there is no dm with this user.

.. code-block:: python3

    client.ConvertUsernameToId("username")