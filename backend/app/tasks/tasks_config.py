from pydantic_settings import BaseSettings, SettingsConfigDict


class TasksSettings(BaseSettings):
    REDIS_URL: str
    REDIS_HOST: str

    model_config = SettingsConfigDict(env_file="C:\\programs\\project\\backend\\.env", extra="ignore")

    def get_redis_url(self):
        return f"{tasks_settings.REDIS_URL}:{tasks_settings.REDIS_HOST}"
    

tasks_settings = TasksSettings()