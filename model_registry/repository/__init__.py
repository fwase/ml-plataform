"""Repository abstractions and implementations for model metadata."""

from model_registry.repository.in_memory import InMemoryRepository
from model_registry.repository.models import ModelMetadata

in_memory_repository_singleton = InMemoryRepository()

__all__ = [
    "InMemoryRepository",
    "ModelMetadata",
    "in_memory_repository_singleton",
]
