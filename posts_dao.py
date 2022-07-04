import json

from config import DATA, DATA_FOLDER, COMMENTS


class PostsDAO:
    """
    Realizes methods to manipulate with json data from file
    """
    @staticmethod
    def get_posts_all() -> list[dict] | Exception:
        """
        :return: loaded data from json file
        """
        if str(DATA).endswith('.json'):
            try:
                with open(DATA, 'r', encoding='utf-8') as file:
                    loaded_json = json.load(file)
                    return loaded_json
            except (FileExistsError, FileNotFoundError):
                raise FileNotFoundError(f'File not found or does not exist. Check the file in {DATA_FOLDER}')
        else:
            raise Exception('File extension is not json. Use the correct file.')

    def get_posts_by_user(self, user_name: str) -> list[dict] | Exception:
        """
        :param user_name: should be equal to "poster_name" key of posts in json file
        :return: loaded data for this user
        """
        user_list = set([post['poster_name'] for post in self.get_posts_all()])
        if user_name not in user_list:
            raise ValueError(f'User *{user_name}* does not exist.')

        user_posts: list[dict] = [post for post in self.get_posts_all() if
                                  post['poster_name'].lower() == user_name.lower()]

        return user_posts

    def get_post_by_pk(self, pk: int) -> dict:
        """
        :param pk: pk value of dict in json file
        :return: exact post with this pk
        """
        for post in self.get_posts_all():
            if pk == post['pk']:
                return post

    @staticmethod
    def get_comments_by_post_id(post_id: int) -> list[tuple]:
        with open(COMMENTS, 'r', encoding='utf-8') as file:
            comments = [(block['commenter_name'], block['comment']) for block in json.load(file) if
                        block['post_id'] == post_id]
        return comments
