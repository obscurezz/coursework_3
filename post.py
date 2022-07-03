from dataclasses import dataclass


@dataclass
class Post:
    poster_name: str
    poster_avatar: str
    pic: str
    content: str
    views_count: int
    likes_count: int
    pk: int
