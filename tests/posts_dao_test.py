from posts_dao import PostsDAO


def test_get_posts_all():
    data = PostsDAO()
    assert isinstance(data.get_posts_all(), list), 'Wrong loaded data'
    assert isinstance(data.get_posts_all()[0], dict), 'Wrong loaded data'


def test_get_posts_by_user():
    data = PostsDAO()
    pass


def test_get_post_by_pk():
    data = PostsDAO()
    pass