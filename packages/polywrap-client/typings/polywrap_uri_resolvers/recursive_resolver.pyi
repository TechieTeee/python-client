"""
This type stub file was generated by pyright.
"""

from polywrap_core import Client, IUriResolutionContext, IUriResolver, Uri, UriPackageOrWrapper
from polywrap_result import Result

class RecursiveResolver(IUriResolver):
    __slots__ = ...
    resolver: IUriResolver
    def __init__(self, resolver: IUriResolver) -> None:
        ...
    
    async def try_resolve_uri(self, uri: Uri, client: Client, resolution_context: IUriResolutionContext) -> Result[UriPackageOrWrapper]:
        ...
    


