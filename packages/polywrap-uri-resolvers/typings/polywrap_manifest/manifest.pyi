"""
This type stub file was generated by pyright.
"""

from dataclasses import dataclass
from enum import Enum
from .wrap_0_1 import Abi as WrapAbi_0_1_0_1, WrapManifest as WrapManifest_0_1

"""
This file was automatically generated by scripts/templates/__init__.py.jinja2.
DO NOT MODIFY IT BY HAND. Instead, modify scripts/templates/__init__.py.jinja2,
and run python ./scripts/generate.py to regenerate this file.
"""
@dataclass(slots=True, kw_only=True)
class DeserializeManifestOptions:
    no_validate: Optional[bool] = ...


@dataclass(slots=True, kw_only=True)
class serializeManifestOptions:
    no_validate: Optional[bool] = ...


class WrapManifestVersions(Enum):
    VERSION_0_1 = ...
    def __new__(cls, value: int, *aliases: str) -> WrapManifestVersions:
        ...
    


class WrapManifestAbiVersions(Enum):
    VERSION_0_1 = ...


class WrapAbiVersions(Enum):
    VERSION_0_1 = ...


AnyWrapManifest = WrapManifest_0_1
AnyWrapAbi = WrapAbi_0_1_0_1
WrapManifest = ...
WrapAbi = WrapAbi_0_1_0_1
latest_wrap_manifest_version = ...
latest_wrap_abi_version = ...