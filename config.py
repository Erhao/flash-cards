# -*- coding: utf-8 -*-
from pydantic import BaseSettings


class Settings(BaseSettings):
    # the configs below will be override with configs in .env, ignore the case
    app_name: str = "flash-cards"
    mongodb_host: str = ""
    mongodb_port: int = 27017
    mongodb_database: str = "flash-cards"

    class Config:
        env_file = ".env"


settings = Settings()
