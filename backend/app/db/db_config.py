from pydantic_settings import BaseSettings, SettingsConfigDict


class DBSettings(BaseSettings):
    DB_HOST: str
    DB_PORT: str
    DB_NAME: str
    DB_USER: str
    DB_PASS: str

    model_config = SettingsConfigDict(env_file="C:\\programs\\project\\backend\\.env", extra="ignore")

    def get_database_url(self):
        return f"postgresql+asyncpg://{db_settings.DB_USER}:{db_settings.DB_PASS}@{db_settings.DB_HOST}:{db_settings.DB_PORT}/{db_settings.DB_NAME}"
    
    
db_settings = DBSettings()