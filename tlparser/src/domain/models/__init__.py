"""
__init__.py: File, containing other domain model modules to simplify import.
"""


from typing import TypeVar
from domain.models.base import AggregateRoot, DomainModel
from domain.models.game import TwichGame
from domain.models.stream import TwichStream
from domain.models.user import TwichUser


DM = TypeVar('DM', bound=DomainModel)


__all__: list[str] = [
    'AggregateRoot',
    'DomainModel',
    'DM',
    'TwichGame',
    'TwichStream',
    'TwichUser',
    'DM',
]
