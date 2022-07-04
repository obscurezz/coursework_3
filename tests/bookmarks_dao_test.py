from bookmarks_dao import BookmarksDAO

def test_get_all_bookmarks():
    data = BookmarksDAO()
    assert isinstance(data.get_all_bookmarks(), list), 'Wrong loaded data'
    if len(data.get_all_bookmarks()) > 0:
        assert isinstance(data.get_all_bookmarks()[0], dict), 'Wrong loaded data'