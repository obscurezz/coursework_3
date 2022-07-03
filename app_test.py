from app import app


def test_app():
    response = app.test_client().get('/')
    assert response.status_code == 200, 'application is not reachable'


def test_api_posts():
    response = app.test_client().get('/api/posts')
    keys = [post.keys() for post in response.json]

    assert response.status_code == 200, 'api is not reachable'
    assert response.is_json is True, 'Result is not json'
    assert all('pk' in obj for obj in keys), 'There is not a valid key in json'


def test_exact_post():
    test_values = (1, 3, 5)
    keys = ["poster_name", "poster_avatar", "pic", "content", "views_count", "likes_count", "pk"]
    for x in test_values:
        response = app.test_client().get(f'/api/posts/{x}')

        assert response.status_code == 200, 'api is not reachable'
        assert isinstance(response.json, dict), 'Result is not dict'
        assert list(response.json.keys()) == sorted(keys), 'Result keys are not valid'

