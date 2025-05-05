.PHONY: run-api-inference
run-api-inference:
	poetry run uvicorn model_serving.api.api_server:app --port 8000 --reload
