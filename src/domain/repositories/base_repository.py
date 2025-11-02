from abc import ABC, abstractmethod
from typing import Optional, TypeVar, Generic, List

T = TypeVar("T")


class BaseRepository(ABC, Generic[T]):
    @abstractmethod
    def get_all(self) -> List[T]:
        pass

    @abstractmethod
    def get_by_id(self, id: str) -> Optional[T]:
        pass

    @abstractmethod
    def create(self, entity: T) -> bool:
        pass

    @abstractmethod
    def update(self, entity: T) -> bool:
        pass

    @abstractmethod
    def delete(self, id: str) -> bool:
        pass
