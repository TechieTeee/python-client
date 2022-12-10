"""
This type stub file was generated by pyright.
"""

from abc import ABC, abstractmethod
from typing import List
from .uri import Uri
from .uri_resolution_step import IUriResolutionStep

class IUriResolutionContext(ABC):
    @abstractmethod
    def is_resolving(self, uri: Uri) -> bool:
        ...
    
    @abstractmethod
    def start_resolving(self, uri: Uri) -> None:
        ...
    
    @abstractmethod
    def stop_resolving(self, uri: Uri) -> None:
        ...
    
    @abstractmethod
    def track_step(self, step: IUriResolutionStep) -> None:
        ...
    
    @abstractmethod
    def get_history(self) -> List[IUriResolutionStep]:
        ...
    
    @abstractmethod
    def get_resolution_path(self) -> List[Uri]:
        ...
    
    @abstractmethod
    def create_sub_history_context(self) -> IUriResolutionContext:
        ...
    
    @abstractmethod
    def create_sub_context(self) -> IUriResolutionContext:
        ...
    


