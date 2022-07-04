from pathlib import Path

BASE_DIR: Path = Path(__file__).resolve().parent

LOGS_FOLDER: Path = BASE_DIR.joinpath('logs')

DATA_FOLDER: Path = BASE_DIR.joinpath('data')

DATA: Path = DATA_FOLDER.joinpath('data.json')

COMMENTS: Path = DATA_FOLDER.joinpath('comments.json')

BOOKMARKS: Path = DATA_FOLDER.joinpath('bookmarks.json')
