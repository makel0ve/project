from pydantic_settings import BaseSettings, SettingsConfigDict


class TasksSettings(BaseSettings):
    REDIS_URL: str
    REDIS_HOST: str

    model_config = SettingsConfigDict(env_file="C:\\programs\\project\\backend\\.env", extra="ignore")

    def get_redis_url(self):
        return f"{self.REDIS_URL}:{self.REDIS_HOST}"
    

tasks_settings = TasksSettings()