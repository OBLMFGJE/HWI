# Automatically generated by pb2py
# fmt: off
from .. import protobuf as p


class ButtonRequest(p.MessageType):
    MESSAGE_WIRE_TYPE = 26

    def __init__(
        self,
        code: int = None,
        data: str = None,
    ) -> None:
        self.code = code
        self.data = data

    @classmethod
    def get_fields(cls):
        return {
            1: ('code', p.UVarintType, 0),
            2: ('data', p.UnicodeType, 0),
        }
