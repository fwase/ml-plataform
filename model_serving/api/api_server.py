from fastapi import FastAPI, status, HTTPException

from .inference import Inference
from .schemas.schemas import InferenceRequest, InferenceResponse

app = FastAPI()

@app.get("/health-check", status_code=status.HTTP_200_OK)
def health_check():
    return {"message": "Health Check: OK!"}

@app.post("/inference/{model_name}", status_code=status.HTTP_200_OK)
def inference(model_name: str, request: InferenceRequest) -> InferenceResponse:
    try:
        result = Inference.run(model_name, request)

        return result
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )
