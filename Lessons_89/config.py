from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DB_HOST: str
    DB_PORT: str
    DB_USER: str
    DB_PASS: str
    DB_NAME: str

    # @property
    # def DATABASE_URL_asyncpg(self):
    #
    #
    #
    # def DATABASE_URL_psycopg(self):
    #
    #
    # model_config = SettingsConfigDict(env_file=".env")
#
# settings = Settings()
