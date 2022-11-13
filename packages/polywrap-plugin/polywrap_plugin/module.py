from abc import ABC
from typing import Any, Dict, TypeVar, Generic, List

from polywrap_core import Invoker
from polywrap_result import Err, Ok, Result

TConfig = TypeVar('TConfig')
TResult = TypeVar('TResult')

class PluginModule(Generic[TConfig, TResult], ABC):
    env: Dict[str, Any]
    config: TConfig

    def __init__(self, config: TConfig):
        self.config = config

    def set_env(self, env: Dict[str, Any]) -> None:
        self.env = env

    async def __wrap_invoke__(self, method: str, args: Dict[str, Any], client: Invoker) -> Result[TResult]:
        methods: List[str] = [name for name in dir(self) if name == method]

        if not methods:
            return Err(Exception(f"{method} is not defined in plugin"))

        callable_method = getattr(self, method)
        return Ok(callable_method(args, client)) if callable(callable_method) else Err(Exception(f"{method} is an attribute, not a method"))