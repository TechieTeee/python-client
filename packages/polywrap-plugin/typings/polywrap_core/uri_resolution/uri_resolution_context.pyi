"""
This type stub file was generated by pyright.
"""

from typing import List, Optional, Set
from ..types import IUriResolutionContext, IUriResolutionStep, Uri

class UriResolutionContext(IUriResolutionContext):
    resolving_uri_set: Set[Uri]
    resolution_path: List[Uri]
    history: List[IUriResolutionStep]
    __slots__ = ...
    def __init__(self, resolving_uri_set: Optional[Set[Uri]] = ..., resolution_path: Optional[List[Uri]] = ..., history: Optional[List[IUriResolutionStep]] = ...) -> None:
        ...
    
    def is_resolving(self, uri: Uri) -> bool:
        ...
    
    def start_resolving(self, uri: Uri) -> None:
        ...
    
    def stop_resolving(self, uri: Uri) -> None:
        ...
    
    def track_step(self, step: IUriResolutionStep) -> None:
        ...
    
    def get_history(self) -> List[IUriResolutionStep]:
        ...
    
    def get_resolution_path(self) -> List[Uri]:
        ...
    
    def create_sub_history_context(self) -> UriResolutionContext:
        ...
    
    def create_sub_context(self) -> UriResolutionContext:
        ...
    


