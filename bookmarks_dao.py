import json

from config import BOOKMARKS


class BookmarksDAO:
    """
    realizes methods to manipulate with bookmarks
    """
    @staticmethod
    def load_all_bookmarks():
        """
        :return: bookmarks as list of dicts (parsed json)
        """
        with open(BOOKMARKS, "r", encoding="utf-8") as file:
            bookmarks = json.load(file)
        return bookmarks

    @staticmethod
    def save_bookmark_to_json(bookmarks):
        """
        :param bookmarks: file data/bookmarks.json
        :return: nothing, just saves data to file
        """
        with open(BOOKMARKS, "w", encoding="utf-8") as file:
            json.dump(bookmarks, file, ensure_ascii=False)

    def get_all_bookmarks(self):
        """
        :return: all bookmarks as list of dicts
        """
        bookmarks = self.load_all_bookmarks()
        return bookmarks

    def add_bookmark(self, bookmark):
        """
        :param bookmark: post which will be added do bookmarks.json
        :return: updated file
        """
        bookmarks = self.get_all_bookmarks()
        if bookmark not in bookmarks:
            bookmarks.append(bookmark)
            self.save_bookmark_to_json(bookmarks)

        return bookmarks

    def delete_bookmark(self, post_id):
        """
        :param post_id: pk of post which will be deleted from bookmarks
        :return: updated file
        """
        bookmarks = self.get_all_bookmarks()
        for index, bookmark in enumerate(bookmarks):
            if bookmark['pk'] == post_id:
                del bookmarks[index]
                break
        self.save_bookmark_to_json(bookmarks)


