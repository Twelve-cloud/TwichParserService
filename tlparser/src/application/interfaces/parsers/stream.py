"""
stream.py: File, containing parser interface for a twich stream.
"""


from domain.interfaces.parsers import ITwichParser
from domain.models import TwichStream


class ITwichStreamParser(ITwichParser):
    async def parse_stream(self, user_login: str) -> TwichStream:
        pass
