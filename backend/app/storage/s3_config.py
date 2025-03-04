from pydantic_settings import BaseSettings, SettingsConfigDict


class StorageSettings(BaseSettings):
    ACCESS_KEY_ID: str
    SECRET_KEY: str
    REGION: str
    ENDPOINT_URL: str
    SERVICE_NAME: str
    BUCKET_NAME: str

    model_config = SettingsConfigDict(env_file="C:\\programs\\project\\backend\\.env", extra="ignore")

    def get_access_key_id(self):
        return self.ACCESS_KEY_ID
    
    def get_secret_key(self):
        return self.SECRET_KEY
    
    def get_region(self):
        return self.REGION
    
    def get_endpoint_url(self):
        return self.ENDPOINT_URL
    
    def get_service_name(self):
        return self.SERVICE_NAME
    
    def get_bucket_name(self):
        return self.BUCKET_NAME
    

storage_settings = StorageSettings()