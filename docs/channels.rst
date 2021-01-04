.. currentmodule:: SelfDiscord

.. _createnewdm:

CreateNewDM
==============

Creates a new DM with specified user.

.. code-block:: python3

    client.CreateNewDM("userid")

.. _createnewgroup:

CreateNewGroup
==============

Creates a new Group with specified user.

.. code-block:: python3

    client.CreateNewGroup("channelid of user", "new userid")

.. _addgroup:

AddToGroup
==============

Adds a user to a group.

.. code-block:: python3

    client.AddToGroup("channelid of group", "userid")

.. _removefromgroup:

RemoveFromGroup
==============

Removes a user from a group.

.. code-block:: python3

    client.RemoveFromGroup("channelid of group", "userid")

.. _sendtyping:

SendTyping
==============

Sends current user's typing que to channel.

.. code-block:: python3

    client.SendTyping("channelid")

.. _sendmessage:

SendMessage
==============

Sends a message to channel.

.. code-block:: python3

    client.SendMessage("message", "channelid")

.. _sendttsmessage:

SendTTSMessage
==============

Sends a tts message to channel.

.. code-block:: python3

    client.SendTTSMessage("message", "channelid")

.. _editmessage:

EditMessage
==============

Edits a message.

.. code-block:: python3

    client.EditMessage("new message", "channelid", "messageid")

.. _deletemessage:

DeleteMessage
==============

Deletes a certain message.

.. code-block:: python3

    client.DeleteMessage("channelid", "messageid")

.. _getmessages:

GetMessages
==============

Gets messages of channel.

.. code-block:: python3

    client.GetMessages("channelid")

.. _getoldmessages:

GetOldMessages
==============

Gets old messages of channel before a certain period time. Time format can be illustrated as 795491538364530708.

.. code-block:: python3

    client.GetOldMessages(time.time() * 1000)

.. _deletechannel:

DeleteChannel
==============

Deletes a certain channel.

.. code-block:: python3

    client.DeleteChannel("channelid")

.. _mutechannel:

MuteChannel
==============

Mutes a certain channel.

.. code-block:: python3

    client.MuteChannel("channelid")

.. _unmutechannel:

UnMuteChannel
==============

Un mutes a certain channel.

.. code-block:: python3

    client.UnMuteChannel("channelid")