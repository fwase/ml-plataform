from model_registry.model_registry import ModelRegistry

class ModelServing:

    @staticmethod
    def deploy(model_name: str):
        model_metadata = ModelRegistry.get_model_metadata(model_name)
        if model_metadata["published"]:
            raise Exception("Model already deployed!")
        
        model_metadata["published"] = True
        ModelRegistry.update_model_metadata(model_name, model_metadata)
