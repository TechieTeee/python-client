"""
This type stub file was generated by pyright.
"""

from typing import List
from polywrap_core import IUriResolutionStep, Uri

class InfiniteLoopError(Exception):
    def __init__(self, uri: Uri, history: List[IUriResolutionStep]) -> None:
        ...
    


