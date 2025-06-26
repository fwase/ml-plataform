from datetime import datetime

class LogInferenceAPI:

    def append_log(log: dict):
        with open("abc.json", "a+") as file_log:
            file_log.write(log)

    def log(
            model_name: str,
            predicted_time_ms: float,
            predicted_value: str
        ):
        log = {
            "model_name": model_name,
            "predicted_time_ms": predicted_time_ms,
            "predicted_value": str(predicted_value),
            "predicted_datetime": datetime.now()
        }
        
        LogInferenceAPI.append_log(log)
