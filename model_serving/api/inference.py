from typing import List
import pandas as pd
import numpy as np

from model_serving.model_repository import ModelRepository
from .schemas.schemas import InferenceRequest, InferenceResponse


class Inference:

    @staticmethod
    def to_dataframe(features: List[object]) -> pd.DataFrame:
        return pd.DataFrame([features])
    
    @staticmethod
    def to_response(prediction: np.ndarray) -> InferenceResponse:
        prediction_value = prediction.tolist()
        
        return InferenceResponse(predicted_value=prediction_value)

    @staticmethod
    def validate_request(request: InferenceRequest, metadata: dict[str, object]) -> None:
        DEFAULT_TOTAL_FEATURES = -1
        if metadata.get("total_features", DEFAULT_TOTAL_FEATURES) != len(request.features_value):
            raise Exception("Size of input features is different from model.")

    @staticmethod
    def run(model_name: str, request: InferenceRequest) -> InferenceResponse:
        ## check if model exists and get pickle model
        model = ModelRepository().get_artifact(model_name)

        ## check if the features in payload is the same size that features model
        metadata = ModelRepository().get_metadata(model_name)
        Inference.validate_request(request, metadata)

        ## mapping to dataframe
        features_df = Inference.to_dataframe(request.features_value)

        ## run inference
        prediction = model.predict(features_df)

        ## log inference

        ## mapping to dict
        prediction_response = Inference.to_response(prediction)

        return prediction_response
