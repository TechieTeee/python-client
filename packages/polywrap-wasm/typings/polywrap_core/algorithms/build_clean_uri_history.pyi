"""
This type stub file was generated by pyright.
"""

from typing import List, Optional, Union
from ..types import IUriResolutionStep

CleanResolutionStep = List[Union[str, "CleanResolutionStep"]]
def build_clean_uri_history(history: List[IUriResolutionStep], depth: Optional[int] = ...) -> CleanResolutionStep:
    ...

