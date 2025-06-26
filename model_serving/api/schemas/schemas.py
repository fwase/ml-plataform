from pydantic import BaseModel
from typing import List

class InferenceRequest(BaseModel):
    features_value: List[object]

class InferenceResponse(BaseModel):
    predicted_value: List[object]
