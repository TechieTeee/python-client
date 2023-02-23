"""
This type stub file was generated by pyright.
"""

from typing import Optional
from polywrap_core import IFileReader
from polywrap_result import Result

class InMemoryFileReader(IFileReader):
    _wasm_manifest: Optional[bytes]
    _wasm_module: Optional[bytes]
    _base_file_reader: IFileReader
    def __init__(self, base_file_reader: IFileReader, wasm_module: Optional[bytes] = ..., wasm_manifest: Optional[bytes] = ...) -> None:
        ...
    
    async def read_file(self, file_path: str) -> Result[bytes]:
        ...
    

