import os
import cloudpickle

from model_registry.repository.base import BaseRepository
from model_registry.repository.models import ModelMetadata


class InMemoryRepository(BaseRepository):

    def __init__(self) -> None:
        self._store: dict[str, ModelMetadata] = {}

    def exists(self, name: str) -> bool:
        return name in self._store

    def __get_artifact_registry_path(self, model_name: str) -> str:
        base_project_path = "/".join(__file__.split("/")[:-2])

        return os.path.join(base_project_path, f"artifacts/{model_name}")

    def create(self, metadata: ModelMetadata, model_object: object) -> None:
        if self.exists(metadata.name):
            raise Exception("Model already exist!")
        
        model_artifact_path = self.__get_artifact_registry_path(metadata.name)
        os.makedirs(model_artifact_path)
        metadata.artifact_store = f"{model_artifact_path}/model.pkl"

        self._store[metadata.name] = metadata

        with open(metadata.artifact_store, "wb") as file:
            cloudpickle.dump(model_object, file)

    def get_by_name(self, name: str) -> ModelMetadata | None:
        if not self.exists(name):
            raise Exception("Model not exist!")
        return self._store.get(name)

    def update(self, name: str, metadata: ModelMetadata) -> None:
        if not self.exists(name):
            raise Exception("Model not exist!")
        self._store[name] = metadata

    def list_all(self) -> list[ModelMetadata]:
        return list(self._store.values())
