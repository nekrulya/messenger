import dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path


dotenv.load_dotenv()

# API Settings
class APIUrlsSettings(BaseSettings):
    """Configure public urls."""

    docs: str = "/docs"
    redoc: str = "/redoc"

# Database Settings
class DatabaseSettings(BaseSettings):
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_HOST: str
    POSTGRES_PORT: int
    POSTGRES_NAME: str

    @property
    def url(self) -> str:
        return f"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_NAME}"

    class Config:
        env_file = "../.env"


# class KafkaSettings(BaseSettings):
#     bootstrap_servers: str = "localhost:9092"


# Logging Settings
class LoggingSettings(BaseSettings):
    """Configure the logging engine."""

    # The time field can be formatted using more human-friendly tokens.
    # These constitute a subset of the one used by the Pendulum library
    # https://pendulum.eustace.io/docs/#tokens
    format: str = "{time:YYYY-MM-DD HH:mm:ss} | {level: <5} | {message}"

    # The .log filename
    file: str = "backend"

    # The .log file Rotation
    rotation: str = "1MB"

    # The type of compression
    compression: str = "zip"


class AccessTokenSettings(BaseSettings):
    secret_key: str = "invaliad"
    ttl: int = 100  # seconds


class RefreshTokenSettings(BaseSettings):
    secret_key: str = "invaliad"
    ttl: int = 100  # seconds


class AuthenticationSettings(BaseSettings):
    access_token: AccessTokenSettings = AccessTokenSettings()
    refresh_token: RefreshTokenSettings = RefreshTokenSettings()
    algorithm: str = "HS256"
    scheme: str = "Bearer"

class Settings(BaseSettings):
    DEBUG: bool
    VERSION: str

    # Project file system
    root_dir: Path
    src_dir: Path

    # Infrastructure settings
    database: DatabaseSettings = DatabaseSettings()

    # Application configuration
    logging: LoggingSettings = LoggingSettings()
    authentication: AuthenticationSettings = AuthenticationSettings()

    class Config:
        env_file = "../.env"


ROOT_PATH = Path(__file__).parent.parent

settings = Settings(
    root_dir=ROOT_PATH,
    src_dir=ROOT_PATH / "src",
)