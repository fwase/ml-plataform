"""Abstract base for model metadata persistence."""

from abc import ABC, abstractmethod
from typing import List

from model_registry.repository.models import ModelMetadata


class BaseRepository(ABC):
    """Contract for storing and querying model metadata."""

    @abstractmethod
    def create(self, metadata: ModelMetadata) -> None:
        """Persist new metadata. Must raise if the model name already exists."""
        pass

    @abstractmethod
    def get_by_name(self, name: str) -> ModelMetadata | None:
        """Return metadata for ``name``, or None if not found."""
        pass

    @abstractmethod
    def update(self, name: str, metadata: ModelMetadata) -> None:
        """Replace metadata for an existing model. Must raise if missing."""
        pass

    @abstractmethod
    def list_all(self) -> List[ModelMetadata]:
        pass
