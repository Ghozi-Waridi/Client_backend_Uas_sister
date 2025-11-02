from abc import ABC, abstractmethod
from typing import List, Optional, Tuple, Any


class BaseService:
    @abstractmethod
    def get_all(self) -> Tuple[bool, List[Any], Optional[str]]:
        pass

    @abstractmethod
    def get_by_id(self, id: str) -> Tuple[bool, Optional[Any], Optional[str]]:
        pass

    @abstractmethod
    def create(self, data: dict) -> Tuple[bool, Optional[str]]:
        pass

    @abstractmethod
    def update(self, data: dict) -> Tuple[bool, Optional[str]]:
        pass

    @abstractmethod
    def delete(self, id: str) -> Tuple[bool, Optional[str]]:
        pass
