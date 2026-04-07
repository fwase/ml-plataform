from typing import Any

from pydantic import BaseModel


class ModelMetadata(BaseModel):

    name: str
    published: bool
    total_features: int
    artifact_store: str

    def to_dict(self) -> dict[str, Any]:
        return self.model_dump()

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "ModelMetadata":
        return cls.model_validate(data)
