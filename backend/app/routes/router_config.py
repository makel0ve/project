from pydantic_settings import BaseSettings, SettingsConfigDict


class RouterSettings(BaseSettings):
    MAX_SIZE_TEXT: int

    model_config = SettingsConfigDict(env_file="C:\\programs\\project\\backend\\.env", extra="ignore")

    def get_max_size_text(self):
        return self.MAX_SIZE_TEXT
        
    
router_settings = RouterSettings()