## Test task
You need to write a REST interface for the chat-like system. One user could have a private conversation with another one and there could be several users in the same room talking to each other. In the django admin there should be available information about when the user last time send a message in the any of the rooms.

Get request should allow to get latest 10 messages from the room and with page parameters - other messages

Post request should create a new message in the room

Put/Patch should allow edit message in the room with restriction: user can’t edit the message older that 30 minutes, user can edit only own messages

You should provide also login/registration endpoints. Please use JWT token based auth.

## TODO
* unittests
