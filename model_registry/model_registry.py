import cloudpickle
from typing import List

from model_registry.repository import ModelMetadata, in_memory_repository_singleton


class ModelRegistry:

    @staticmethod
    def create(metadata: ModelMetadata, model_object: object) -> None:
        in_memory_repository_singleton.create(metadata, model_object)

    @staticmethod
    def get_model_metadata(name: str) -> ModelMetadata:
        return in_memory_repository_singleton.get_by_name(name)

    @staticmethod
    def update(name: str, metadata: ModelMetadata) -> None:
        in_memory_repository_singleton.update(name, metadata)

    @staticmethod
    def list_all() -> List[ModelMetadata]:
        return in_memory_repository_singleton.list_all()

    @staticmethod
    def get_model_artifact(name: str) -> object:
        model_metadata = ModelRegistry.get_model_metadata(name)
        if model_metadata is None:
            raise Exception("Model not exist!")
        
        with open(model_metadata.artifact_store, "rb") as file:
            return cloudpickle.load(file)

