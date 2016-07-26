"""Defines Echo Reply message during the handshake."""

# System imports

# Third-party imports

from pyof.v0x01.common import header as of_header
from pyof.v0x01.foundation import base

__all__ = ('EchoReply',)

# Classes


class EchoReply(base.GenericMessage):
    """OpenFlow Reply message.

    This message does not contain a body beyond the OpenFlow Header.
    """

    header = of_header.Header(message_type=of_header.Type.OFPT_ECHO_REPLY,
                              length=8)

    def __init__(self, xid=None):
        """The constructor takes the parameters below.

        Args:
            xid (int): xid to be used on the message header.
        """
        super().__init__()
        self.header.xid = xid if xid else self.header.xid
