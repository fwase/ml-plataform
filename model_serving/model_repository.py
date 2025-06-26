from model_registry.model_registry import ModelRegistry

class ModelRepository:
    _instance = None

    def __init__(self, load_strategy: str = "default"):
        print("Init ModelRepository")
        self.models = {}
        self.pre_load_models(load_strategy)
        self._instance = self


    def pre_load_models(self, load_strategy: str = "default"):
        print("Pre loading models")
        self.pre_load_models_default()

    def pre_load_models_default(self) -> object:
        """
        This strategy loads all models
        """
        all_models_metadata = ModelRegistry.list_all_models_metadata()
        for model_metadata in all_models_metadata:
            if model_metadata.get("published", False):
                model_name = model_metadata.get("name")
                self.models[model_name] = ModelRegistry.get_model_artifact(model_name)

        return None
    
    def add_new_model(self, model_name: str) -> None:
        self.models[model_name] = ModelRegistry.get_model_artifact(model_name)

    def get_artifact(self, model_name: str) -> object:
        metadata = ModelRegistry.get_model_metadata(model_name)
        if not metadata.get("published"):
            raise Exception("Model doesn't deployed!")
        
        if model_name in self.models:
            print("Load model from cache!")
        
        return ModelRegistry.get_model_artifact(model_name)
    
    def get_metadata(self, model_name: str) -> dict[str, object]:
        metadata = ModelRegistry.get_model_metadata(model_name)
        if not metadata.get("published"):
            raise Exception("Model doesn't deployed!")
        
        return metadata
