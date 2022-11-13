from __future__ import annotations

from abc import abstractmethod
from dataclasses import dataclass, field
from typing import List, Optional, Union, Dict

from polywrap_manifest import AnyWrapManifest, DeserializeManifestOptions
from polywrap_result import Result

from .invoke import Invoker
from .uri import Uri
from .env import Env
from .uri_resolver import IUriResolver
from .uri_resolver_handler import UriResolverHandler

@dataclass(slots=True, kw_only=True)
class ClientConfig:
    envs: Dict[Uri, Env] = field(default_factory=dict) 
    interfaces: Dict[Uri, List[Uri]] = field(default_factory=dict)
    resolver: IUriResolver


@dataclass(slots=True, kw_only=True)
class GetUriResolversOptions:
    pass


@dataclass(slots=True, kw_only=True)
class GetFileOptions:
    path: str
    encoding: Optional[str] = "utf-8"


@dataclass(slots=True, kw_only=True)
class GetManifestOptions(DeserializeManifestOptions):
    pass


class Client(Invoker, UriResolverHandler):
    @abstractmethod
    def get_interfaces(self) -> Dict[Uri, List[Uri]]:
        pass

    @abstractmethod
    def get_envs(self) -> Dict[Uri, Env]:
        pass

    @abstractmethod
    def get_env_by_uri(
        self, uri: Uri
    ) -> Union[Env, None]:
        pass

    @abstractmethod
    def get_uri_resolver(
        self, options: Optional[GetUriResolversOptions] = None
    ) -> IUriResolver:
        pass

    @abstractmethod
    async def get_file(
        self, uri: Uri, options: GetFileOptions
    ) -> Result[Union[bytes, str]]:
        pass

    @abstractmethod
    async def get_manifest(
        self, uri: Uri, options: Optional[GetManifestOptions] = None
    ) -> Result[AnyWrapManifest]:
        pass
