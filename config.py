from models.user import User
from pathlib import Path

BASE_URL: str = "https://trello.com/"

STANDARD_USER: User = User(
    email="sveta1978medved@gmail.com",
    password="Medqwerty12345!",
)

BASE_DIR: Path = Path(__file__).resolve().parent
DATA_PATH: Path = BASE_DIR / "data"
PROFILE_PHOTO_PATH_CAT: Path = DATA_PATH / "cat4.jpg"
PROFILE_PHOTO_PATH_ZEBRA: Path = DATA_PATH / "zebra.jpg"
