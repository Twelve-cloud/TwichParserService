"""
base.py: File, containing base dto.
"""


from abc import ABC
from dataclasses import dataclass


@dataclass(frozen=True)
class BaseDTO(ABC):
    pass
