from flask import Blueprint, render_template, redirect

from posts_dao import PostsDAO
from bookmarks_dao import BookmarksDAO

POSTS = PostsDAO()
BOOKMARKS = BookmarksDAO()

bookmarks_blueprint = Blueprint('bookmarks_blueprint', __name__, template_folder='../templates')


@bookmarks_blueprint.route('/bookmarks', methods=['GET'])
def all_bookmarks():
    """
    :return: bookmarks.html
    """
    bookmarks = BOOKMARKS.get_all_bookmarks()
    return render_template('bookmarks.html', posts=bookmarks)


@bookmarks_blueprint.route('/bookmarks/add/<int:post_id>', methods=['POST'])
def add_bookmark(post_id: int):
    """
    :param post_id: pk of post which be added to the bookmarks
    :return: adds post to the bookmarks and redirects to main
    """
    post = POSTS.get_post_by_pk(post_id)
    BOOKMARKS.add_bookmark(post)
    return redirect("/", code=302)


@bookmarks_blueprint.route('/bookmarks/remove/<int:post_id>', methods=['POST'])
def delete_bookmark(post_id: int):
    """
    :param post_id: pk of post which be deleted from the bookmarks
    :return: deletes post from the bookmarks and redirects to main
    """
    BOOKMARKS.delete_bookmark(post_id)
    return redirect("/", code=302)