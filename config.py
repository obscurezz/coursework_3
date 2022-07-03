from pathlib import Path

BASE_DIR: Path = Path(__file__).resolve().parent

LOGS_FOLDER: Path = BASE_DIR.joinpath('logs')

DATA_FOLDER: Path = BASE_DIR.joinpath('data')

COMMENTS: Path = DATA_FOLDER.joinpath('comments.json')