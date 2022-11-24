from abc import ABC, abstractmethod
from dataclasses import dataclass
from polywrap_core import Uri, IUriResolver, Env
from typing import Dict, Any, List, Optional, Union

@dataclass(slots=True, kw_only=True) 
class ClientConfig():
    """
    This Abstract class is used to configure the polywrap client before it executes a call
    The ClientConfig class is created and modified with the ClientConfigBuilder module
    """
    envs: Dict[Uri, Dict[str, Any]]
    interfaces: Dict[Uri, List[Uri]]
    resolver: List[IUriResolver]
    wrappers: List[Uri]


class BaseClientConfigBuilder(ABC):
    """
    An abstract base class of the `ClientConfigBuilder`, which uses the ABC module
    to define the methods that can be used to configure the `ClientConfig` object.
    """

    def __init__(self):
        self.config = ClientConfig(envs={}, interfaces={}, resolver=[], wrappers= [])

    @abstractmethod
    def build(self) -> ClientConfig:
        """Returns a sanitized config object from the builder's config."""
        pass

    @abstractmethod
    def get_envs(self)-> Dict[Uri, Dict[str, Any]]:
        """Returns the envs dictionary from the builder's config."""
        return self.config.envs

    @abstractmethod    
    def set_env(self, env: Env, uri: Uri):
        """Sets the envs dictionary in the builder's config, overiding any existing values."""
        if (env or uri) is None:
            raise KeyError("Must provide both an env or uri")
        self.config.envs[uri] = env
        return self

    @abstractmethod
    def add_env(self, env: Env = None , uri: Uri = None):
        """Adds an environment (in the form of an `Env`) for a given uri, without overwriting existing environments,
        unless the env key already exists in the environment, then it will overwrite the existing value"""
        if (env or uri) is None:
            raise KeyError("Must provide both an env or uri")
        
        if uri in self.config.envs.keys():
            for key in env.keys():
                self.config.envs[uri][key] = env[key]
        else:
            self.config.envs[uri] = env
        return self

    @abstractmethod
    def add_envs(self, envs: List[Env], uri: Uri = None):
        """
        Adds a list of environments (each in the form of an `Env`) for a given uri
        """
        for env in envs:
            self.add_env(env, uri )
        return self

    @abstractmethod
    def add_interface_implementations(self, interface_uri: Uri, implementations_uris: List[Uri]):
        """
        Adds a list of implementations (each in the form of an `Uri`) for a given interface
        """
        if interface_uri is None:
            raise ValueError()
        if interface_uri in self.config.interfaces.keys():
            self.config.interfaces[interface_uri] = self.config.interfaces[interface_uri] + implementations_uris
        else:
            self.config.interfaces[interface_uri] = implementations_uris
        return self

    @abstractmethod
    def add_wrapper(self, wrapper_uri: Uri) :
        """
        Adds a wrapper to the list of wrappers
        """
        self.config.wrappers.append(wrapper_uri)
        return self

    @abstractmethod
    def add_wrappers(self, wrappers_uris: List[Uri]) :
        """
        Adds a list of wrappers to the list of wrappers
        """
        for wrapper_uri in wrappers_uris:
            self.add_wrapper(wrapper_uri)
        return self

    @abstractmethod
    def remove_wrapper(self, wrapper_uri: Uri) :
        """
        Removes a wrapper from the list of wrappers
        """
        self.config.wrappers.remove(wrapper_uri)
        return self

    @abstractmethod
    def set_resolver(self, uri_resolver):
        """
        Sets a single resolver for the `ClientConfig` object before it is built
        """
        self.config.resolver = [uri_resolver]
        return self

    @abstractmethod
    def add_resolver(self, resolver: IUriResolver) :
        """
        Adds a resolver to the list of resolvers
        """

        if self.config.resolver is None:
            raise ValueError("This resolver is not set. Please set a resolver before adding resolvers.")
        self.config.resolver.append(resolver)
        return self

    @abstractmethod
    def add_resolvers(self, resolvers_list: List[IUriResolver]):
        """
        Adds a list of resolvers to the list of resolvers
        """
        for resolver in resolvers_list:
            self.add_resolver(resolver)
        return self

class ClientConfigBuilder(BaseClientConfigBuilder):
   
    def build(self)-> ClientConfig:
        """
        Returns a sanitized config object from the builder's config.
        """
        return self.config
    
    def get_envs(self) -> Dict[Uri, Dict[str, Any]]:
        return super().get_envs()

    def set_env(self, env: Env, uri: Uri)-> BaseClientConfigBuilder:
        super().set_env(env, uri)
        return self

    def add_env(self, env: Env, uri: Uri)-> BaseClientConfigBuilder:
        super().add_env(env, uri)
        return self

    def add_envs(self, envs: List[Env], uri: Uri)-> BaseClientConfigBuilder:
        super().add_envs(envs, uri)
        return self

    def add_interface_implementations(self, interface_uri: Uri, implementations_uris: List[Uri])-> BaseClientConfigBuilder:
        super().add_interface_implementations(interface_uri, implementations_uris)
        return self

    def add_wrapper(self, wrapper_uri: Uri)-> BaseClientConfigBuilder:
        super().add_wrapper(wrapper_uri)
        return self

    def add_wrappers(self, wrappers_uris: List[Uri])-> BaseClientConfigBuilder:
        super().add_wrappers(wrappers_uris)
        return self

    def remove_wrapper(self, wrapper_uri: Uri)-> BaseClientConfigBuilder:
        super().remove_wrapper(wrapper_uri)
        return self 
    
    def set_resolver(self, uri_resolver: IUriResolver)-> BaseClientConfigBuilder:
        super().set_resolver(uri_resolver)
        return self

    def add_resolver(self, resolver: IUriResolver)-> BaseClientConfigBuilder:
        super().add_resolver(resolver)
        return self

    def add_resolvers(self, resolvers_list: List[IUriResolver])-> BaseClientConfigBuilder:
        super().add_resolvers(resolvers_list)
        return self


