# Automatically generated by pb2py
# fmt: off
from .. import protobuf as p


class HDNodeType(p.MessageType):

    def __init__(
        self,
        depth: int = None,
        fingerprint: int = None,
        child_num: int = None,
        chain_code: bytes = None,
        private_key: bytes = None,
        public_key: bytes = None,
    ) -> None:
        self.depth = depth
        self.fingerprint = fingerprint
        self.child_num = child_num
        self.chain_code = chain_code
        self.private_key = private_key
        self.public_key = public_key

    @classmethod
    def get_fields(cls):
        return {
            1: ('depth', p.UVarintType, 0),  # required
            2: ('fingerprint', p.UVarintType, 0),  # required
            3: ('child_num', p.UVarintType, 0),  # required
            4: ('chain_code', p.BytesType, 0),  # required
            5: ('private_key', p.BytesType, 0),
            6: ('public_key', p.BytesType, 0),
        }
