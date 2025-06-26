import os
import cloudpickle
import json

class ModelRegistry:

    @staticmethod
    def new_model(model_name: str, total_features: int, model_object: object) -> None:
        if ModelRegistry.model_exist(model_name):
            raise Exception("Model already exist!")

        model_artifact_path = os.path.join(ModelRegistry.get_artifact_registry_path(), f"{model_name}/")
        os.makedirs(model_artifact_path)

        with open(os.path.join(model_artifact_path, "model.pkl"), "wb") as file:
            cloudpickle.dump(model_object, file)

        metadata = {
            "name": model_name,
            "published": False,
            "total_features": total_features,
            "artifact_store": os.path.join(model_artifact_path, "model.pkl")
        }

        with open(os.path.join(model_artifact_path, "metadata.json"), "w") as file:
            json.dump(metadata, file)

    @staticmethod
    def get_artifact_registry_path() -> str:
        base_project_path = "/".join(__file__.split("/")[:-1])

        return os.path.join(base_project_path, "artifacts/")
    
    @staticmethod
    def model_exist(model_name: str) -> bool:
        model_artifact_path = os.path.join(ModelRegistry.get_artifact_registry_path(), f"{model_name}/")

        return os.path.exists(model_artifact_path)
    
    @staticmethod
    def get_model_artifact(model_name: str) -> object:
        if not ModelRegistry.model_exist(model_name):
            raise Exception("Model not exist!")

        model_artifact_file = os.path.join(
            ModelRegistry.get_artifact_registry_path(),
            f"{model_name}/",
            "model.pkl"
        )

        with open(model_artifact_file, "rb") as file:
            return cloudpickle.load(file)
        
    @staticmethod
    def get_model_metadata(model_name: str) -> dict[str, object]:
        if not ModelRegistry.model_exist(model_name):
            raise Exception("Model not exist!")

        model_metadata_file = os.path.join(
            ModelRegistry.get_artifact_registry_path(),
            f"{model_name}/",
            "metadata.json"
        )

        with open(model_metadata_file, "r") as file:
            return json.load(file)
        
    @staticmethod
    def update_model_metadata(model_name: str, new_model_metadata: dict[str, object]) -> dict[str, object]:
        if not ModelRegistry.model_exist(model_name):
            raise Exception("Model not exist!")

        model_metadata_file = os.path.join(
            ModelRegistry.get_artifact_registry_path(),
            f"{model_name}/",
            "metadata.json"
        )

        with open(model_metadata_file, "w") as file:
            json.dump(new_model_metadata, file)

    
    @staticmethod
    def list_all_models_metadata() -> dict[str, object]:
        models_folder = [
            folder.path.split("/")[-1]
            for folder
            in os.scandir(ModelRegistry.get_artifact_registry_path())
            if folder.is_dir()
        ]

        return [
            ModelRegistry.get_model_metadata(model)
            for model in models_folder
        ]

